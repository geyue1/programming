import e1
def testProgram2(testValues,f):
    testPasses = []
    for test in list(testValues):
        try:
            if f(test)==testValues[test]:
                testPasses.append(True)
            else:
                testPasses.append(False)
        except:
            if testValues[test]=="error":
                 testPasses.append(True)
            else:
                testPasses.append(False)
    print(testPasses)
    if False not in testPasses:
        print("all tests passed")

if __name__=="__main__":
   testValues = {"dgo and cta and duck":"chien (word not known) chat (word not known) canard",1:"(word not known)"}
   testProgram2(testValues,e1.checkAndTranslate)