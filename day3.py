f = open("inputday3.txt","r")
myList = []



for x in f:
    print(x)
    myList.append(str.rstrip(x))

# The pattern actually continues for an infinite amount,
# and I need to reach the bottom of the whole thing.


counter = 0
widthOfList = len(myList[0])
# If i*3 exceeds widthOfList, I need to
# take the next highest multiple of widthOfList and minus i*3

# if width of list is 10
# 9 + 3 = 12
# I need to return 2.

# if width of list is 9
# 12, I need to return 3.
# 12 % 9 


# So I've found for right 3 down 1,
# I need to find for right 1, down 1


def day2fn(down,right):
    counter = 0
    rightCounter = 0
    
    for i in range(0,len(myList),down):
        currentPosition = myList[i][(rightCounter) % widthOfList ]
        rightCounter += right
        if currentPosition == "#":
           counter = counter + 1
    return counter

print("OUTPUT")
print(day2fn(1,1))
print(day2fn(1,3))
print(day2fn(1,5)) 
print(day2fn(1,7))
print(day2fn(2,1)) 

print( day2fn(1,1) * day2fn(1,3) * day2fn(1,5) * day2fn(1,7) * day2fn(2,1))










