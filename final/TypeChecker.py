from LangListener import LangListener
from LangParser import LangParser

class TypeChecker(LangListener):

    def __init__(self):
        self.symbol_table = {}  # identifikátor -> typ
        self.types = {}         # kontext -> typ výrazu
        self.errors = []
    
    def error(self, ctx, message):
        line = ctx.start.line
        self.errors.append(f"Error on line {line}: {message}")
    
    def exitDeclaration(self, ctx):
        type = ctx.primitiveType().getText()

        for id_token in ctx.IDENTIFIER():
            var_name = id_token.getText()
            if var_name in self.symbol_table:
                self.error(ctx, "Variable already declared")
            else:
                self.symbol_table[var_name] = type
    
    def exitInt(self, ctx):
        self.types[ctx] = 'int'
    
    def exitFloat(self, ctx):
        self.types[ctx] = 'float'
    
    def exitBool(self, ctx):
        self.types[ctx] = 'bool'
    
    def exitString(self, ctx):
        self.types[ctx] = 'string'

    def exitId(self, ctx):
        var_name = ctx.getText()
        if var_name not in self.symbol_table:
            self.error(ctx, "Undeclared variable '{var_name}'.")
            self.types[ctx] = 'error'
        else:
            self.types[ctx] =self.symbol_table[var_name]
    
    def exitAssignment(self, ctx):
        var_name = ctx.IDENTIFIER().getText()
        expr_type = self.types[ctx.expr()]
    
        if var_name not in self.symbol_table:
            self.error(ctx, f"Undeclared variable '{var_name}'.")
        else:
            var_type = self.symbol_table[var_name]
            if var_type == expr_type:
                self.types[ctx] = var_type
            elif var_type == 'float' and expr_type == 'int':
                self.types[ctx] = 'float'
            else:
                self.error(ctx, f"Cannot convert '{expr_type}' to '{var_type}'.")
                self.types[ctx] = 'error'

    def exitAddSub(self, ctx):
        left = self.types[ctx.expr(0)]
        right = self.types[ctx.expr(1)]

        if 'string' in (left, right) or 'bool' in (left, right):
            self.error(ctx, "Cannot count with this type.")
            self.types[ctx] = 'error'
        elif 'float' in (left, right):
            self.types[ctx] = 'float'
        else:
            self.types[ctx] = 'int'
    
    def exitMulDiv(self, ctx):
        left = self.types[ctx.expr(0)]
        right = self.types[ctx.expr(1)]
        if 'string' in (left, right) or 'bool' in (left, right):
            self.error(ctx, "Cannot count with this type.")
            self.types[ctx] = 'error'
        elif 'float' in (left, right):
            self.types[ctx] = 'float'
        else:
            self.types[ctx] = 'int'

    def exitModulo(self, ctx):
        left = self.types[ctx.expr(0)]
        right = self.types[ctx.expr(1)]
        if left != 'int' and right != 'int':
            self.error(ctx,"Modulo supported only with ingere numbers.")
            self.types[ctx] = 'error'
        
        else:
            self.types[ctx] = 'int'
    
    def exitCompare(self, ctx):
        self.types[ctx] = 'bool'
    
    def exitRelational(self, ctx):
        self.types[ctx] = 'bool'

    def exitLogic(self, ctx):
        left = self.types[ctx.expr(0)]
        right = self.types[ctx.expr(1)]
        if left != 'bool' or right != 'bool':
            self.error(ctx, "Logic operations supported only with bool.")
            self.types[ctx] = 'error'
        else:
            self.types[ctx] = 'bool'

    def exitNot(self, ctx):
        expr_type = self.types[ctx.expr()]
        if expr_type != 'bool':
            self.error(ctx, "Not operation only with bool.")
            self.types[ctx] = 'error'
        else:
            self.types[ctx] = 'bool'
    
    def exitUnaryMinus(self, ctx):
        expr_type = self.types[ctx.expr()]
        if expr_type == 'int' or expr_type == 'float':
            self.types[ctx] = expr_type
        else:
            self.error(ctx, "Unary minus only with number.")
            self.types[ctx] = 'error'
    
    def exitConcat(self, ctx):
        left = self.types[ctx.expr(0)]
        right = self.types[ctx.expr(1)]
        if left == 'string' and right == 'string':
            self.types[ctx] = 'string'
        else:
            self.error(ctx, "Concatenation only with strings.")
            self.types[ctx] = 'error'
    
    def exitParens(self, ctx):
        self.types[ctx] = self.types[ctx.expr()]

    def exitPrintExpr(self, ctx):
        self.types[ctx.expr()]  # Trigger type checking

    def exitIfElse(self, ctx):
        cond_type = self.types[ctx.condition().expr()]
        if cond_type != 'bool':
            self.error(ctx, "Condition must be in bool.")

    def exitWhileLoop(self, ctx):
        cond_type = self.types[ctx.condition().expr()]
        if cond_type != 'bool':
            self.error(ctx, "Condition must be in bool.")