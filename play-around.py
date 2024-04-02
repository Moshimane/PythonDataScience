#                      Removing the Py Rust               #
#                                                         #
###########################################################


###########################################################
#                      Strings                            #
###########################################################

string = 'i am coding in python'
print(string)

#string[0] = 'i'  : this throws a type error because str object does not support item assignment which means strings are immutable

#print substring to a specific index
print(string[0:5])

#print substring from index to the rest of the string
print(string[5:])

#use triple codes for multi line string

string = """Start
i am coding in python
End"""
print(string)

#another method is to use \n
string = 'start2\nI am coding in python\nEnd2'
print(string)

#convert number to a string and do concatination
string = 'I am coding in python '
num = 2

print(string + str(num))

##########################################################
#                       Lists                            #
##########################################################

numbers = [1, 2, 3, 4]
print(numbers)

print(numbers[0])

#print sub list
print(numbers[0:2])

#print rest of the list
print(numbers[2:])

#add/append item to list -- add 5
numbers.append(5)
print(numbers)

#add at a specific location -- add 0
numbers.insert(0,0)
print(numbers)

bigNumbers = [100,101,102,103,104]

#join lists
combinedNumbers = numbers + bigNumbers
print(combinedNumbers)

#print length of a list
print(len(combinedNumbers))

#check if number exists in list
print(100 in combinedNumbers)


##########################################################
#                   If Statement                         #
##########################################################

if 100 in combinedNumbers:
    print('100 exists in list')
else: print("100 doesn't exists in list")

value = input("Enter a number")
num = int(value)

if num == 0:
    print("Zero")
elif num == 1:
    print("One")
elif num >= 2:
    print("Greater than one")
elif num < 0 and num%2==0:
    print("Negative even number")
else:
    print("Negative odd number")
    

##########################################################
#                       For Loop                         #
########################################################## 

for i in combinedNumbers:
    if i%2==0:
        print(i, "is even number")

#specific number incremental
for i in range(0, 10, 2):
    print(i)
    
    
#range with length
for i in range(len(combinedNumbers)):
    print(combinedNumbers[i])
    
    
##########################################################
#                       Methods                          #
########################################################## 

def DoSomething():
    print("I am doing something")
    
DoSomething()

def calculateSum(a,b):
    return a+b


##########################################################
#                 Dictionaries and Tuples                #
########################################################## 

d = {'joy': 10, 'master': 9}

print(f'joy is {d["joy"]} years old')

d['joy2'] = 30
print(d)

for key in d:
    print(f'key: {key}, value: {d[key]}')
  
#print key value pairs using tuples
for k,v in d.items():
    print(f'key: {k}, value: {v}')

del d['master']
print(d)

# check if joy exists in dictionary
print('joy' in d)

# remove everything from dictionary
d.clear()
print(d)

#define a tuple
point = (5,9)

print(point[0])

# tupleas are immutables
# point[0] = 3 -> throws an error