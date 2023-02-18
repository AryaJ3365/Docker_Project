import socket
import string
import time

if_file = open("./IF.txt", "r")
limerick_file = open("./Limerick.txt", "r")

result_file = open("./result.txt", "w")

if_data = if_file.read()
limerick_data = limerick_file.read()

if_words = if_data.split()
limerick_words = limerick_data.split()

ifWordNum = str(len(if_words))
limerickWordNum = str(len(limerick_words))

x = result_file.write("Total number of words in IF.txt: " + ifWordNum)
x = result_file.write("\n")

x = result_file.write("Total number of words in limerick.txt: " + limerickWordNum)
x = result_file.write("\n")
x = result_file.write("\n")

def counter(str):
    
    if_wordcount = dict()

    # Makes string have no spaces or newlines, lowercase, and no punctuation.
    str = str.strip()
    str = str.lower()
    str = str.translate(str.maketrans("", "", string.punctuation))
    
    words = str.split( )
    #print(str)
    
    for i in words:
        if i in if_wordcount:
            if_wordcount[i] += 1
        else:
            if_wordcount[i] = 1
            
    return if_wordcount

freq = counter(if_data)

new_freq = dict()
first = 0
second = 0
third = 0

for key, value in freq.items():
    
    if(value > first):
        third = second
        second = first
        first = value
    elif(value > second):
        third = second
        second = value
    elif(value > second):
        third = value

#print(first)
#print(second)
#print(third)

i = 0

for key, value in freq.items():
    
    if(value == first and i == 0):
        new_freq[key] = value
        i += 1
    elif(value == second and i == 1):
        new_freq[key] = value
        i += 1
    elif(value == third and i == 2):
        new_freq[key] = value
        i += 1

for key, value in freq.items():
    
    if(value == first and i == 0):
        new_freq[key] = value
        i += 1
    elif(value == second and i == 1):
        new_freq[key] = value
        i += 1
    elif(value == third and i == 2):
        new_freq[key] = value
        i += 1

nc = str(new_freq)
x = result_file.write("The top three words in the IF.txt file are: " + nc)
x = result_file.write("\n")
x = result_file.write("\n")

host = socket.gethostname()
IP_Address = socket.gethostbyname(host)

t = if_file.readlines()

x = result_file.write("Your machine's IP address is: " + IP_Address)
x = result_file.write("\n")

#print(t)
#print("hello world")

result_file.close()

result_file = open("./result.txt", "r")
result_data = result_file.read()
print(result_data)