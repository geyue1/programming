import string
class WordFamily:
    initial = None
    suffixes = None
    def __init__(self,initial:[],suffixes:[]):
        self.initial = initial
        self.suffixes = suffixes


class Pattern:
    pattern_name:string = None
    wordFamilies:[] = None
    def __init__(self,pattern_name:string,wordFamilies:[]):
        self.pattern_name = pattern_name
        self.wordFamilies = wordFamilies

    def recognise(self,str:string):
        str_list = str.split(" ")
        str_list_len = len(str_list)
        index =0
        if (str_list_len == len(self.wordFamilies)):
            for wordFamily in self.wordFamilies:
                temp = []
                n = len(wordFamily.initial)
                m = len(wordFamily.suffixes)
                i = 0
                while (i < n):
                    j = 0
                    while j < m:
                        temp.append(wordFamily.initial[i] + wordFamily.suffixes[j])
                        j += 1
                    i += 1
                if temp.count(str_list[index]) == 0:
                    return False
                index+=1
            return True
        else:
            return False
    @staticmethod
    def recognise_all(patterns:[],str:string):
        result:string=None
        for p in patterns:
            if p.recognise(str):
                result = p.pattern_name
        if result == None:
            result = "Unknown"
        print(result)
if __name__ == "__main__":
    nouns = ["dog", "cat"]
    verbs = ["bark", "meow"]
    is_word = ["is"]
    it_word = ["it"]
    sentence_types = [
        Pattern("Pattern 1", [WordFamily(nouns, ["", "s"]), WordFamily(verbs, ["s", ""])]),
        Pattern("Pattern 2", [WordFamily(it_word, [""]), WordFamily(is_word, [""]), WordFamily(verbs, ["ing"])]),
    ]
    Pattern.recognise_all(sentence_types, "it is barking")
    Pattern.recognise_all(sentence_types, "cats meow")
    Pattern.recognise_all(sentence_types, "cat is meowing")
