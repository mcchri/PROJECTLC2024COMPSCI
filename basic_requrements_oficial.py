import time
import statistics
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
# path to the private key
cred = credentials.Certificate("C:/Users/k_tur/OneDrive/Documents/cs/config.json")
# URL to the database
firebase_admin.initialize_app(cred,{'databaseURL': 'https://comp-sci-c8d0a-default-rtdb.europe-west1.firebasedatabase.app/'})
# get a reference to our db
ref = db.reference()

data = ref.get()
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
    for key, value in data.items():
        #change score to Memory ////////
        if key == 'Score':
            #print(value.get("Score"))
            first_key = list(value.items())
            for i in first_key:
                #print(list(str(i).split("'")))
                j = 0
                x = 0
                for i in list(str(i).split("'")):
                    # Change score to memory //////////
                    if i == "Score":
                        j = 0
                        #print(i)
                    j+=1
                    x+=1
                    if j == 3:
                        if x % 2 ==0:
                            i = list(i.split(" "))
                            #print(i[0])
                            if i[0].isnumeric():
                                list_memory.append(int(i[0]))
            break
Sum = sum(list_memory)
average = Sum / len(list_memory)
print("average memory span is",round(average))
median = round(len(list_memory) / 2) - 1
list_memory2 = list_memory
list_memory.sort()
print("median memory span is",list_memory2[median])
print("Modal number of memory is",(statistics.mode(list_memory2)))
memory_level(average,list_memory2[median],statistics.mode(list_memory2))