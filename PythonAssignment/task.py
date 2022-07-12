
# 1st problem
def substr(strIn):
    oldstr = ""
    lenVal = 0
    for letter in strIn:
        if letter not in oldstr:
            oldstr = oldstr+letter
            lenVal = len(oldstr)
        else:
            oldstr = oldstr.split(letter)[1]+letter
    return lenVal


# 2nd problem
def pairGen(n):
    def addPair(resList, groupStr, left, right):
        if left == 0 and right == 0:
            resList.append(groupStr)
        if left > 0:
            addPair(resList, groupStr+"(", left-1, right)
        if right > 0 and left < right:
            addPair(resList, groupStr+")", left, right-1)

    pairList = []
    addPair(pairList, "", n, n)
    return pairList


# 3rd problem
def palindromePart(strIn):
    palindromeList = []

    for i in range(len(strIn)):
        for j in range(i, len(strIn)):
            if i == 0:
                if strIn[i:j+1] == strIn[j::-1]:
                    if strIn[j::-1] not in palindromeList:
                        palindromeList.append(strIn[j::-1])
            else:
                if strIn[i:j+1] == strIn[j:i-1:-1]:
                    if strIn[j:i-1:-1] not in palindromeList:
                        palindromeList.append(strIn[j:i-1:-1])
    return palindromeList


print(substr("pwwkew"))
print(pairGen(3))
print(palindromePart("aab"))
