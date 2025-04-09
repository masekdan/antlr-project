from LangParser import LangParser
from LangVisitor import LangVisitor

class TypeChecker(LangVisitor):

    def __init__(self):
      self.symbol_table = {} # jmeno , typ
      self.errors = []
    
    def error(self, ctx, message):
      line = ctx.start.line
      self.errors.append(f"Error on line {line}: {message}")
    
    def visitProgram(self, ctx):
        for stmt in ctx.statement():
          self.visit(stmt)
        return
    
    def visitDeclaration(self, ctx):
        var_type = ctx.primitiveType().getText()
        for id in ctx.IDENTIFIER():
            name = id.getText()
            if name in self.symbol_table:
              self.error(ctx, f"Variable '{name}' already declared.")
            else:
               self.symbol_table[name] = var_type
        return
    
    def visitAssignment(self, ctx):
        var_name = ctx.IDENTIFIER().getText()
        expr_type = self.visit(ctx.expr())
        if var_name not in self.symbol_table:
           self.error(ctx,f"Undeclared variable '{var_name}'.")
        else:
           var_type = self.symbol_table[var_name]
           if var_type == expr_type or (var_type == "float" and expr_type == "int"):   #itof
               return var_type
           else:
              self.error(ctx, f"Cannot convert '{expr_type}' to '{var_type}'.")
              return "error"
           
    def visitId(self, ctx):
       name = ctx.getText()
       if name not in self.symbol_table:
          self.error(ctx, f"Undeclared variable '{name}'.")
          return "error"
       return self.symbol_table[name]
    
    def visitInt(self, ctx):
       val = ctx.getText()
       return "int"
    
    def visitFloat(self, ctx):
       val = ctx.getText()
       return "float"
    
    def visitBoolTrue(self, ctx):
       return "bool"
    
    def visitBoolFalse(self, ctx):
       return "bool"
    
    def visitString(self, ctx):
       val = ctx.getText()
       return "string"

    def visitAddSub(self, ctx):
       left = self.visit(ctx.expr(0))
       right = self.visit(ctx.expr(1))
       if "string" in (left,right) or "bool" in (left,right):
          self.error(ctx, "Only with numerical operations.")
          return "error"
       elif "float" in (left,right):
          return "float"
       else:
          return "int"
    
    def visitMulDiv(self, ctx):
       left = self.visit(ctx.expr(0))
       right = self.visit(ctx.expr(1))
       if "string" in (left,right) or "bool" in (left,right):
          self.error(ctx, "Only with numerical operations.")
          return "error"
       elif "float" in (left,right):
          return "float"
       else:
          return "int"
       
    def visitModulo(self, ctx):
       left = self.visit(ctx.expr(0))
       right = self.visit(ctx.expr(1))
       if left != "int" or right != "int":
          self.error(ctx,"Modulo only works with integer.")
          return "error"
       return "int"
    
    def visitNot(self, ctx):
       value_type = self.visit(ctx.expr())
       if value_type != "bool":
          self.error(ctx, "Only works with boolean.")
          return "error"
       return "bool"
    
    def visitLogicAnd(self, ctx):
       left = self.visit(ctx.expr(0))
       right = self.visit(ctx.expr(1))
       if left != "bool" or right != "bool":
          self.error(ctx,"Logic operators only works with boolean.")
          return "error"
       return "bool"
    
    def visitLogicOr(self, ctx):
       left = self.visit(ctx.expr(0))
       right = self.visit(ctx.expr(1))
       if left != "bool" or right != "bool":
          self.error(ctx,"Logic operators only works with boolean.")
          return "error"
       return "bool"
    
    def visitCompare(self, ctx):
       left = self.visit(ctx.expr(0))
       right = self.visit(ctx.expr(1))
       if left != right:
          self.error(ctx,"Cannot compare different types.")
          return "error"
       return "bool"
    
    def visitRelational(self, ctx):
       left = self.visit(ctx.expr(0))
       right = self.visit(ctx.expr(1))
       if left not in ['int','float'] or right not in ['int','float']:
          self.error(ctx,"Cannot compare different types.")
          return "error"
       return "bool"
    
    def visitUnaryMinus(self, ctx):
       value_type = self.visit(ctx.expr())
       if value_type not in ("int", "float"):
          self.error(ctx, "Only works with numeric type.")
          return "error"
       return value_type
    
    def visitConcat(self, ctx):
       left = self.visit(ctx.expr(0))
       right = self.visit(ctx.expr(1))
       if left != "string" and right != "string":
          self.error(ctx,"Concatenation only works with strings.")
          return "error"
       return "string"
    
    def visitParens(self, ctx):
       return self.visit(ctx.expr())
    
    def visitIfElse(self, ctx):
        cond_type = self.visit(ctx.condition().expr())
        if cond_type != "bool":
          self.error(ctx, "Condition must be boolean type.")
        self.visit(ctx.statement(0))
        if ctx.ELSE_KEYWORD():
           self.visit(ctx.statement(1))
    
    def visitWhileLoop(self, ctx):
        cond_type = self.visit(ctx.condition().expr())
        if cond_type != "bool":
          self.error(ctx, "Condition must be boolean type.")
        self.visit(ctx.statement())

    def visitPrintExpr(self, ctx):
       self.visit(ctx.expr())
    
    def visitBlockExp(self, ctx):
       for stmt in ctx.statement():
          self.visit(stmt)
    
    def visitReadExp(self, ctx):
       for id in ctx.IDENTIFIER():
          name = id.getText()
          if name not in self.symbol_table:
             self.error(ctx, f"Variable '{name}' undeclared.")
    
    def visitWriteExp(self, ctx):
       for e in ctx.expr():
          self.visit(e)

    def visitTernary(self, ctx):
         cond_type = self.visit(ctx.expr(0))
         left = self.visit(ctx.expr(1))
         right = self.visit(ctx.expr(2))

         if cond_type != 'bool':
            self.error(ctx,"Condidtion must be bool.")
            return "error"
         
         if right=="string" and left == "string":
            return "string"
         elif right=="bool" and left == "bool":
            return "string"
         elif "float" in (left,right):
            return "float"
         elif right == "int" and left == "int":
            return "int"
         else:
            self.error(ctx,"Expressions are not the same type")
            return "error"
          