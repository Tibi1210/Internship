
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
    if 1 <= n <= 8:
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
    return "Number must be between [1-8]"


# 3rd problem

def isPalindrome(strIn, start, end):
    while start < end:
        if strIn[start] != strIn[end]:
            return False
        start += 1
        end -= 1
    return True

def allPalPartitions(palindromeList, onePalList, start, n, strIn):
    if start >= n:
        palindromeList.append(onePalList.copy())
        
    for i in range(start, n):
        if isPalindrome(strIn, start, i):
            onePalList.append(strIn[start:i + 1])
            allPalPartitions(palindromeList, onePalList, i + 1, n, strIn)
            onePalList.pop()

def palindromePart(strIn):
    if 1 <= len(strIn) <= 16:
        strIn = strIn.lower()
        n = len(strIn)
        palindromeList = []
        onePalList = []

        allPalPartitions(palindromeList, onePalList, 0, n, strIn)
        return palindromeList
    return "String length must be between [1-16] characters"

print(substr("pwwkew"))
print(pairGen(3))
print(palindromePart("aab"))
