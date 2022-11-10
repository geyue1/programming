import string
class Word:
    word:string = None
    def __init__(self,word:string):
        self.word = word
    def get_forms(self):
        pass

class VerbWord(Word):
    def __init__(self,word:string):
        super().__init__(word)

    def get_forms(self):
        a = self.word
        b = self.word+"d" if self.word.endswith("e") else self.word+"ed"
        c = self.word+"ing"
        d = self.word+"s"
        return a,b,c,d

class NounWord(Word):
    def __init__(self,word:string):
        super().__init__(word)

    def get_forms(self):
        a = self.word
        b = self.word+"s"
        return a,b

class Dict:
    words:[] = []

    def add_word(self,word:Word):
        for w in word.get_forms():
             self.words.append(w)

    def is_known(self,str:string):
        return True if self.words.count(str)>=1 else False


if __name__ == "__main__":
    w = NounWord("apple")
    m = VerbWord("move")
    d = Dict()
    d.add_word(w)
    d.add_word(m)
    print(d.words)
    print(d.is_known("apples"))
    print(d.is_known("moved"))