# Generated from expr.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .exprParser import exprParser
else:
    from exprParser import exprParser

# This class defines a complete listener for a parse tree produced by exprParser.
class exprListener(ParseTreeListener):

    # Enter a parse tree produced by exprParser#prog.
    def enterProg(self, ctx:exprParser.ProgContext):
        pass

    # Exit a parse tree produced by exprParser#prog.
    def exitProg(self, ctx:exprParser.ProgContext):
        pass


    # Enter a parse tree produced by exprParser#Integer.
    def enterInteger(self, ctx:exprParser.IntegerContext):
        pass

    # Exit a parse tree produced by exprParser#Integer.
    def exitInteger(self, ctx:exprParser.IntegerContext):
        pass


    # Enter a parse tree produced by exprParser#Par.
    def enterPar(self, ctx:exprParser.ParContext):
        pass

    # Exit a parse tree produced by exprParser#Par.
    def exitPar(self, ctx:exprParser.ParContext):
        pass


    # Enter a parse tree produced by exprParser#Add.
    def enterAdd(self, ctx:exprParser.AddContext):
        pass

    # Exit a parse tree produced by exprParser#Add.
    def exitAdd(self, ctx:exprParser.AddContext):
        pass


    # Enter a parse tree produced by exprParser#Octal.
    def enterOctal(self, ctx:exprParser.OctalContext):
        pass

    # Exit a parse tree produced by exprParser#Octal.
    def exitOctal(self, ctx:exprParser.OctalContext):
        pass


    # Enter a parse tree produced by exprParser#Hexa.
    def enterHexa(self, ctx:exprParser.HexaContext):
        pass

    # Exit a parse tree produced by exprParser#Hexa.
    def exitHexa(self, ctx:exprParser.HexaContext):
        pass


    # Enter a parse tree produced by exprParser#Mul.
    def enterMul(self, ctx:exprParser.MulContext):
        pass

    # Exit a parse tree produced by exprParser#Mul.
    def exitMul(self, ctx:exprParser.MulContext):
        pass



del exprParser