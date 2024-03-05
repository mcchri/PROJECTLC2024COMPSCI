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
ref = db.reference()

data = ref.get()
nested_dict = data
def memory_level(avg,med,mod):
    level = avg*med*mod
def light_level(loc,light_val,on_or_off_light):    
    if loc == "room":
        if on_or_off_light:
            return light_val*10
        else:
            return int(light_val/2)
    elif loc == "outside":
         if on_or_off_light:
            return light_val*5
    else:
            return int(light_val/2)
        
def age_level(read,age,under_age):
    if read == "Yes":
        if under_age:
            return age*10
        else:
            return int(age/2)
    elif read == "No":
         if under_age:
            return age*5
    else:
            return int(age/2)
        
list_memory = []
list_light = []
list_age = []
count = 0
if data:
    for k,v in data.items():
        list1 = list(str(v.items()).split("'"))
        count = 0
        if k == "Light":
            for i in list1:
                if i == "Light_level":
                    string_element = list1[count+2].strip()
                    num1 = list(string_element.split(" "))
                    if num1[0].isnumeric():
                        list_light.append(int(num1[0]))
                count += 1
        elif k == "Age":
            for i in list1:
                if i == "Age":
                    string_element = list1[count+2].strip()
                    num1 = list(string_element.split(" "))
                    if num1[0].isnumeric():
                        list_age.append(int(num1[0]))
                count += 1
        elif k == "Memory":
            for i in list1:
                if i == "Memory_level":
                    string_element = list1[count+2].strip()
                    num1 = list(string_element.split(" "))
                    if num1[0].isnumeric():
                        
                        list_memory.append(int(num1[0]))
                count += 1        
      
Sum = sum(list_memory)
average_memory = Sum / len(list_memory)
median = round(len(list_memory) / 2) - 1
list_memory2 = list_memory
list_memory.sort()
memory_level(average_memory,list_memory2[median],statistics.mode(list_memory2))
location = input("Are you in a room or outside,(enter room or outside) ")
ONOROFF = input("Is there lights on in your room or is there sunlight outside,(True or False) ")
on_off = False
if ONOROFF == "True":
    on_off = True
else:
    on_off = False
Sum = sum(list_light)
average = Sum / len(list_light)
light_level = light_level(location,average,on_off)
read1 = input("Do you read any books,(Yes or No) ")
undereightheen = input("Are you under 18,(True or False) ")
under= False
if undereightheen == "True":
    under = True
else:
    under = False
age_level2 = age_level(read1,list_age[-1],under)

if(age_level2 > 150 and average_memory > 15):
    print("Lower age with comes with higher memory attention span")
elif(age_level2 < 150 and average_memory < 15):
    print("Higher age with comes with Lower memory attention span")
elif(light_level > 500 and average_memory > 15):
    print("Higher light intensity with comes with Higher memory attention span")
elif(light_level < 500 and average_memory < 15):
    print("Lower light intensity with comes with Lower memory attention span")    
