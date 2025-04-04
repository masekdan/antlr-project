# Generated from Lang.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,36,125,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,1,0,4,0,12,8,
        0,11,0,12,0,13,1,1,1,1,1,1,1,1,5,1,20,8,1,10,1,12,1,23,9,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,5,1,34,8,1,10,1,12,1,37,9,1,1,1,1,
        1,1,1,1,1,1,1,5,1,44,8,1,10,1,12,1,47,9,1,1,1,1,1,1,1,1,1,4,1,53,
        8,1,11,1,12,1,54,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,64,8,1,1,1,1,1,
        1,1,1,1,3,1,70,8,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,
        2,1,2,1,2,1,2,1,2,1,2,3,2,89,8,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,
        1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,5,2,112,8,2,
        10,2,12,2,115,9,2,1,3,1,3,1,4,1,4,1,4,1,4,3,4,123,8,4,1,4,0,1,4,
        5,0,2,4,6,8,0,5,1,0,19,20,1,0,21,22,1,0,24,25,1,0,26,27,1,0,28,29,
        149,0,11,1,0,0,0,2,69,1,0,0,0,4,88,1,0,0,0,6,116,1,0,0,0,8,122,1,
        0,0,0,10,12,3,2,1,0,11,10,1,0,0,0,12,13,1,0,0,0,13,11,1,0,0,0,13,
        14,1,0,0,0,14,1,1,0,0,0,15,16,3,8,4,0,16,21,5,30,0,0,17,18,5,18,
        0,0,18,20,5,30,0,0,19,17,1,0,0,0,20,23,1,0,0,0,21,19,1,0,0,0,21,
        22,1,0,0,0,22,24,1,0,0,0,23,21,1,0,0,0,24,25,5,17,0,0,25,70,1,0,
        0,0,26,27,3,4,2,0,27,28,5,17,0,0,28,70,1,0,0,0,29,30,5,12,0,0,30,
        35,5,30,0,0,31,32,5,18,0,0,32,34,5,30,0,0,33,31,1,0,0,0,34,37,1,
        0,0,0,35,33,1,0,0,0,35,36,1,0,0,0,36,38,1,0,0,0,37,35,1,0,0,0,38,
        70,5,17,0,0,39,40,5,13,0,0,40,45,3,4,2,0,41,42,5,18,0,0,42,44,3,
        4,2,0,43,41,1,0,0,0,44,47,1,0,0,0,45,43,1,0,0,0,45,46,1,0,0,0,46,
        48,1,0,0,0,47,45,1,0,0,0,48,49,5,17,0,0,49,70,1,0,0,0,50,52,5,1,
        0,0,51,53,3,2,1,0,52,51,1,0,0,0,53,54,1,0,0,0,54,52,1,0,0,0,54,55,
        1,0,0,0,55,56,1,0,0,0,56,57,5,2,0,0,57,70,1,0,0,0,58,59,5,14,0,0,
        59,60,3,6,3,0,60,63,3,2,1,0,61,62,5,15,0,0,62,64,3,2,1,0,63,61,1,
        0,0,0,63,64,1,0,0,0,64,70,1,0,0,0,65,66,5,16,0,0,66,67,3,6,3,0,67,
        68,3,2,1,0,68,70,1,0,0,0,69,15,1,0,0,0,69,26,1,0,0,0,69,29,1,0,0,
        0,69,39,1,0,0,0,69,50,1,0,0,0,69,58,1,0,0,0,69,65,1,0,0,0,70,3,1,
        0,0,0,71,72,6,2,-1,0,72,73,5,22,0,0,73,89,3,4,2,13,74,75,5,3,0,0,
        75,89,3,4,2,12,76,89,5,30,0,0,77,89,5,32,0,0,78,89,5,31,0,0,79,89,
        5,33,0,0,80,89,5,34,0,0,81,82,5,5,0,0,82,83,3,4,2,0,83,84,5,6,0,
        0,84,89,1,0,0,0,85,86,5,30,0,0,86,87,5,7,0,0,87,89,3,4,2,1,88,71,
        1,0,0,0,88,74,1,0,0,0,88,76,1,0,0,0,88,77,1,0,0,0,88,78,1,0,0,0,
        88,79,1,0,0,0,88,80,1,0,0,0,88,81,1,0,0,0,88,85,1,0,0,0,89,113,1,
        0,0,0,90,91,10,16,0,0,91,92,7,0,0,0,92,112,3,4,2,17,93,94,10,15,
        0,0,94,95,7,1,0,0,95,112,3,4,2,16,96,97,10,14,0,0,97,98,5,23,0,0,
        98,112,3,4,2,15,99,100,10,11,0,0,100,101,5,4,0,0,101,112,3,4,2,12,
        102,103,10,10,0,0,103,104,7,2,0,0,104,112,3,4,2,11,105,106,10,9,
        0,0,106,107,7,3,0,0,107,112,3,4,2,10,108,109,10,8,0,0,109,110,7,
        4,0,0,110,112,3,4,2,9,111,90,1,0,0,0,111,93,1,0,0,0,111,96,1,0,0,
        0,111,99,1,0,0,0,111,102,1,0,0,0,111,105,1,0,0,0,111,108,1,0,0,0,
        112,115,1,0,0,0,113,111,1,0,0,0,113,114,1,0,0,0,114,5,1,0,0,0,115,
        113,1,0,0,0,116,117,3,4,2,0,117,7,1,0,0,0,118,123,5,8,0,0,119,123,
        5,9,0,0,120,123,5,10,0,0,121,123,5,11,0,0,122,118,1,0,0,0,122,119,
        1,0,0,0,122,120,1,0,0,0,122,121,1,0,0,0,123,9,1,0,0,0,11,13,21,35,
        45,54,63,69,88,111,113,122
    ]

