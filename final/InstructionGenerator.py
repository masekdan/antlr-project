from LangParser import LangParser
from LangVisitor import LangVisitor

class InstructionGenerator(LangVisitor):

    def __init__(self, table, file):
        self.symbol_table = table
        self.labels = 0
        self.file = file
    
    def visitInt(self, ctx):
        val = ctx.getText()
        self.file.write(f"push I {val}\n")
        return "int"
    
    def visitFloat(self, ctx):
        val = ctx.getText()
        self.file.write(f"push F {val}\n")
        return "float"

    def visitBoolFalse(self, ctx):
        self.file.write(f"push B false\n")
        return "bool"
    
    def visitBoolTrue(self, ctx):
        self.file.write(f"push B true\n")
        return "bool"
    
    def visitString(self, ctx):
        val = ctx.getText()
        self.file.write(f"push S {val}\n")
        return "string"
    
    def visitDeclaration(self, ctx):
        var_type = ctx.primitiveType().getText()[0].upper()
        for id in ctx.IDENTIFIER():
            name = id.getText()
            if var_type == "I":
                self.file.write(f"push I 0\n")
            elif var_type == "F":
                self.file.write(f"push I 0.0\n")
            elif var_type == "S":
                self.file.write(f'push S ""\n')
            elif var_type == "B":
                self.file.write(f"push B false\n")
            self.file.write(f"save {name}")
        
    def visitAssignment(self, ctx):
        var_name = ctx.IDENTIFIER().getText()
        self.file.write("assign\n")

    def visitIfElse(self, ctx):
        lbl1 = self.labels
        self.labels = self.labels + 1
        lbl2 = self.labels
        self.labels = self.labels + 1

        self.visit(ctx.condition().expr())
        self.file.write(f"fjmp {lbl1}\n")
        self.visit(ctx.statement(0))
        self.file.write(f"jmp {lbl2}\n")
        self.file.write(f"label {lbl1}\n")
        if ctx.ELSE_KEYWORD():
           self.visit(ctx.statement(1))
        self.file.write(f"label {lbl2}\n")

    def visitWhileLoop(self, ctx):
        lbl1 = self.labels
        self.labels = self.labels + 1
        lbl2 = self.labels
        self.labels = self.labels + 1

        self.file.write(f"label {lbl1}\n")
        self.visit(ctx.condition().expr())
        self.file.write(f"fjmp {lbl2}\n")
        self.visit(ctx.statement())
        self.file.write(f"jmp {lbl1}\n")
        self.file.write(f"label {lbl2}\n")
        
    
    def visitWriteExp(self, ctx):
        vals = 0
        for e in ctx.expr():
          self.visit(e)
          vals = vals+1
        self.file.write(f"print {vals}\n")
    
    def visitConcat(self, ctx):
        self.visit(ctx.expr(0))
        self.visit(ctx.expr(1))
        self.file.write("concat\n")
        return "string"
    
    def visitUnaryMinus(self, ctx):
        type = self.visit(ctx.expr())
        self.file.write(f"uminus {type[0].upper()}\n")
        return type
    
    def visitLogic(self, ctx):
        op = ctx.getChild(1).getText()
        self.visit(ctx.expr(0))
        self.visit(ctx.expr(1))
        if op == "||":
            self.file.write("or\n")
        else:
            self.file.write("and\n")
        return "bool"
    
    def visitMulDiv(self, ctx):
        op = ctx.getChild(1).getText()
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))

        if left == "int" and right == "int":
            if op == "*":
                self.file.write("mul I\n")
            else:
                self.file.write("div I\n")
        
        elif left == "float" and right == "float":
            if op == "*":
                self.file.write("mul F\n")
            else:
                self.file.write("div F\n")
        
        elif left == "float" and right == "int":
            self.file.write("itof\n")
            if op == "*":
                self.file.write("mul F\n")
            else:
                self.file.write("div F\n")
    
    def visitModulo(self, ctx):
        self.visit(ctx.expr(0))
        self.visit(ctx.expr(1))
        self.file.write("mod\n")
        return "int"


    def visitRelational(self, ctx):
        op = ctx.getChild(1).getText()
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        if left == "int" and right == "int":
            if op == '>':
                self.file.write("gt I\n")
            else:
                self.file.write("lt I\n")

        if left == "float" and right == "float":
            if op == '>':
                self.file.write("gt F\n")
            else:
                self.file.write("lt F\n")

    def visitBlockExp(self, ctx):
        for stmt in ctx.statement():
            self.visit(stmt)
    
    def visitParens(self, ctx):
        return self.visit(ctx.expr())


    
