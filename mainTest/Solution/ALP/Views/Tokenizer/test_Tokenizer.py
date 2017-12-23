
from ....ALP.Controllers.Tokenization.Tokenizer import *

t = Tokenizer()
t.Tokenize("./بسم الله الرحمن 5#الرحيم. الح@مد لله رب4 العالمين.")
#t = Tokenizer("the avg: 8.3 time 2:23:21 am... This is   nice...")
sentences = t.Tokenize("./بسم الله الرحمن 5#الرحيم. الح@مد لله رب4 العالمين.")
print(t)
t.print_tokens()