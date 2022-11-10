
def creditCardBill(list):
    result = 0
    for n in list:
        if n<100:
            result = result+n*(1+0.05)
        else:result = result+n*(1+0.03)

    return result

print(creditCardBill([175,45,165]))

def oddEven(list):
    oddCount:int= 0
    evenCount:int = 0
    for n in list:
         if n % 2==0:oddCount+=1
         else: evenCount+=1
    if oddCount==8 or evenCount==8:
        print("big win")
    elif oddCount==7 or evenCount==7:
        print("small win")
    else:print("lose")
oddEven([2,2,2,2,2,2,2,2,1])
oddEven([3,3,3,3,3,3,3,2,2])

import random
def coinGame():
    score = 0
    while score<5 and score>-5:
        n = random.randint(0,1)
        if n==1:
            score+=1
            print(f"the coin is a head and current score is {score}")
        else:
            score-=1
            print(f"the coin is a tail and current score is {score}")

    if(score>=5):print("win")
    else:print("lose")

coinGame()


def calculateStudentResults(list):
    for studentList in list:
        name = studentList[0]
        student_year = studentList[1]
        marks = studentList[2]
        score = 0
        for m in marks:
            score += m
        average = score/len(marks)
        if student_year==1 and average>=40:
            print(f"{name}'s average mark is {average} and has passed")
        else:print(f"{name}'s average mark is {average} and has failed")

        if student_year==2 and average>=50:
            print(f"{name}'s average mark is {average} and has passed")
        else:print(f"{name}'s average mark is {average} and has failed")

        if student_year==3 and average>=60:
            print(f"{name}'s average mark is {average} and has passed")
        else:print(f"{name}'s average mark is {average} and has failed")

studentList = []
studentList.append(["Eddard Stark", 3, [55,56,41,54,57,64,56,54]])
studentList.append(["Daenerys Targaryen", 2, [43,75,56,84,34,43,56,23]])
studentList.append(["Arya Stark", 1, [56,67,86,36,71,55,28]])
studentList.append(["Joffrey Baratheon", 2, [23,49,34,17,3,45,25,23]])
studentList.append(["Tyrion Lannister",3,[79,68,83,86,84,95,58,85]])
calculateStudentResults(studentList)

def buySell(list:[]):
    results = []
    n=1
    length = len(list)
    while n<=length:
        tempList = []
        if n-5<0:
            tempList = list[:n]
        else:tempList = list[n-5:n]
        result = "hold"
        if len(tempList)==5:
            k=1
            while k<5 and tempList[k-1]<tempList[k]:
                if k==4:result = "sell"
                k+=1
            k=1
            while k<5 and tempList[k-1]>tempList[k]:
                if k==4:result="buy"
                k+=1
        results.append(result)
        n+=1
    return results
a = [10,10,30,40,35,20,30,40,50,60,70,40,50,30,25,21,19,17,20]
print(buySell(a))

