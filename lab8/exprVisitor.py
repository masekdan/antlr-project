# Generated from expr.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .exprParser import exprParser
else:
    from exprParser import exprParser

# This class defines a complete generic visitor for a parse tree produced by exprParser.

class exprVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by exprParser#program.
    def visitProgram(self, ctx:exprParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by exprParser#declaration.
    def visitDeclaration(self, ctx:exprParser.DeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by exprParser#printExpr.
    def visitPrintExpr(self, ctx:exprParser.PrintExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by exprParser#parens.
    def visitParens(self, ctx:exprParser.ParensContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by exprParser#assignment.
    def visitAssignment(self, ctx:exprParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by exprParser#addSub.
    def visitAddSub(self, ctx:exprParser.AddSubContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by exprParser#id.
    def visitId(self, ctx:exprParser.IdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by exprParser#float.
    def visitFloat(self, ctx:exprParser.FloatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by exprParser#int.
    def visitInt(self, ctx:exprParser.IntContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by exprParser#mulDiv.
    def visitMulDiv(self, ctx:exprParser.MulDivContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by exprParser#primitiveType.
    def visitPrimitiveType(self, ctx:exprParser.PrimitiveTypeContext):
        return self.visitChildren(ctx)



del exprParser