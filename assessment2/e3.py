import string
def giveHelp(text:string,advice:[]):
    result = ""
    temp =[]
    textList = text.split(" ")
    for keyWord in textList:
        if (keyWord in advice) and (keyWord not in temp):
            result = result+advice[keyWord]+"\n"
            temp.append(keyWord)
    return result

advice = { "blank":"try turning the screen on", "signal":"reboot the Wi-Fi",
          "power":"check if the battery is charged", "frozen":"turn it off and on again"}

print(giveHelp("My computer is frozen the keyboard has no power and the monitor has no power",advice))