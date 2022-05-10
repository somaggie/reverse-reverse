#reverseReverse reverses a list just like the reverse() method by iterating through a given list backwards, 
# starting at the end of the given list
def reverseReverse(myList):
    reversedList = []
    i = len(myList) - 1
    while i > -1:
        reversedList.append(myList[i])
        i -= 1
    return reversedList

sampleList = ['item a', 'item B', 'item c', 'item D']

#expected output: ['item D', 'item c', 'item B', 'item a']
print (reverseReverse(sampleList))
