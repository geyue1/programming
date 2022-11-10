
def combineDictionaries(dict_1:{},dict_2:{}):
    result = {}
    key_2_list = list(dict_2)
    for k,v in dict_1.items():
        if(v in key_2_list):
            result[k] = dict_2[v]
        else:result[k] = "(not known)"
    return result

dict_1 = { "cat":"chat", "dog":"chien", "mouse":"souris",
                    "horse":"cheval", "cow":"vache", "sheep":"mouton",
                    "the":"la", "eats":"mange", "food":"nourriture", "chicken":"poulet"}

dict_2 = { "chat":"Katze", "souris":"Maus", "chien":"Hund",
                         "cheval":"Pferd", "vache":"Kuh", "mouton":"Schaf",
                         "la":"das", "mange":"frisst", "nourriture":"Futter"}

print(combineDictionaries(dict_1,dict_2))