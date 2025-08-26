# Generated from message_parser.g4 by ANTLR 4.13.2
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
        4,1,17,129,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,1,0,1,0,1,0,1,1,1,1,1,1,
        5,1,43,8,1,10,1,12,1,46,9,1,1,2,1,2,1,2,1,2,1,3,1,3,1,3,3,3,55,8,
        3,1,3,1,3,1,4,1,4,4,4,61,8,4,11,4,12,4,62,1,5,1,5,3,5,67,8,5,1,6,
        1,6,1,6,1,6,1,6,1,7,1,7,1,7,3,7,77,8,7,1,7,5,7,80,8,7,10,7,12,7,
        83,9,7,1,7,1,7,1,8,4,8,88,8,8,11,8,12,8,89,1,9,1,9,3,9,94,8,9,1,
        10,1,10,1,10,1,11,1,11,1,11,1,12,1,12,3,12,104,8,12,1,13,4,13,107,
        8,13,11,13,12,13,108,1,14,1,14,3,14,113,8,14,1,15,1,15,1,15,1,15,
        1,15,1,16,4,16,121,8,16,11,16,12,16,122,1,17,1,17,3,17,127,8,17,
        1,17,0,0,18,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,0,0,
        125,0,36,1,0,0,0,2,44,1,0,0,0,4,47,1,0,0,0,6,51,1,0,0,0,8,58,1,0,
        0,0,10,66,1,0,0,0,12,68,1,0,0,0,14,73,1,0,0,0,16,87,1,0,0,0,18,93,
        1,0,0,0,20,95,1,0,0,0,22,98,1,0,0,0,24,103,1,0,0,0,26,106,1,0,0,
        0,28,112,1,0,0,0,30,114,1,0,0,0,32,120,1,0,0,0,34,126,1,0,0,0,36,
        37,3,2,1,0,37,38,5,0,0,1,38,1,1,0,0,0,39,43,5,1,0,0,40,43,3,4,2,
        0,41,43,3,14,7,0,42,39,1,0,0,0,42,40,1,0,0,0,42,41,1,0,0,0,43,46,
        1,0,0,0,44,42,1,0,0,0,44,45,1,0,0,0,45,3,1,0,0,0,46,44,1,0,0,0,47,
        48,3,6,3,0,48,49,3,2,1,0,49,50,3,12,6,0,50,5,1,0,0,0,51,52,5,2,0,
        0,52,54,5,4,0,0,53,55,3,8,4,0,54,53,1,0,0,0,54,55,1,0,0,0,55,56,
        1,0,0,0,56,57,5,7,0,0,57,7,1,0,0,0,58,60,5,6,0,0,59,61,3,10,5,0,
        60,59,1,0,0,0,61,62,1,0,0,0,62,60,1,0,0,0,62,63,1,0,0,0,63,9,1,0,
        0,0,64,67,5,8,0,0,65,67,3,14,7,0,66,64,1,0,0,0,66,65,1,0,0,0,67,
        11,1,0,0,0,68,69,5,2,0,0,69,70,5,5,0,0,70,71,5,4,0,0,71,72,5,7,0,
        0,72,13,1,0,0,0,73,74,5,3,0,0,74,76,3,16,8,0,75,77,3,20,10,0,76,
        75,1,0,0,0,76,77,1,0,0,0,77,81,1,0,0,0,78,80,3,22,11,0,79,78,1,0,
        0,0,80,83,1,0,0,0,81,79,1,0,0,0,81,82,1,0,0,0,82,84,1,0,0,0,83,81,
        1,0,0,0,84,85,5,12,0,0,85,15,1,0,0,0,86,88,3,18,9,0,87,86,1,0,0,
        0,88,89,1,0,0,0,89,87,1,0,0,0,89,90,1,0,0,0,90,17,1,0,0,0,91,94,
        5,9,0,0,92,94,3,14,7,0,93,91,1,0,0,0,93,92,1,0,0,0,94,19,1,0,0,0,
        95,96,5,10,0,0,96,97,5,13,0,0,97,21,1,0,0,0,98,99,5,11,0,0,99,100,
        3,24,12,0,100,23,1,0,0,0,101,104,3,30,15,0,102,104,3,26,13,0,103,
        101,1,0,0,0,103,102,1,0,0,0,104,25,1,0,0,0,105,107,3,28,14,0,106,
        105,1,0,0,0,107,108,1,0,0,0,108,106,1,0,0,0,108,109,1,0,0,0,109,
        27,1,0,0,0,110,113,5,14,0,0,111,113,3,14,7,0,112,110,1,0,0,0,112,
        111,1,0,0,0,113,29,1,0,0,0,114,115,5,14,0,0,115,116,5,15,0,0,116,
        117,3,32,16,0,117,118,5,17,0,0,118,31,1,0,0,0,119,121,3,34,17,0,
        120,119,1,0,0,0,121,122,1,0,0,0,122,120,1,0,0,0,122,123,1,0,0,0,
        123,33,1,0,0,0,124,127,5,16,0,0,125,127,3,14,7,0,126,124,1,0,0,0,
        126,125,1,0,0,0,127,35,1,0,0,0,14,42,44,54,62,66,76,81,89,93,103,
        108,112,122,126
    ]

