from LangParser import LangParser
from LangVisitor import LangVisitor

class InstructionGenerator(LangVisitor):

    def __init__(self, table):
        self.symbol_table = table
        self.labels = 0
    
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
    
    def visitDeclaration(self, ctx):
        var_type = ctx.primitiveType().getText()[0].upper()
        for id in ctx.IDENTIFIER():
            name = id.getText()
            if var_type == "I":
                print(f"push I 0")
            elif var_type == "F":
                print(f"push I 0.0")
            elif var_type == "S":
                print(f'push S ""')
            elif var_type == "B":
                print(f"push B false")
            print(f"save {name}")
        
    def visitAssignment(self, ctx):
        var_name = ctx.IDENTIFIER().getText()
        print ("assign")

    def visitIfElse(self, ctx):
        lbl1 = self.labels
        self.labels = self.labels + 1
        lbl2 = self.labels
        self.labels = self.labels + 1

        self.visit(ctx.condition().expr())
        print(f"fjmp {lbl1}")
        self.visit(ctx.statement(0))
        print(f"jmp {lbl2}")
        print(f"label {lbl1}")
        if ctx.ELSE_KEYWORD():
           self.visit(ctx.statement(1))
        print(f"label {lbl2}")

    def visitWhileLoop(self, ctx):
        lbl1 = self.labels
        self.labels = self.labels + 1
        lbl2 = self.labels
        self.labels = self.labels + 1

        print(f"label {lbl1}")
        self.visit(ctx.condition().expr())
        print(f"fjmp {lbl2}")
        self.visit(ctx.statement())
        print(f"jmp {lbl1}")
        print(f"label {lbl2}")
        
    
    def visitWriteExp(self, ctx):
        vals = 0
        for e in ctx.expr():
          self.visit(e)
          vals = vals+1
        print(f"print {vals}")
    
    def visitConcat(self, ctx):
        self.visit(ctx.expr(0))
        self.visit(ctx.expr(1))
        print("concat")
        return "string"
    
    def visitLogic(self, ctx):
        op = ctx.getChild(1).getText()
        self.visit(ctx.expr(0))
        self.visit(ctx.expr(1))
        if op == "||":
            print("or")
        else:
            print("and")
        return "bool"
    
    def visitRelational(self, ctx):
        op = ctx.getChild(1)
        if self.visit(ctx.expr(0)) == "int" and self.visit(ctx.expr(1)) == "int":
            if op == '>':
                print ("gt I")
            else:
                print ("lt I")


    
