import time
import statistics
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
# path to the private key
cred = credentials.Certificate("C:/Users/19CTurean.ACC/Documents/config.json")
# URL to the database
firebase_admin.initialize_app(cred,{'databaseURL': 'https://comp-sci-c8d0a-default-rtdb.europe-west1.firebasedatabase.app/'})
# get a reference to our db
ref = db.reference('Memory')

data = ref.get()
print(ref.get())
nested_dict = data
def memory_level(avg,med,mod):
    level = avg*med*mod
    if level < 5:
        print("You have low memory span")
        print("My prediction is that you should play more of this game for your own mental well-being.")
    elif level < 15:
        print("You have average memory span")
        print("My prediction is that you should prehaps play the memory game for your own mental well-being.")
    else:
        print("You Have above average memory span")
        print("My prediction is that you should take a break for your own mental well-being.")
# Loop through the nested dictionary until the 'Score' key is found

list_memory = []
if data:
    print(data)
    list1 = list(str(data).split("'"))
    count = 0
    for i in list1:
        if i == "A_Memory_level":
            string_element = list1[count+2]
            num1 = list(string_element.split(" "))
            if num1[0].isnumeric():
                list_memory.append(int(num1[0]))
        count += 1        

    
Sum = sum(list_memory)
average = Sum / len(list_memory)
print("average memory span is",round(average),"points.")
median = round(len(list_memory) / 2) - 1
list_memory2 = list_memory
list_memory.sort()
print("median memory span is",list_memory2[median],"points.")
print("Modal number of memory is",(statistics.mode(list_memory2)),"points.")
memory_level(average,list_memory2[median],statistics.mode(list_memory2))