class LangParser ( Parser ):

    grammarFileName = "Lang.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'{'", "'}'", "'!'", "'.'", "'('", "')'", 
                     "'='", "'int'", "'float'", "'bool'", "'string'", "'read'", 
                     "'write'", "'if'", "'else'", "'while'", "';'", "','", 
                     "'*'", "'/'", "'+'", "'-'", "'%'", "'>'", "'<'", "'=='", 
                     "'!='", "'&&'", "'||'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "INT_KEYWORD", "FLOAT_KEYWORD", "BOOL_KEYWORD", "STRING_KEYWORD", 
                      "READ_KEYWORD", "WRITE_KEYWORD", "IF_KEYWORD", "ELSE_KEYWORD", 
                      "WHILE_KEYWORD", "SEMI", "COMMA", "MUL", "DIV", "ADD", 
                      "SUB", "MOD", "GT", "LT", "EQ", "NEQ", "AND", "OR", 
                      "IDENTIFIER", "FLOAT", "INT", "BOOL", "STRING", "WS", 
                      "COMMENT" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_expr = 2
    RULE_condition = 3
    RULE_primitiveType = 4

    ruleNames =  [ "program", "statement", "expr", "condition", "primitiveType" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    INT_KEYWORD=8
    FLOAT_KEYWORD=9
    BOOL_KEYWORD=10
    STRING_KEYWORD=11
    READ_KEYWORD=12
    WRITE_KEYWORD=13
    IF_KEYWORD=14
    ELSE_KEYWORD=15
    WHILE_KEYWORD=16
    SEMI=17
    COMMA=18
    MUL=19
    DIV=20
    ADD=21
    SUB=22
    MOD=23
    GT=24
    LT=25
    EQ=26
    NEQ=27
    AND=28
    OR=29
    IDENTIFIER=30
    FLOAT=31
    INT=32
    BOOL=33
    STRING=34
    WS=35
    COMMENT=36

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LangParser.StatementContext)
            else:
                return self.getTypedRuleContext(LangParser.StatementContext,i)


        def getRuleIndex(self):
            return LangParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = LangParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 11 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 10
                self.statement()
                self.state = 13 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 33290288938) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return LangParser.RULE_statement

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ReadExpContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LangParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def READ_KEYWORD(self):
            return self.getToken(LangParser.READ_KEYWORD, 0)
        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(LangParser.IDENTIFIER)
            else:
                return self.getToken(LangParser.IDENTIFIER, i)
        def SEMI(self):
            return self.getToken(LangParser.SEMI, 0)
        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(LangParser.COMMA)
            else:
                return self.getToken(LangParser.COMMA, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReadExp" ):
                listener.enterReadExp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReadExp" ):
                listener.exitReadExp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReadExp" ):
                return visitor.visitReadExp(self)
            else:
                return visitor.visitChildren(self)


    class BlockExpContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LangParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LangParser.StatementContext)
            else:
                return self.getTypedRuleContext(LangParser.StatementContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlockExp" ):
                listener.enterBlockExp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlockExp" ):
                listener.exitBlockExp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlockExp" ):
                return visitor.visitBlockExp(self)
            else:
                return visitor.visitChildren(self)


    class WhileLoopContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LangParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def WHILE_KEYWORD(self):
            return self.getToken(LangParser.WHILE_KEYWORD, 0)
        def statement(self):
            return self.getTypedRuleContext(LangParser.StatementContext,0)

        def condition(self):
            return self.getTypedRuleContext(LangParser.ConditionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhileLoop" ):
                listener.enterWhileLoop(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhileLoop" ):
                listener.exitWhileLoop(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhileLoop" ):
                return visitor.visitWhileLoop(self)
            else:
                return visitor.visitChildren(self)


    class DeclarationContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LangParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def primitiveType(self):
            return self.getTypedRuleContext(LangParser.PrimitiveTypeContext,0)

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(LangParser.IDENTIFIER)
            else:
                return self.getToken(LangParser.IDENTIFIER, i)
        def SEMI(self):
            return self.getToken(LangParser.SEMI, 0)
        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(LangParser.COMMA)
            else:
                return self.getToken(LangParser.COMMA, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaration" ):
                listener.enterDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaration" ):
                listener.exitDeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaration" ):
                return visitor.visitDeclaration(self)
            else:
                return visitor.visitChildren(self)


    class IfElseContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LangParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def IF_KEYWORD(self):
            return self.getToken(LangParser.IF_KEYWORD, 0)
        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LangParser.StatementContext)
            else:
                return self.getTypedRuleContext(LangParser.StatementContext,i)

        def condition(self):
            return self.getTypedRuleContext(LangParser.ConditionContext,0)

        def ELSE_KEYWORD(self):
            return self.getToken(LangParser.ELSE_KEYWORD, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfElse" ):
                listener.enterIfElse(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfElse" ):
                listener.exitIfElse(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfElse" ):
                return visitor.visitIfElse(self)
            else:
                return visitor.visitChildren(self)


    class WriteExpContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LangParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def WRITE_KEYWORD(self):
            return self.getToken(LangParser.WRITE_KEYWORD, 0)
        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LangParser.ExprContext)
            else:
                return self.getTypedRuleContext(LangParser.ExprContext,i)

        def SEMI(self):
            return self.getToken(LangParser.SEMI, 0)
        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(LangParser.COMMA)
            else:
                return self.getToken(LangParser.COMMA, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWriteExp" ):
                listener.enterWriteExp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWriteExp" ):
                listener.exitWriteExp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWriteExp" ):
                return visitor.visitWriteExp(self)
            else:
                return visitor.visitChildren(self)


    class PrintExprContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LangParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(LangParser.ExprContext,0)

        def SEMI(self):
            return self.getToken(LangParser.SEMI, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrintExpr" ):
                listener.enterPrintExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrintExpr" ):
                listener.exitPrintExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrintExpr" ):
                return visitor.visitPrintExpr(self)
            else:
                return visitor.visitChildren(self)



    def statement(self):

        localctx = LangParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        self._la = 0 # Token type
        try:
            self.state = 69
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [8, 9, 10, 11]:
                localctx = LangParser.DeclarationContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 15
                self.primitiveType()
                self.state = 16
                self.match(LangParser.IDENTIFIER)
                self.state = 21
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==18:
                    self.state = 17
                    self.match(LangParser.COMMA)
                    self.state = 18
                    self.match(LangParser.IDENTIFIER)
                    self.state = 23
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 24
                self.match(LangParser.SEMI)
                pass
            elif token in [3, 5, 22, 30, 31, 32, 33, 34]:
                localctx = LangParser.PrintExprContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 26
                self.expr(0)
                self.state = 27
                self.match(LangParser.SEMI)
                pass
            elif token in [12]:
                localctx = LangParser.ReadExpContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 29
                self.match(LangParser.READ_KEYWORD)
                self.state = 30
                self.match(LangParser.IDENTIFIER)
                self.state = 35
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==18:
                    self.state = 31
                    self.match(LangParser.COMMA)
                    self.state = 32
                    self.match(LangParser.IDENTIFIER)
                    self.state = 37
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 38
                self.match(LangParser.SEMI)
                pass
            elif token in [13]:
                localctx = LangParser.WriteExpContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 39
                self.match(LangParser.WRITE_KEYWORD)
                self.state = 40
                self.expr(0)
                self.state = 45
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==18:
                    self.state = 41
                    self.match(LangParser.COMMA)
                    self.state = 42
                    self.expr(0)
                    self.state = 47
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 48
                self.match(LangParser.SEMI)
                pass
            elif token in [1]:
                localctx = LangParser.BlockExpContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 50
                self.match(LangParser.T__0)
                self.state = 52 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 51
                    self.statement()
                    self.state = 54 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 33290288938) != 0)):
                        break

                self.state = 56
                self.match(LangParser.T__1)
                pass
            elif token in [14]:
                localctx = LangParser.IfElseContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 58
                self.match(LangParser.IF_KEYWORD)

                self.state = 59
                self.condition()
                self.state = 60
                self.statement()
                self.state = 63
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
                if la_ == 1:
                    self.state = 61
                    self.match(LangParser.ELSE_KEYWORD)
                    self.state = 62
                    self.statement()


                pass
            elif token in [16]:
                localctx = LangParser.WhileLoopContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 65
                self.match(LangParser.WHILE_KEYWORD)

                self.state = 66
                self.condition()
                self.state = 67
                self.statement()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return LangParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class ParensContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(LangParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParens" ):
                listener.enterParens(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParens" ):
                listener.exitParens(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParens" ):
                return visitor.visitParens(self)
            else:
                return visitor.visitChildren(self)


    class CompareContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LangParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LangParser.ExprContext)
            else:
                return self.getTypedRuleContext(LangParser.ExprContext,i)

        def EQ(self):
            return self.getToken(LangParser.EQ, 0)
        def NEQ(self):
            return self.getToken(LangParser.NEQ, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCompare" ):
                listener.enterCompare(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCompare" ):
                listener.exitCompare(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCompare" ):
                return visitor.visitCompare(self)
            else:
                return visitor.visitChildren(self)


    class BoolContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def BOOL(self):
            return self.getToken(LangParser.BOOL, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBool" ):
                listener.enterBool(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBool" ):
                listener.exitBool(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBool" ):
                return visitor.visitBool(self)
            else:
                return visitor.visitChildren(self)


    class StringContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def STRING(self):
            return self.getToken(LangParser.STRING, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterString" ):
                listener.enterString(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitString" ):
                listener.exitString(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitString" ):
                return visitor.visitString(self)
            else:
                return visitor.visitChildren(self)


    class AssignmentContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def IDENTIFIER(self):
            return self.getToken(LangParser.IDENTIFIER, 0)
        def expr(self):
            return self.getTypedRuleContext(LangParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment" ):
                listener.enterAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment" ):
                listener.exitAssignment(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment" ):
                return visitor.visitAssignment(self)
            else:
                return visitor.visitChildren(self)


    class AddSubContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LangParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LangParser.ExprContext)
            else:
                return self.getTypedRuleContext(LangParser.ExprContext,i)

        def ADD(self):
            return self.getToken(LangParser.ADD, 0)
        def SUB(self):
            return self.getToken(LangParser.SUB, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAddSub" ):
                listener.enterAddSub(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAddSub" ):
                listener.exitAddSub(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAddSub" ):
                return visitor.visitAddSub(self)
            else:
                return visitor.visitChildren(self)


    class ConcatContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LangParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LangParser.ExprContext)
            else:
                return self.getTypedRuleContext(LangParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConcat" ):
                listener.enterConcat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConcat" ):
                listener.exitConcat(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConcat" ):
                return visitor.visitConcat(self)
            else:
                return visitor.visitChildren(self)


    class FloatContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def FLOAT(self):
            return self.getToken(LangParser.FLOAT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFloat" ):
                listener.enterFloat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFloat" ):
                listener.exitFloat(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFloat" ):
                return visitor.visitFloat(self)
            else:
                return visitor.visitChildren(self)


    class IntContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INT(self):
            return self.getToken(LangParser.INT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInt" ):
                listener.enterInt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInt" ):
                listener.exitInt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInt" ):
                return visitor.visitInt(self)
            else:
                return visitor.visitChildren(self)


    class MulDivContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LangParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LangParser.ExprContext)
            else:
                return self.getTypedRuleContext(LangParser.ExprContext,i)

        def MUL(self):
            return self.getToken(LangParser.MUL, 0)
        def DIV(self):
            return self.getToken(LangParser.DIV, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMulDiv" ):
                listener.enterMulDiv(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMulDiv" ):
                listener.exitMulDiv(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMulDiv" ):
                return visitor.visitMulDiv(self)
            else:
                return visitor.visitChildren(self)


    class NotContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LangParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(LangParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNot" ):
                listener.enterNot(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNot" ):
                listener.exitNot(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNot" ):
                return visitor.visitNot(self)
            else:
                return visitor.visitChildren(self)


    class UnaryMinusContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LangParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(LangParser.ExprContext,0)

        def SUB(self):
            return self.getToken(LangParser.SUB, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnaryMinus" ):
                listener.enterUnaryMinus(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnaryMinus" ):
                listener.exitUnaryMinus(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnaryMinus" ):
                return visitor.visitUnaryMinus(self)
            else:
                return visitor.visitChildren(self)


    class RelationalContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LangParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LangParser.ExprContext)
            else:
                return self.getTypedRuleContext(LangParser.ExprContext,i)

        def GT(self):
            return self.getToken(LangParser.GT, 0)
        def LT(self):
            return self.getToken(LangParser.LT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRelational" ):
                listener.enterRelational(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRelational" ):
                listener.exitRelational(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRelational" ):
                return visitor.visitRelational(self)
            else:
                return visitor.visitChildren(self)


    class IdContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def IDENTIFIER(self):
            return self.getToken(LangParser.IDENTIFIER, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterId" ):
                listener.enterId(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitId" ):
                listener.exitId(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitId" ):
                return visitor.visitId(self)
            else:
                return visitor.visitChildren(self)


    class LogicContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LangParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LangParser.ExprContext)
            else:
                return self.getTypedRuleContext(LangParser.ExprContext,i)

        def AND(self):
            return self.getToken(LangParser.AND, 0)
        def OR(self):
            return self.getToken(LangParser.OR, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogic" ):
                listener.enterLogic(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogic" ):
                listener.exitLogic(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogic" ):
                return visitor.visitLogic(self)
            else:
                return visitor.visitChildren(self)


    class ModuloContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LangParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LangParser.ExprContext)
            else:
                return self.getTypedRuleContext(LangParser.ExprContext,i)

        def MOD(self):
            return self.getToken(LangParser.MOD, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterModulo" ):
                listener.enterModulo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitModulo" ):
                listener.exitModulo(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitModulo" ):
                return visitor.visitModulo(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = LangParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 4
        self.enterRecursionRule(localctx, 4, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 88
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                localctx = LangParser.UnaryMinusContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 72
                localctx.op = self.match(LangParser.SUB)
                self.state = 73
                self.expr(13)
                pass

            elif la_ == 2:
                localctx = LangParser.NotContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 74
                localctx.op = self.match(LangParser.T__2)
                self.state = 75
                self.expr(12)
                pass

            elif la_ == 3:
                localctx = LangParser.IdContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 76
                self.match(LangParser.IDENTIFIER)
                pass

            elif la_ == 4:
                localctx = LangParser.IntContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 77
                self.match(LangParser.INT)
                pass

            elif la_ == 5:
                localctx = LangParser.FloatContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 78
                self.match(LangParser.FLOAT)
                pass

            elif la_ == 6:
                localctx = LangParser.BoolContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 79
                self.match(LangParser.BOOL)
                pass

            elif la_ == 7:
                localctx = LangParser.StringContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 80
                self.match(LangParser.STRING)
                pass

            elif la_ == 8:
                localctx = LangParser.ParensContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 81
                self.match(LangParser.T__4)
                self.state = 82
                self.expr(0)
                self.state = 83
                self.match(LangParser.T__5)
                pass

            elif la_ == 9:
                localctx = LangParser.AssignmentContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 85
                self.match(LangParser.IDENTIFIER)
                self.state = 86
                self.match(LangParser.T__6)
                self.state = 87
                self.expr(1)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 113
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,9,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 111
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
                    if la_ == 1:
                        localctx = LangParser.MulDivContext(self, LangParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 90
                        if not self.precpred(self._ctx, 16):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 16)")
                        self.state = 91
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==19 or _la==20):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 92
                        self.expr(17)
                        pass

                    elif la_ == 2:
                        localctx = LangParser.AddSubContext(self, LangParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 93
                        if not self.precpred(self._ctx, 15):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 15)")
                        self.state = 94
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==21 or _la==22):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 95
                        self.expr(16)
                        pass

                    elif la_ == 3:
                        localctx = LangParser.ModuloContext(self, LangParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 96
                        if not self.precpred(self._ctx, 14):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 14)")
                        self.state = 97
                        localctx.op = self.match(LangParser.MOD)
                        self.state = 98
                        self.expr(15)
                        pass

                    elif la_ == 4:
                        localctx = LangParser.ConcatContext(self, LangParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 99
                        if not self.precpred(self._ctx, 11):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 100
                        localctx.op = self.match(LangParser.T__3)
                        self.state = 101
                        self.expr(12)
                        pass

                    elif la_ == 5:
                        localctx = LangParser.RelationalContext(self, LangParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 102
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 103
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==24 or _la==25):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 104
                        self.expr(11)
                        pass

                    elif la_ == 6:
                        localctx = LangParser.CompareContext(self, LangParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 105
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 106
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==26 or _la==27):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 107
                        self.expr(10)
                        pass

                    elif la_ == 7:
                        localctx = LangParser.LogicContext(self, LangParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 108
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 109
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==28 or _la==29):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 110
                        self.expr(9)
                        pass

             
                self.state = 115
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,9,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class ConditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(LangParser.ExprContext,0)


        def getRuleIndex(self):
            return LangParser.RULE_condition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondition" ):
                listener.enterCondition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondition" ):
                listener.exitCondition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCondition" ):
                return visitor.visitCondition(self)
            else:
                return visitor.visitChildren(self)




    def condition(self):

        localctx = LangParser.ConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_condition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 116
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrimitiveTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.type_ = None # Token

        def INT_KEYWORD(self):
            return self.getToken(LangParser.INT_KEYWORD, 0)

        def FLOAT_KEYWORD(self):
            return self.getToken(LangParser.FLOAT_KEYWORD, 0)

        def BOOL_KEYWORD(self):
            return self.getToken(LangParser.BOOL_KEYWORD, 0)

        def STRING_KEYWORD(self):
            return self.getToken(LangParser.STRING_KEYWORD, 0)

        def getRuleIndex(self):
            return LangParser.RULE_primitiveType

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrimitiveType" ):
                listener.enterPrimitiveType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrimitiveType" ):
                listener.exitPrimitiveType(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimitiveType" ):
                return visitor.visitPrimitiveType(self)
            else:
                return visitor.visitChildren(self)




    def primitiveType(self):

        localctx = LangParser.PrimitiveTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_primitiveType)
        try:
            self.state = 122
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [8]:
                self.enterOuterAlt(localctx, 1)
                self.state = 118
                localctx.type_ = self.match(LangParser.INT_KEYWORD)
                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 2)
                self.state = 119
                localctx.type_ = self.match(LangParser.FLOAT_KEYWORD)
                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 3)
                self.state = 120
                localctx.type_ = self.match(LangParser.BOOL_KEYWORD)
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 4)
                self.state = 121
                localctx.type_ = self.match(LangParser.STRING_KEYWORD)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[2] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 16)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 15)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 14)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 11)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 10)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 9)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 8)
         




