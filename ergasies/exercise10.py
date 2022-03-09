import math

val = """This eBook is for the use of anyone anywhere in the United States and most
other parts of the world at no cost and with almost no restrictions
whatsoever.  You may copy it, give it away or re-use it under the terms of
the Project Gutenberg License included with this eBook or online at
www.gutenberg.org.  If you are not located in the United States, you'll have
to check the laws of the country where you are located before using this ebook."""

firstLast=[]
list2=[]
#
def toBinary(val):
  l,m=[],[]
  for i in val:
    l.append(ord(i))
  for i in l:
    m.append(int(bin(i)[2:]))
  return m

def first_n_digits(num, n=2):
    return num // 10 ** (int(math.log(num, 10)) - n + 1)

def get_last_digits(num, last_digits_count=2):
    return abs(num) % (10**last_digits_count)

var=toBinary(val)

for i in range(len(var)):
    # print(var[i])
    # print(("%02d" % first_n_digits(var[i])),("%02d" % get_last_digits(var[i])))
    firstLast.append(("%02d" % first_n_digits(var[i])))
    firstLast.append(("%02d" % get_last_digits(var[i])))

# print(firstLast)

helpList = "".join(firstLast)
firstLast=[]
firstLast.append(helpList)

# print(firstLast)
# print(type(firstLast[0]))
# # firstLast[0]=str(firstLast[0])
# print(type(firstLast[0]))
# print(firstLast)

list3=[]
list2=[]

helpList=[]
sixteenDList=[]

count=0
for i in firstLast[0]:
    count+=1
    # print(i)
    helpList.append(i)
    if count%16==0:
        sixteenDList.append(helpList)
        helpList=[]

# print(range(len(sixteenDList)))

myList=[]
helpList=[]

for i in range(len(sixteenDList)):
    helpList = "".join(sixteenDList[i])
    myList.append(helpList)
    helpList=[]

# print(myList)

count2=0
count3=0
count5=0
count7=0

# print(type(list5[1]))  #=string

for i in range(len(myList)):
    # print(int(myList[i], base=2))
    if int(myList[i], base=2)%2==0:
        count2+=1
    elif int(myList[i], base=2)%3==0:
        count3+=1
    elif int(myList[i], base=2)%5==0:
        count5+=1
    elif int(myList[i], base=2)%7==0:
        count7+=1

print(len(myList))

print("Percentage of numbers devided by two:",count2*100/len(myList),"%")
print("Percentage of numbers devided by three:",count3*100/len(myList),"%")
print("Percentage of numbers devided by five:",count5*100/len(myList),"%")
print("Percentage of numbers devided by seven:",count7*100/len(myList),"%")