class message_parser ( Parser ):

    grammarFileName = "message_parser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "'['", "'{'", "<INVALID>", 
                     "'/'", "'='", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'!'", "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'('", "<INVALID>", "')'" ]

    symbolicNames = [ "<INVALID>", "TEXT", "OPEN_TAG", "OPEN_SUB", "TAG_NAME", 
                      "TAG_SLASH", "TAG_SEP", "CLOSE_TAG", "TAG_PARAM", 
                      "SUB_FIELD", "SUB_CONVERT", "SUB_SPEC", "CLOSE_SUB", 
                      "SUB_IDENTIFIER", "SPEC_VALUE", "OPEN_ARGLIST", "ARGLIST_VALUE", 
                      "CLOSE_ARGLIST" ]

    RULE_main = 0
    RULE_string = 1
    RULE_tag = 2
    RULE_open_tag = 3
    RULE_tag_param = 4
    RULE_tag_param_frag = 5
    RULE_close_tag = 6
    RULE_sub = 7
    RULE_sub_field = 8
    RULE_sub_field_frag = 9
    RULE_sub_convert = 10
    RULE_sub_spec = 11
    RULE_spec_value = 12
    RULE_spec_literal = 13
    RULE_spec_literal_frag = 14
    RULE_spec_func = 15
    RULE_spec_func_arg = 16
    RULE_spec_func_arg_frag = 17

    ruleNames =  [ "main", "string", "tag", "open_tag", "tag_param", "tag_param_frag", 
                   "close_tag", "sub", "sub_field", "sub_field_frag", "sub_convert", 
                   "sub_spec", "spec_value", "spec_literal", "spec_literal_frag", 
                   "spec_func", "spec_func_arg", "spec_func_arg_frag" ]

    EOF = Token.EOF
    TEXT=1
    OPEN_TAG=2
    OPEN_SUB=3
    TAG_NAME=4
    TAG_SLASH=5
    TAG_SEP=6
    CLOSE_TAG=7
    TAG_PARAM=8
    SUB_FIELD=9
    SUB_CONVERT=10
    SUB_SPEC=11
    CLOSE_SUB=12
    SUB_IDENTIFIER=13
    SPEC_VALUE=14
    OPEN_ARGLIST=15
    ARGLIST_VALUE=16
    CLOSE_ARGLIST=17

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class MainContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def string(self):
            return self.getTypedRuleContext(message_parser.StringContext,0)


        def EOF(self):
            return self.getToken(message_parser.EOF, 0)

        def getRuleIndex(self):
            return message_parser.RULE_main

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMain" ):
                listener.enterMain(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMain" ):
                listener.exitMain(self)




    def main(self):

        localctx = message_parser.MainContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_main)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 36
            self.string()
            self.state = 37
            self.match(message_parser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StringContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TEXT(self, i:int=None):
            if i is None:
                return self.getTokens(message_parser.TEXT)
            else:
                return self.getToken(message_parser.TEXT, i)

        def tag(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(message_parser.TagContext)
            else:
                return self.getTypedRuleContext(message_parser.TagContext,i)


        def sub(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(message_parser.SubContext)
            else:
                return self.getTypedRuleContext(message_parser.SubContext,i)


        def getRuleIndex(self):
            return message_parser.RULE_string

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterString" ):
                listener.enterString(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitString" ):
                listener.exitString(self)




    def string(self):

        localctx = message_parser.StringContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_string)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 44
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,1,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 42
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [1]:
                        self.state = 39
                        self.match(message_parser.TEXT)
                        pass
                    elif token in [2]:
                        self.state = 40
                        self.tag()
                        pass
                    elif token in [3]:
                        self.state = 41
                        self.sub()
                        pass
                    else:
                        raise NoViableAltException(self)
             
                self.state = 46
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TagContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def open_tag(self):
            return self.getTypedRuleContext(message_parser.Open_tagContext,0)


        def string(self):
            return self.getTypedRuleContext(message_parser.StringContext,0)


        def close_tag(self):
            return self.getTypedRuleContext(message_parser.Close_tagContext,0)


        def getRuleIndex(self):
            return message_parser.RULE_tag

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTag" ):
                listener.enterTag(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTag" ):
                listener.exitTag(self)




    def tag(self):

        localctx = message_parser.TagContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_tag)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 47
            self.open_tag()
            self.state = 48
            self.string()
            self.state = 49
            self.close_tag()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Open_tagContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPEN_TAG(self):
            return self.getToken(message_parser.OPEN_TAG, 0)

        def TAG_NAME(self):
            return self.getToken(message_parser.TAG_NAME, 0)

        def CLOSE_TAG(self):
            return self.getToken(message_parser.CLOSE_TAG, 0)

        def tag_param(self):
            return self.getTypedRuleContext(message_parser.Tag_paramContext,0)


        def getRuleIndex(self):
            return message_parser.RULE_open_tag

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOpen_tag" ):
                listener.enterOpen_tag(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOpen_tag" ):
                listener.exitOpen_tag(self)




    def open_tag(self):

        localctx = message_parser.Open_tagContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_open_tag)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 51
            self.match(message_parser.OPEN_TAG)
            self.state = 52
            self.match(message_parser.TAG_NAME)
            self.state = 54
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==6:
                self.state = 53
                self.tag_param()


            self.state = 56
            self.match(message_parser.CLOSE_TAG)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Tag_paramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TAG_SEP(self):
            return self.getToken(message_parser.TAG_SEP, 0)

        def tag_param_frag(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(message_parser.Tag_param_fragContext)
            else:
                return self.getTypedRuleContext(message_parser.Tag_param_fragContext,i)


        def getRuleIndex(self):
            return message_parser.RULE_tag_param

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTag_param" ):
                listener.enterTag_param(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTag_param" ):
                listener.exitTag_param(self)




    def tag_param(self):

        localctx = message_parser.Tag_paramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_tag_param)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 58
            self.match(message_parser.TAG_SEP)
            self.state = 60 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 59
                self.tag_param_frag()
                self.state = 62 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==3 or _la==8):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Tag_param_fragContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TAG_PARAM(self):
            return self.getToken(message_parser.TAG_PARAM, 0)

        def sub(self):
            return self.getTypedRuleContext(message_parser.SubContext,0)


        def getRuleIndex(self):
            return message_parser.RULE_tag_param_frag

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTag_param_frag" ):
                listener.enterTag_param_frag(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTag_param_frag" ):
                listener.exitTag_param_frag(self)




    def tag_param_frag(self):

        localctx = message_parser.Tag_param_fragContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_tag_param_frag)
        try:
            self.state = 66
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [8]:
                self.enterOuterAlt(localctx, 1)
                self.state = 64
                self.match(message_parser.TAG_PARAM)
                pass
            elif token in [3]:
                self.enterOuterAlt(localctx, 2)
                self.state = 65
                self.sub()
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


    class Close_tagContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPEN_TAG(self):
            return self.getToken(message_parser.OPEN_TAG, 0)

        def TAG_SLASH(self):
            return self.getToken(message_parser.TAG_SLASH, 0)

        def TAG_NAME(self):
            return self.getToken(message_parser.TAG_NAME, 0)

        def CLOSE_TAG(self):
            return self.getToken(message_parser.CLOSE_TAG, 0)

        def getRuleIndex(self):
            return message_parser.RULE_close_tag

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterClose_tag" ):
                listener.enterClose_tag(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitClose_tag" ):
                listener.exitClose_tag(self)




    def close_tag(self):

        localctx = message_parser.Close_tagContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_close_tag)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 68
            self.match(message_parser.OPEN_TAG)
            self.state = 69
            self.match(message_parser.TAG_SLASH)
            self.state = 70
            self.match(message_parser.TAG_NAME)
            self.state = 71
            self.match(message_parser.CLOSE_TAG)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SubContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPEN_SUB(self):
            return self.getToken(message_parser.OPEN_SUB, 0)

        def sub_field(self):
            return self.getTypedRuleContext(message_parser.Sub_fieldContext,0)


        def CLOSE_SUB(self):
            return self.getToken(message_parser.CLOSE_SUB, 0)

        def sub_convert(self):
            return self.getTypedRuleContext(message_parser.Sub_convertContext,0)


        def sub_spec(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(message_parser.Sub_specContext)
            else:
                return self.getTypedRuleContext(message_parser.Sub_specContext,i)


        def getRuleIndex(self):
            return message_parser.RULE_sub

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSub" ):
                listener.enterSub(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSub" ):
                listener.exitSub(self)




    def sub(self):

        localctx = message_parser.SubContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_sub)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 73
            self.match(message_parser.OPEN_SUB)
            self.state = 74
            self.sub_field()
            self.state = 76
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==10:
                self.state = 75
                self.sub_convert()


            self.state = 81
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==11:
                self.state = 78
                self.sub_spec()
                self.state = 83
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 84
            self.match(message_parser.CLOSE_SUB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Sub_fieldContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def sub_field_frag(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(message_parser.Sub_field_fragContext)
            else:
                return self.getTypedRuleContext(message_parser.Sub_field_fragContext,i)


        def getRuleIndex(self):
            return message_parser.RULE_sub_field

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSub_field" ):
                listener.enterSub_field(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSub_field" ):
                listener.exitSub_field(self)




    def sub_field(self):

        localctx = message_parser.Sub_fieldContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_sub_field)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 87 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 86
                self.sub_field_frag()
                self.state = 89 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==3 or _la==9):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Sub_field_fragContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SUB_FIELD(self):
            return self.getToken(message_parser.SUB_FIELD, 0)

        def sub(self):
            return self.getTypedRuleContext(message_parser.SubContext,0)


        def getRuleIndex(self):
            return message_parser.RULE_sub_field_frag

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSub_field_frag" ):
                listener.enterSub_field_frag(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSub_field_frag" ):
                listener.exitSub_field_frag(self)




    def sub_field_frag(self):

        localctx = message_parser.Sub_field_fragContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_sub_field_frag)
        try:
            self.state = 93
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [9]:
                self.enterOuterAlt(localctx, 1)
                self.state = 91
                self.match(message_parser.SUB_FIELD)
                pass
            elif token in [3]:
                self.enterOuterAlt(localctx, 2)
                self.state = 92
                self.sub()
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


    class Sub_convertContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SUB_CONVERT(self):
            return self.getToken(message_parser.SUB_CONVERT, 0)

        def SUB_IDENTIFIER(self):
            return self.getToken(message_parser.SUB_IDENTIFIER, 0)

        def getRuleIndex(self):
            return message_parser.RULE_sub_convert

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSub_convert" ):
                listener.enterSub_convert(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSub_convert" ):
                listener.exitSub_convert(self)




    def sub_convert(self):

        localctx = message_parser.Sub_convertContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_sub_convert)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 95
            self.match(message_parser.SUB_CONVERT)
            self.state = 96
            self.match(message_parser.SUB_IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Sub_specContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SUB_SPEC(self):
            return self.getToken(message_parser.SUB_SPEC, 0)

        def spec_value(self):
            return self.getTypedRuleContext(message_parser.Spec_valueContext,0)


        def getRuleIndex(self):
            return message_parser.RULE_sub_spec

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSub_spec" ):
                listener.enterSub_spec(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSub_spec" ):
                listener.exitSub_spec(self)




    def sub_spec(self):

        localctx = message_parser.Sub_specContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_sub_spec)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 98
            self.match(message_parser.SUB_SPEC)
            self.state = 99
            self.spec_value()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Spec_valueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def spec_func(self):
            return self.getTypedRuleContext(message_parser.Spec_funcContext,0)


        def spec_literal(self):
            return self.getTypedRuleContext(message_parser.Spec_literalContext,0)


        def getRuleIndex(self):
            return message_parser.RULE_spec_value

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSpec_value" ):
                listener.enterSpec_value(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSpec_value" ):
                listener.exitSpec_value(self)




    def spec_value(self):

        localctx = message_parser.Spec_valueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_spec_value)
        try:
            self.state = 103
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 101
                self.spec_func()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 102
                self.spec_literal()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Spec_literalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def spec_literal_frag(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(message_parser.Spec_literal_fragContext)
            else:
                return self.getTypedRuleContext(message_parser.Spec_literal_fragContext,i)


        def getRuleIndex(self):
            return message_parser.RULE_spec_literal

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSpec_literal" ):
                listener.enterSpec_literal(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSpec_literal" ):
                listener.exitSpec_literal(self)




    def spec_literal(self):

        localctx = message_parser.Spec_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_spec_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 106 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 105
                self.spec_literal_frag()
                self.state = 108 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==3 or _la==14):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Spec_literal_fragContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SPEC_VALUE(self):
            return self.getToken(message_parser.SPEC_VALUE, 0)

        def sub(self):
            return self.getTypedRuleContext(message_parser.SubContext,0)


        def getRuleIndex(self):
            return message_parser.RULE_spec_literal_frag

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSpec_literal_frag" ):
                listener.enterSpec_literal_frag(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSpec_literal_frag" ):
                listener.exitSpec_literal_frag(self)




    def spec_literal_frag(self):

        localctx = message_parser.Spec_literal_fragContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_spec_literal_frag)
        try:
            self.state = 112
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [14]:
                self.enterOuterAlt(localctx, 1)
                self.state = 110
                self.match(message_parser.SPEC_VALUE)
                pass
            elif token in [3]:
                self.enterOuterAlt(localctx, 2)
                self.state = 111
                self.sub()
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


    class Spec_funcContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SPEC_VALUE(self):
            return self.getToken(message_parser.SPEC_VALUE, 0)

        def OPEN_ARGLIST(self):
            return self.getToken(message_parser.OPEN_ARGLIST, 0)

        def spec_func_arg(self):
            return self.getTypedRuleContext(message_parser.Spec_func_argContext,0)


        def CLOSE_ARGLIST(self):
            return self.getToken(message_parser.CLOSE_ARGLIST, 0)

        def getRuleIndex(self):
            return message_parser.RULE_spec_func

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSpec_func" ):
                listener.enterSpec_func(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSpec_func" ):
                listener.exitSpec_func(self)




    def spec_func(self):

        localctx = message_parser.Spec_funcContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_spec_func)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 114
            self.match(message_parser.SPEC_VALUE)
            self.state = 115
            self.match(message_parser.OPEN_ARGLIST)
            self.state = 116
            self.spec_func_arg()
            self.state = 117
            self.match(message_parser.CLOSE_ARGLIST)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Spec_func_argContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def spec_func_arg_frag(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(message_parser.Spec_func_arg_fragContext)
            else:
                return self.getTypedRuleContext(message_parser.Spec_func_arg_fragContext,i)


        def getRuleIndex(self):
            return message_parser.RULE_spec_func_arg

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSpec_func_arg" ):
                listener.enterSpec_func_arg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSpec_func_arg" ):
                listener.exitSpec_func_arg(self)




    def spec_func_arg(self):

        localctx = message_parser.Spec_func_argContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_spec_func_arg)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 120 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 119
                self.spec_func_arg_frag()
                self.state = 122 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==3 or _la==16):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Spec_func_arg_fragContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ARGLIST_VALUE(self):
            return self.getToken(message_parser.ARGLIST_VALUE, 0)

        def sub(self):
            return self.getTypedRuleContext(message_parser.SubContext,0)


        def getRuleIndex(self):
            return message_parser.RULE_spec_func_arg_frag

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSpec_func_arg_frag" ):
                listener.enterSpec_func_arg_frag(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSpec_func_arg_frag" ):
                listener.exitSpec_func_arg_frag(self)




    def spec_func_arg_frag(self):

        localctx = message_parser.Spec_func_arg_fragContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_spec_func_arg_frag)
        try:
            self.state = 126
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [16]:
                self.enterOuterAlt(localctx, 1)
                self.state = 124
                self.match(message_parser.ARGLIST_VALUE)
                pass
            elif token in [3]:
                self.enterOuterAlt(localctx, 2)
                self.state = 125
                self.sub()
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





