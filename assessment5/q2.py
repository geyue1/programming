import string

def replace_ob(str:string):
    return str.replace("o","0").replace("b","6")

print(replace_ob('mobile phone'))
print(replace_ob('guitar'))