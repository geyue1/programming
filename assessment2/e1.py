import string


def spellCheck(word):
    spelling = {"teh":"the", "phyton":"python", "cta":"cat", "pyhton":"python", "dgo":"dog",
               "dukc":"duck", "mta":"mat"}
    if word in list(spelling.keys()):
        return spelling[word]
    else:
        return word

def translate(word):
    frenchDictionary = { "cat":"chat", "dog":"chien", "mouse":"souris",
                        "horse":"cheval", "cow":"vache", "sheep":"mouton",
                        "chicken":"poulet", "parrot":"perroquet", "duck":"canard",
                        "the":"la", "sat":"s'est assis", "mat":"tapis", "on":"sur"}
    if word in list(frenchDictionary.keys()):
        return frenchDictionary[word]
    else:
        return "(word not known)"

def checkAndTranslate(str:string):
    list = str.split(" ")
    frenchList = []
    for englisthWord in list:
        checkedWord = spellCheck(englisthWord)
        frenchWord = translate(checkedWord)
        frenchList.append(frenchWord)

    return " ".join(frenchList)

if __name__ == '__main__':
    s = checkAndTranslate("pyhton is an dgo or an cta or an duck")
    print(s)