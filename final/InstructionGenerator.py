from LangParser import LangParser
from LangVisitor import LangVisitor

class InstructionGenerator(LangVisitor):

    def __init__(self, table):
        self.symbol_table = table
    
    def visitInt(self, ctx):
        val = ctx.getText()
        print(f"push I {val}")
        return "int"
    
    def visitFloat(self, ctx):
        val = ctx.getText()
        print(f"push F {val}")
        return "float"

    def visitBoolFalse(self, ctx):
        print(f"push B false")
        return "bool"
    
    def visitBoolTrue(self, ctx):
        print(f"push B true")
        return "bool"
    
    def visitString(self, ctx):
        val = ctx.getText()
        print(f"push S {val}")
        return "string"
    
    def visitWriteExp(self, ctx):
        vals = 0
        for e in ctx.expr():
          self.visit(e)
          vals = vals+1
        print(f"print {vals}")
    
    def visitRelational(self, ctx):
        op = ctx.getChild(1)
        if self.visit(ctx.expr(0)) == "int" and self.visit(ctx.expr(1)) == "int":
            if op == '>':
                print ("gt I")
            else:
                print ("lt I")


    
