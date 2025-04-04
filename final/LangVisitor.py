# Generated from Lang.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .LangParser import LangParser
else:
    from LangParser import LangParser

# This class defines a complete generic visitor for a parse tree produced by LangParser.

class LangVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by LangParser#program.
    def visitProgram(self, ctx:LangParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangParser#declaration.
    def visitDeclaration(self, ctx:LangParser.DeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangParser#printExpr.
    def visitPrintExpr(self, ctx:LangParser.PrintExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangParser#readExp.
    def visitReadExp(self, ctx:LangParser.ReadExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangParser#writeExp.
    def visitWriteExp(self, ctx:LangParser.WriteExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangParser#blockExp.
    def visitBlockExp(self, ctx:LangParser.BlockExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangParser#ifElse.
    def visitIfElse(self, ctx:LangParser.IfElseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangParser#whileLoop.
    def visitWhileLoop(self, ctx:LangParser.WhileLoopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangParser#parens.
    def visitParens(self, ctx:LangParser.ParensContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangParser#compare.
    def visitCompare(self, ctx:LangParser.CompareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangParser#bool.
    def visitBool(self, ctx:LangParser.BoolContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangParser#string.
    def visitString(self, ctx:LangParser.StringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangParser#assignment.
    def visitAssignment(self, ctx:LangParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangParser#addSub.
    def visitAddSub(self, ctx:LangParser.AddSubContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangParser#concat.
    def visitConcat(self, ctx:LangParser.ConcatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangParser#float.
    def visitFloat(self, ctx:LangParser.FloatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangParser#int.
    def visitInt(self, ctx:LangParser.IntContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangParser#mulDiv.
    def visitMulDiv(self, ctx:LangParser.MulDivContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangParser#not.
    def visitNot(self, ctx:LangParser.NotContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangParser#unaryMinus.
    def visitUnaryMinus(self, ctx:LangParser.UnaryMinusContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangParser#relational.
    def visitRelational(self, ctx:LangParser.RelationalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangParser#id.
    def visitId(self, ctx:LangParser.IdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangParser#logic.
    def visitLogic(self, ctx:LangParser.LogicContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangParser#modulo.
    def visitModulo(self, ctx:LangParser.ModuloContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangParser#condition.
    def visitCondition(self, ctx:LangParser.ConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangParser#primitiveType.
    def visitPrimitiveType(self, ctx:LangParser.PrimitiveTypeContext):
        return self.visitChildren(ctx)



del LangParser