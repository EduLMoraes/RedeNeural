#   Implementação de um chatbot básico:
#   
#   Utilize uma biblioteca de processamento de linguagem natural, 
#   como o NLTK, para processar a entrada do usuário e gerar respostas adequadas.
#   Crie um conjunto de regras ou use técnicas de aprendizado de
#   máquina para ensinar o chatbot a responder a perguntas comuns.
#   Teste o chatbot interagindo com ele e observe como ele lida com
#   diferentes tipos de perguntas e entradas do usuário.
#   Considere a possibilidade de adicionar recursos extras, como
#   aprendizado por reforço, para melhorar a capacidade de resposta
#   do chatbot.

import nltk
from nltk import *
from nltk.stem.porter import PorterStemmer

stemmer = PorterStemmer()

#nltk.download('punkt')

def tokenize(text):
    return nltk.word_tokenize(text)

def stem(word):
    return stemmer.stem(word.lower())

def bag_of_words(toeknize_setence, words):
    pass

a = "How long does shipping take?"
print(a)
a = tokenize(a)
print(a)
b = [stem(w) for w in a]
print(a)

