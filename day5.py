def listProcessor(myStr):
    def processor(lowerLetter, upperLetter, start, end, myStr):
        if len(myStr) == 1:
            if myStr == lowerLetter:
                return start
            else:
                return end
        elif myStr[0] == lowerLetter:
            return processor(lowerLetter, upperLetter, start, start + (end-start)//2 , myStr[1:]) 
        elif myStr[0] == upperLetter: 
            return processor(lowerLetter, upperLetter, start + (end-start) // 2 + 1, end , myStr[1:])
        else:
            return 0
        
    row = processor("F","B",0,127,myStr[:7]) 
    column = processor("L","R",0,7,myStr[-3:])
    return (row * 8) + column

anotherList = []
with open('inputday5.txt') as f :
    data = f.read().split('\n')
    for x in data:
        if x.isspace() != True:
            try:
                anotherList.append(listProcessor(x))
            except:
                pass
            
print(max(anotherList))

potentialCandidates = []
for x in anotherList:
    if (x+1 not in anotherList) and (x+2 in anotherList):
        potentialCandidates.append(x+1)

print(potentialCandidates)
