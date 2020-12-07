f = open("inputday1.txt","r")
myList = []
for x in f:
    myList.append(int(str.rstrip(x)))

print(myList)

##for firstNumber in myList:
##    for secondNumber in myList:
##        if firstNumber + secondNumber == 2020:
##            print(firstNumber * secondNumber)
            
for firstNumber in myList:
    for secondNumber in myList:
        for thirdNumber in myList:
            
            if firstNumber + secondNumber + thirdNumber == 2020:
                print(firstNumber * secondNumber * thirdNumber)
