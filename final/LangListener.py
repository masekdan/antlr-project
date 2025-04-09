# Generated from Lang.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .LangParser import LangParser
else:
    from LangParser import LangParser

# This class defines a complete listener for a parse tree produced by LangParser.
class LangListener(ParseTreeListener):

    # Enter a parse tree produced by LangParser#program.
    def enterProgram(self, ctx:LangParser.ProgramContext):
        pass

    # Exit a parse tree produced by LangParser#program.
    def exitProgram(self, ctx:LangParser.ProgramContext):
        pass


    # Enter a parse tree produced by LangParser#declaration.
    def enterDeclaration(self, ctx:LangParser.DeclarationContext):
        pass

    # Exit a parse tree produced by LangParser#declaration.
    def exitDeclaration(self, ctx:LangParser.DeclarationContext):
        pass


    # Enter a parse tree produced by LangParser#printExpr.
    def enterPrintExpr(self, ctx:LangParser.PrintExprContext):
        pass

    # Exit a parse tree produced by LangParser#printExpr.
    def exitPrintExpr(self, ctx:LangParser.PrintExprContext):
        pass


    # Enter a parse tree produced by LangParser#readExp.
    def enterReadExp(self, ctx:LangParser.ReadExpContext):
        pass

    # Exit a parse tree produced by LangParser#readExp.
    def exitReadExp(self, ctx:LangParser.ReadExpContext):
        pass


    # Enter a parse tree produced by LangParser#writeExp.
    def enterWriteExp(self, ctx:LangParser.WriteExpContext):
        pass

    # Exit a parse tree produced by LangParser#writeExp.
    def exitWriteExp(self, ctx:LangParser.WriteExpContext):
        pass


    # Enter a parse tree produced by LangParser#blockExp.
    def enterBlockExp(self, ctx:LangParser.BlockExpContext):
        pass

    # Exit a parse tree produced by LangParser#blockExp.
    def exitBlockExp(self, ctx:LangParser.BlockExpContext):
        pass


    # Enter a parse tree produced by LangParser#ifElse.
    def enterIfElse(self, ctx:LangParser.IfElseContext):
        pass

    # Exit a parse tree produced by LangParser#ifElse.
    def exitIfElse(self, ctx:LangParser.IfElseContext):
        pass


    # Enter a parse tree produced by LangParser#whileLoop.
    def enterWhileLoop(self, ctx:LangParser.WhileLoopContext):
        pass

    # Exit a parse tree produced by LangParser#whileLoop.
    def exitWhileLoop(self, ctx:LangParser.WhileLoopContext):
        pass


    # Enter a parse tree produced by LangParser#emptyCmd.
    def enterEmptyCmd(self, ctx:LangParser.EmptyCmdContext):
        pass

    # Exit a parse tree produced by LangParser#emptyCmd.
    def exitEmptyCmd(self, ctx:LangParser.EmptyCmdContext):
        pass


    # Enter a parse tree produced by LangParser#parens.
    def enterParens(self, ctx:LangParser.ParensContext):
        pass

    # Exit a parse tree produced by LangParser#parens.
    def exitParens(self, ctx:LangParser.ParensContext):
        pass


    # Enter a parse tree produced by LangParser#compare.
    def enterCompare(self, ctx:LangParser.CompareContext):
        pass

    # Exit a parse tree produced by LangParser#compare.
    def exitCompare(self, ctx:LangParser.CompareContext):
        pass


    # Enter a parse tree produced by LangParser#string.
    def enterString(self, ctx:LangParser.StringContext):
        pass

    # Exit a parse tree produced by LangParser#string.
    def exitString(self, ctx:LangParser.StringContext):
        pass


    # Enter a parse tree produced by LangParser#boolFalse.
    def enterBoolFalse(self, ctx:LangParser.BoolFalseContext):
        pass

    # Exit a parse tree produced by LangParser#boolFalse.
    def exitBoolFalse(self, ctx:LangParser.BoolFalseContext):
        pass


    # Enter a parse tree produced by LangParser#assignment.
    def enterAssignment(self, ctx:LangParser.AssignmentContext):
        pass

    # Exit a parse tree produced by LangParser#assignment.
    def exitAssignment(self, ctx:LangParser.AssignmentContext):
        pass


    # Enter a parse tree produced by LangParser#logicOr.
    def enterLogicOr(self, ctx:LangParser.LogicOrContext):
        pass

    # Exit a parse tree produced by LangParser#logicOr.
    def exitLogicOr(self, ctx:LangParser.LogicOrContext):
        pass


    # Enter a parse tree produced by LangParser#addSub.
    def enterAddSub(self, ctx:LangParser.AddSubContext):
        pass

    # Exit a parse tree produced by LangParser#addSub.
    def exitAddSub(self, ctx:LangParser.AddSubContext):
        pass


    # Enter a parse tree produced by LangParser#concat.
    def enterConcat(self, ctx:LangParser.ConcatContext):
        pass

    # Exit a parse tree produced by LangParser#concat.
    def exitConcat(self, ctx:LangParser.ConcatContext):
        pass


    # Enter a parse tree produced by LangParser#float.
    def enterFloat(self, ctx:LangParser.FloatContext):
        pass

    # Exit a parse tree produced by LangParser#float.
    def exitFloat(self, ctx:LangParser.FloatContext):
        pass


    # Enter a parse tree produced by LangParser#int.
    def enterInt(self, ctx:LangParser.IntContext):
        pass

    # Exit a parse tree produced by LangParser#int.
    def exitInt(self, ctx:LangParser.IntContext):
        pass


    # Enter a parse tree produced by LangParser#mulDiv.
    def enterMulDiv(self, ctx:LangParser.MulDivContext):
        pass

    # Exit a parse tree produced by LangParser#mulDiv.
    def exitMulDiv(self, ctx:LangParser.MulDivContext):
        pass


    # Enter a parse tree produced by LangParser#not.
    def enterNot(self, ctx:LangParser.NotContext):
        pass

    # Exit a parse tree produced by LangParser#not.
    def exitNot(self, ctx:LangParser.NotContext):
        pass


    # Enter a parse tree produced by LangParser#boolTrue.
    def enterBoolTrue(self, ctx:LangParser.BoolTrueContext):
        pass

    # Exit a parse tree produced by LangParser#boolTrue.
    def exitBoolTrue(self, ctx:LangParser.BoolTrueContext):
        pass


    # Enter a parse tree produced by LangParser#logicAnd.
    def enterLogicAnd(self, ctx:LangParser.LogicAndContext):
        pass

    # Exit a parse tree produced by LangParser#logicAnd.
    def exitLogicAnd(self, ctx:LangParser.LogicAndContext):
        pass


    # Enter a parse tree produced by LangParser#unaryMinus.
    def enterUnaryMinus(self, ctx:LangParser.UnaryMinusContext):
        pass

    # Exit a parse tree produced by LangParser#unaryMinus.
    def exitUnaryMinus(self, ctx:LangParser.UnaryMinusContext):
        pass


    # Enter a parse tree produced by LangParser#relational.
    def enterRelational(self, ctx:LangParser.RelationalContext):
        pass

    # Exit a parse tree produced by LangParser#relational.
    def exitRelational(self, ctx:LangParser.RelationalContext):
        pass


    # Enter a parse tree produced by LangParser#id.
    def enterId(self, ctx:LangParser.IdContext):
        pass

    # Exit a parse tree produced by LangParser#id.
    def exitId(self, ctx:LangParser.IdContext):
        pass


    # Enter a parse tree produced by LangParser#modulo.
    def enterModulo(self, ctx:LangParser.ModuloContext):
        pass

    # Exit a parse tree produced by LangParser#modulo.
    def exitModulo(self, ctx:LangParser.ModuloContext):
        pass


    # Enter a parse tree produced by LangParser#ternary.
    def enterTernary(self, ctx:LangParser.TernaryContext):
        pass

    # Exit a parse tree produced by LangParser#ternary.
    def exitTernary(self, ctx:LangParser.TernaryContext):
        pass


    # Enter a parse tree produced by LangParser#condition.
    def enterCondition(self, ctx:LangParser.ConditionContext):
        pass

    # Exit a parse tree produced by LangParser#condition.
    def exitCondition(self, ctx:LangParser.ConditionContext):
        pass


    # Enter a parse tree produced by LangParser#primitiveType.
    def enterPrimitiveType(self, ctx:LangParser.PrimitiveTypeContext):
        pass

    # Exit a parse tree produced by LangParser#primitiveType.
    def exitPrimitiveType(self, ctx:LangParser.PrimitiveTypeContext):
        pass



del LangParser