'''
Created on ١٠‏/٠٣‏/٢٠١٠

@Created by: Muhammad Altabba
'''

from ....ALP.Controllers.TextEntities.Sentence import *
from ....ALP.Controllers.TextEntities.Word import *
from ....ALP.Controllers.Tokenization.TokenType import TokenType
from ....ALP.Models.Lexicon import *
from ....ALP.Models.Lexicon.LettersConstants import ArabicLetters
from ....ALP.Models.Tokenization.SentenceSeperatorsList import *
from ....ALP.Models.Tokenization.TokenizerConstants import *
import re


class Tokenizer(object):
    """
     # PyUML: Do not remove this line! # XMI_ID:_hUBlVI34Ed-gg8GOK1TmhA
    """
    '''
    Text Tokenizer
    '''
    FinalCharsType = []

    def __init__(self):
        '''
        Constructor
        '''

        self.string = ""
        self.FinalCharsType = []
        self.lis_of_tokens = []

    pass

    def Tokenize(self, string):

        self.string = string
        #        if not self.isSentenceSeperator(self.string[len(self.string)-1])\
        #        and not self.isSentenceSeperator(self.string[len(self.string)-2])\
        #        and not self.isSentenceSeperator(self.string[len(self.string)-3]):
        #            self.string += '.'
        if not self.isSentenceSeperator(self.string[- 1]):
            self.string += '.'

        self.__FillFinalCharsTypeList(self.string)

        wordStart = 0
        sentenceStart = 0
        wordsList = []
        sentences = []
        i = 0
        while i < len(self.string):
            if self.FinalCharsType[i] != 's' and self.FinalCharsType[i + 1] == 's':
                if self.FinalCharsType[i] in WhiteSpacesList:
                    word = Word(self.string[wordStart:i + 1])
                    word.TokenType = TokenType(2)  # (2, "White Space")
                    wordsList.append(word)
                elif self.FinalCharsType[i] == 'l':
                    words = self.__SeparateByLanguage(self.string[wordStart:i + 1])
                    wordsList.extend(words)
                elif self.FinalCharsType[i] == 'd':
                    word = Word(self.string[wordStart:i + 1])
                    word.TokenType = TokenType(1)  # (1, "Numbers")
                    wordsList.append(word)
                wordStart = i + 1

            if self.FinalCharsType[i] == 's':
                isEndOfSentence = False
                sentenceEnd = i + 1
                while i + 1 < len(self.string) \
                        and (self.string[i] == self.string[i + 1]
                             or self.string[i + 1] == ' '
                             or (self.isSentenceSeperator(self.string[i]) and self.isSentenceSeperator(self.string[i + 1]))):
                    if self.isSentenceSeperator(self.string[i]):
                        isEndOfSentence = True
                        sentenceEnd = i + 2
                    i += 1
                word = Word(self.string[wordStart:i + 1])
                if self.string[i] in WhiteSpacesList:
                    word.TokenType = TokenType(2)  # (2, "White Space")
                else:
                    word.TokenType = TokenType(3)  # (3, "Punctuation")
                wordsList.append(word)
                wordStart = i + 1

                if self.isSentenceSeperator(self.string[i]) == True or isEndOfSentence == True:
                    sentence = Sentence(self.string[sentenceStart:sentenceEnd])
                    sentence.Words = wordsList
                    sentences.append(sentence)
                    sentenceStart = i + 1
                    wordsList = []

            i += 1
        return sentences

    pass

    def __SeparateByLanguage(self, string):

        words = []
        wordStart = 0
        previousLanguage = ''
        currentLanguage = ''
        if (string[0] in ArabicLetters.AllLetters or string[0] in DiacriticsConstants.AllDiacritics):
            previousLanguage = TokenType.Constants.Id.ArabicText
        elif (string[0] not in ArabicLetters.AllLetters):
            previousLanguage = TokenType.Constants.Id.OtherText
        for i in range(1, len(string)):
            if (string[i] in ArabicLetters.AllLetters or string[i] in DiacriticsConstants.AllDiacritics):
                currentLanguage = TokenType.Constants.Id.ArabicText
            elif (string[i] not in ArabicLetters.AllLetters):
                currentLanguage = TokenType.Constants.Id.OtherText

            if (previousLanguage != currentLanguage):
                #                print(previousLanguage, ', ', currentLanguage,\
                #                      ', ', wordStart, ', ', i)
                word = Word(string[wordStart:i])
                word.TokenType = TokenType(previousLanguage)  # (0 or 4, "Text")
                wordStart = i
                words.append(word)
                previousLanguage = currentLanguage
        else:
            if (len(string) == 1):
                i = 0
                currentLanguage = previousLanguage
            word = Word(string[wordStart:i + 1])
            word.TokenType = TokenType(currentLanguage)  # (0, "ArabicText")
            words.append(word)

        return words

    pass

    def isSentenceSeperator(self, sepChar):
        # ...
        if sepChar in SentenceSeperatorsList:
            return True
        else:
            return False

    pass

    def __FillFinalCharsTypeList(self, string):

        # new lists for for applying independent algorithm 
        self.FinalCharsType = []

        i = 0
        while i < len(string):
            if ((string[i] in isAmbiguousA) or
                    (string[i] in isAmbiguousB) or
                    (string[i] in isAmbiguousC) or (string[i] in isAmbiguousD)) and (i + 1 == len(string) or i == 0):
                self.FinalCharsType.append('s')
                i += 1
                continue

            elif string[i] in isDigit:
                self.FinalCharsType.append("d")
            elif string[i] not in isAmbiguousA \
                    and string[i] not in isAmbiguousB \
                    and string[i] not in isAmbiguousC \
                    and string[i] not in isAmbiguousD \
                    and string[i] not in isSep:
                # or letter given letter
                self.FinalCharsType.append("l")
            elif string[i] in isAmbiguousA:  # to checking the rules (dot)
                if string[i - 1] not in isAmbiguousA \
                        and string[i - 1] not in isAmbiguousB \
                        and string[i - 1] not in isAmbiguousC \
                        and string[i - 1] not in isSep \
                        and string[i + 1] not in isAmbiguousA \
                        and string[i + 1] not in isAmbiguousB \
                        and string[i + 1] not in isAmbiguousC \
                        and string[i + 1] not in isSep:
                    # between two letter & between two digit give two letter
                    if string[i - 1] in isDigit and string[i + 1] in isDigit:
                        self.FinalCharsType.append("d")
                    else:
                        self.FinalCharsType.append("l")
                else:
                    self.FinalCharsType.append('s')
            elif string[i] in isSep:
                self.FinalCharsType.append('s')
            elif string[i] in isAmbiguousB:
                if string[i - 1] in isDigit and string[i + 1] in isDigit:
                    self.FinalCharsType.append("d")
                else:
                    self.FinalCharsType.append('s')
            elif string[i] in isAmbiguousC:  # between two numbers give letter
                if string[i - 1] in isDigit and string[i + 1] in isDigit:
                    self.FinalCharsType.append("l")
                else:
                    self.FinalCharsType.append('s')
            else:
                self.FinalCharsType.append('s')
            i += 1

    pass

    def __str__(self):
        output_str = ""

        for i in range(len(self.string)):
            output_str += self.string[i].__str__()
        return output_str
        return output_str

    pass

    def print_tokens(self):
        list_of_tokens = []
        token = ""
        for i in range(len(self.string)):
            if self.FinalCharsType[i] == "l":
                token += self.string[i]
            elif token != "":
                list_of_tokens.append(token)
                token = ""
        print(list_of_tokens)
