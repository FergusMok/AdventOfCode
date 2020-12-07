import re
f = open("inputday4.txt","r")
tempDict = {}
myList = []
for x in f:
    if x.isspace():
        myList.append(tempDict.copy())
        tempDict = {}
    else: 
        for valueKeyPair in str.rstrip(x).split(" "):
            tempList = valueKeyPair.split(":")
            tempDict[tempList[0]] = tempList[1]
myList.append(tempDict.copy())




# Part 1

def partone(myList):
    counter = 0
    for passport in myList:
        if all( x in passport.keys() for x in ['byr','iyr','eyr','hgt','hcl','ecl','pid'] ):
            counter += 1
    return counter
            
print(partone(my
              List))

def parttwo(myList):

    requirementDictionary = {
    "byr": lambda x : 1920 <= int(x) <= 2002,
    "iyr": lambda x : 2010 <= int(x) <= 2020,
    "eyr": lambda x : 2020 <= int(x) <= 2030,
    "hgt": lambda x : (x[-2:] == "in" and 59 <= int(x[:-2])<=76 ) or (x[-2:] == "cm" and 150 <= int(x[:-2]) <= 193),
    "hcl": lambda x : re.match(r'^#[0-9a-f]{6}$', x) != None,
    "ecl": lambda x : x in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"],
    "pid": lambda x : re.match(r'^[0-9]{9}$', x) != None,
    "cid": lambda x : True
    }
    counter = 0
    for passport in myList:
        try:
            if all(requirementDictionary[x](passport[x]) for x in passport.keys()) and all( x in passport.keys() for x in ['byr','iyr','eyr','hgt','hcl','ecl','pid'] ):
                counter += 1
        except ValueError:
            pass
    return counter

print(parttwo(myList))
