


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
from typing import Type
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

    def __init__(self,basic_form:string,*x):
        super().__init__(basic_form)
        if  len(x) == 1:
            self.past_tense = x[0]
            self.past_participle=x[0]
        elif len(x)==2:
           self.past_tense = x[0]
           self.past_participle = x[1]
        else:
            raise TypeError

    def get_forms(self):
        a = self.basic_form + "es" if self.basic_form.endswith("s") else self.basic_form + "s"
        b = self.basic_form[:-1] + "ing" if self.basic_form.endswith("e") else self.basic_form + "ing"
        return [self.basic_form,a,b,self.past_tense,self.past_participle]

class ToBe(Verb):
    basic_form:string = "be"
    def __init__(self):
        pass

    def get_forms(self):
        return ["be", "am", "is", "are", "was", "were", "been","being"]

class IdenticalWordComparator(WordComparator):
    def match(self, word1, word2):
        return True if word1==word2 else False

class OneSymbolDiffComparator(WordComparator):
    def match(self, word1, word2):
        if len(word1)==len(word2):
            temp = []
            list1 = list(word1)
            list2= list(word2)
            i=0
            while i< len(list1):
                if list1[i]!=list2[i]:
                    temp.append(list1[i])
                    temp.append(list2[i])
                i+=1
            return True if len(temp)==2 else False
        return False

class SwapTwoSymbolsComparator(WordComparator):
    def match(self, word1, word2):
        if len(word1)==len(word2) and word1!=word2:
            list1 = list(word1)
            list2 = list(word2)
            i = 0
            while i<(len(list1)-1):
                if list1[i]==list2[i] and list1[i+1]== list2[i+1] and list1[i]!=list1[i+1]:
                    return True
                i+=1
        return False
class Spellchecker:

    dictionary = {}
    key_noun = "N"
    key_verb = "V"


    def __init__(self):
        pass

    def add_word(self,wordBase:WordBase):
        if wordBase.basic_form in self.dictionary:
            if isinstance(wordBase, Noun):
                self.dictionary.get(wordBase.basic_form).update({self.key_noun:wordBase.get_forms()})
            else:
                self.dictionary.get(wordBase.basic_form).update({self.key_verb:wordBase.get_forms()})
        else:
            word_forms = {}
            if isinstance(wordBase,Noun):
                word_forms = {self.key_noun:wordBase.get_forms()}
            else:
                word_forms = {self.key_verb: wordBase.get_forms()}
            self.dictionary.update({wordBase.basic_form:word_forms})

    def delete_word(self,word:string,type:Type):
        if word in self.dictionary:
            forms:{} = self.dictionary.get(word)
            if issubclass(type,Noun) and (self.key_noun in forms):
                forms.pop(self.key_noun)
            elif issubclass(type,Verb) and (self.key_verb in forms):
                forms.pop(self.key_verb)
            if len(forms) ==0:
                self.dictionary.pop(word)

    def get_all_words(self):
        words = []
        for _,v in self.dictionary.items():
            for _,v_ in v.items():
                for word in v_:
                   words.append(word)

        return words
    def get_all_forms(self,word:string):
        forms = []
        if word in self.dictionary:
            for _,v in self.dictionary.get(word).items():
                for word in v:
                   forms.append(word)
        return forms

    def is_correct_sentence(self,sentence:string):
        words = sentence.split(" ")
        all_words = self.get_all_words()
        for word in words:
            if(all_words.count(word)<=0):
                return False
        return True

    def find_matches(self,word:string,wordComparators:[]):
        result = []
        all_words = self.get_all_words()
        for comparator in wordComparators:
            for word_form in all_words:
                if comparator.match(word,word_form):
                    result.append(word_form)
        return result

    def autocorrect_word(self,word:string,wordComparators:[]):
        all_words = self.get_all_words()
        for comparator in wordComparators:
            result = []
            for word_form in all_words:
                if comparator.match(word, word_form):
                    result.append(word_form)
            if len(result)>0:
                result.sort()
                return result[0]
        return word



    def autocorrect_sentence(self,sentence:string,wordComparators:[]):
        words = sentence.split(" ")
        temp = []
        for word in words:
            correct_word = self.autocorrect_word(word,wordComparators)
            temp.append(correct_word)
        return " ".join(temp)
    def __str__(self):
        print(self.dictionary)

if __name__ == "__main__":
    print(isinstance(Noun("cat"), WordBase))
    print(isinstance(Verb("move"), WordBase))
    print(set(Noun("cat").get_forms()) == {"cat", "cats"})
    print(set(Verb("move").get_forms()) == {"move", "moving", "moved", "moves"})
    print(set(IrregularVerb("go", "went", "gone").get_forms()))
    print(set(IrregularVerb("go", "went", "gone").get_forms()) == {"go", "went", "gone", "going", "gos"})

    check = Spellchecker()
    check.add_word(Verb("please"))
    check.add_word(Verb("cat"))
    check.add_word(IrregularVerb("put","puttted"))
    check.add_word(Noun("put"))
    #check.add_word(IrregularVerb("puttt"))
    #check.add_word(IrregularNoun("puttings"))
    check.__str__()
    check.delete_word("put",Verb)
    print(check.get_all_forms("put"))
    print(check.autocorrect_word("pleese",[SwapTwoSymbolsComparator()]))
    print(check.autocorrect_sentence("cads are lovley", [OneSymbolDiffComparator()]))
