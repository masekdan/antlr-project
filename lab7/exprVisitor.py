# Generated from expr.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .exprParser import exprParser
else:
    from exprParser import exprParser

# This class defines a complete generic visitor for a parse tree produced by exprParser.

class exprVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by exprParser#prog.
    def visitProg(self, ctx:exprParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by exprParser#Integer.
    def visitInteger(self, ctx:exprParser.IntegerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by exprParser#Par.
    def visitPar(self, ctx:exprParser.ParContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by exprParser#Add.
    def visitAdd(self, ctx:exprParser.AddContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by exprParser#Octal.
    def visitOctal(self, ctx:exprParser.OctalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by exprParser#Hexa.
    def visitHexa(self, ctx:exprParser.HexaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by exprParser#Mul.
    def visitMul(self, ctx:exprParser.MulContext):
        return self.visitChildren(ctx)



del exprParser