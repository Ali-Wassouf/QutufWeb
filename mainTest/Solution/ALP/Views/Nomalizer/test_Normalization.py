'''
Created on ١٠‏/٠٣‏/٢٠١٠
ن
@Created by: Muhammad Altabba
'''

from ....ALP.Controllers.Tokenization.Tokenizer import *
from ....ALP.Controllers.Normalization.Normalizer import Normalizer

if __name__ == '__main__':
    tok = Tokenizer()
    tok.Tokenize("الْعَرَبــــــِيّةُ")
    norm = Normalizer(tok.Sentences)
    norm.Normalize()

    for i in range(len(norm.Sentences)):
        for j in range(len(norm.Sentences[i].Words)):
            print(norm.Sentences[i].Words[j].OriginalString)
            print(norm.Sentences[i].Words[j].FirstNormalizationForm)
            print(norm.Sentences[i].Words[j].SecondNormalizationForm)
#            
    x = 0
