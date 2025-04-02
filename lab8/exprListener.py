# Generated from expr.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .exprParser import exprParser
else:
    from exprParser import exprParser

# This class defines a complete listener for a parse tree produced by exprParser.
class exprListener(ParseTreeListener):

    # Enter a parse tree produced by exprParser#program.
    def enterProgram(self, ctx:exprParser.ProgramContext):
        pass

    # Exit a parse tree produced by exprParser#program.
    def exitProgram(self, ctx:exprParser.ProgramContext):
        pass


    # Enter a parse tree produced by exprParser#declaration.
    def enterDeclaration(self, ctx:exprParser.DeclarationContext):
        pass

    # Exit a parse tree produced by exprParser#declaration.
    def exitDeclaration(self, ctx:exprParser.DeclarationContext):
        pass


    # Enter a parse tree produced by exprParser#printExpr.
    def enterPrintExpr(self, ctx:exprParser.PrintExprContext):
        pass

    # Exit a parse tree produced by exprParser#printExpr.
    def exitPrintExpr(self, ctx:exprParser.PrintExprContext):
        pass


    # Enter a parse tree produced by exprParser#parens.
    def enterParens(self, ctx:exprParser.ParensContext):
        pass

    # Exit a parse tree produced by exprParser#parens.
    def exitParens(self, ctx:exprParser.ParensContext):
        pass


    # Enter a parse tree produced by exprParser#assignment.
    def enterAssignment(self, ctx:exprParser.AssignmentContext):
        pass

    # Exit a parse tree produced by exprParser#assignment.
    def exitAssignment(self, ctx:exprParser.AssignmentContext):
        pass


    # Enter a parse tree produced by exprParser#addSub.
    def enterAddSub(self, ctx:exprParser.AddSubContext):
        pass

    # Exit a parse tree produced by exprParser#addSub.
    def exitAddSub(self, ctx:exprParser.AddSubContext):
        pass


    # Enter a parse tree produced by exprParser#id.
    def enterId(self, ctx:exprParser.IdContext):
        pass

    # Exit a parse tree produced by exprParser#id.
    def exitId(self, ctx:exprParser.IdContext):
        pass


    # Enter a parse tree produced by exprParser#float.
    def enterFloat(self, ctx:exprParser.FloatContext):
        pass

    # Exit a parse tree produced by exprParser#float.
    def exitFloat(self, ctx:exprParser.FloatContext):
        pass


    # Enter a parse tree produced by exprParser#int.
    def enterInt(self, ctx:exprParser.IntContext):
        pass

    # Exit a parse tree produced by exprParser#int.
    def exitInt(self, ctx:exprParser.IntContext):
        pass


    # Enter a parse tree produced by exprParser#mulDiv.
    def enterMulDiv(self, ctx:exprParser.MulDivContext):
        pass

    # Exit a parse tree produced by exprParser#mulDiv.
    def exitMulDiv(self, ctx:exprParser.MulDivContext):
        pass


    # Enter a parse tree produced by exprParser#primitiveType.
    def enterPrimitiveType(self, ctx:exprParser.PrimitiveTypeContext):
        pass

    # Exit a parse tree produced by exprParser#primitiveType.
    def exitPrimitiveType(self, ctx:exprParser.PrimitiveTypeContext):
        pass



del exprParser