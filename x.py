class Sentence:
    def __init__(self, sentence):
        self.sentence = sentence
        self.i = 0
        self.word = self.sentence.split()

    def __iter__(self):
        return self

    def __next__(self):
        if self.i >= len(self.word):
            raise StopIteration

        
        result = self.word[self.i]
        self.i += 1
        return result

my_sentence = Sentence('This is a Test')

for word in my_sentence:
    print(word)


def Sentance(sentence):
    sentence = sentence.split()
    for word in sentence:
        yield word
my_sentence = Sentence('This is a Test')

for word in my_sentence:
    print(word)

