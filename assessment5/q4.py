import string
import re

class StringChecker:
    def is_string_correct(self, string):
        return False

class IntChecker(StringChecker):

    def is_string_correct(self,str:string):
        if len(str)!=0 and re.match("^[0-9]*$",str):
            return True
        else:
            return False
