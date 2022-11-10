import string
class Record:
    word = None
    is_noun = None
    def __init__(self,word:string,is_noun:bool):
        self.word = word
        self.is_noun = is_noun

    def get_plural(self):
        if (self.is_noun):
            return self.word+"s"
        else:
            return self.word

    def is_the_same_as(self,word:string):
        if (word==self.get_plural()):
            return True
        else:
            return False

if __name__ == "__main__":
    r = Record("apple",True)
    r.is_the_same_as("apples")
    print(Record("table", True).is_the_same_as("table"))