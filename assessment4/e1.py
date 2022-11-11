class WordBase:
  def __init__(self, basic_form):
    self.basic_form = basic_form

  # Returns a list of strings: list of eligible forms of the word,
  # including the basic form
  def get_forms(self):
    raise NotImplementedError()

  def __repr__(self):
    return f'{type(self).__name__}: {self.basic_form}'


class WordComparator:
  def match(self, word1, word2):
    return False

######### start ################
import string
class Noun(WordBase):
    def __init__(self,basic_form:string):
        super().__init__(basic_form)
    def get_plural_form(self):
        return self.basic_form + "es" if self.basic_form.endswith("s") else self.basic_form + "s"

    def get_forms(self):
        return [self.basic_form,self.get_plural_form()]

class UncountableNoun(Noun):
    def __init__(self,basic_form:string):
        super().__init__(basic_form)
    def get_forms(self):
        return [self.basic_form]

class IrregularNoun(Noun):
    plural_form:string = None
    def __init__(self,basic_form:string,plural_form:string):
        self.basic_form = basic_form
        self.plural_form = plural_form

    def get_forms(self):
        return [self.basic_form,self.plural_form]

class Verb(WordBase):

    def __init__(self,basic_form:string):
        super().__init__(basic_form)

    def get_forms(self):
        a = self.basic_form+"es" if self.basic_form.endswith("s") else self.basic_form+"s"
        b = self.basic_form[:-1]+"ing" if self.basic_form.endswith("e") else self.basic_form+"ing"
        c = self.basic_form+"d" if self.basic_form.endswith("e") else self.basic_form+"ed"
        return [self.basic_form,a,b,c]

class IrregularVerb(Verb):
    past_tense: string = None
    past_participle:string = None

    def __init__(self,basic_form:string,past_tense:string,past_participle:string):
        super().__init__(basic_form)
        self.past_tense = past_tense
        self.past_participle = past_participle
    def __init__(self,basic_form:string,past_tense:string):
        super().__init__(basic_form)
        self.past_tense = past_tense
        self.past_participle = past_tense

    def get_forms(self):
        a = self.basic_form + "es" if self.basic_form.endswith("s") else self.basic_form + "s"
        b = self.basic_form[:-1] + "ing" if self.basic_form.endswith("e") else self.basic_form + "ing"
        return [self.basic_form,a,b,self.past_tense,self.past_participle]

class ToBe(Verb):
    basic_form:string = "be"
    def __init__(self):
        pass

    def get_forms(self):
        return ["be", "am", "is", "are", "was", "were", "been","beeing"]

class Spellchecker:

    def __init__(self):
        pass

    def add_word(self,word:WordBase):

if __name__ == "__main__":
    noun = Noun("apple")
    print(noun.get_forms())