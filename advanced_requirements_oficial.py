#imports all the necessary modules
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
#gets all the data from the firebase
data = ref.get()
# a function to calculate the memory level of the user using the average, median and mode of the memory data
def memory_level(avg,med,mod):
    level = avg*med*mod
# a function to calculate the memory level of the user by knowing the location of the user, knowing if there is a sufficient light source and the average light level.
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
# a function to calculate the age level of the user by knowing if the user reads, if they are underage and the average age of all the users who played the game        
def age_level(read,age,under_age):
    if read == "Yes":
        if under_age:
            age_level2 = age*10
        else:
            age_level2 = int(age/2)
    elif read == "No":
         if under_age:
            age_level2 = age*5
    else:
            age_level2 = int(age/2)
    # the program tells the user of what the outcome is from all the datasets
    if(age_level2 > 150 and average_memory > 15):
        print("The overall age is low and the memory is high therfore the well-being of the contestants is quite high")
    elif(age_level2 < 150 and average_memory < 15):
        print("The overall age is high and the memory is low therfore the well-being of the contestants is quite normal due to the age affectimg the attention span")
    elif(light_level > 500 and average_memory > 15):
        print("The overall light intensity is high and the memory is high therfore the well-being of the contestants is quite high")
    elif(light_level < 500 and average_memory < 15):
        print("The overall light intensity is low and the memory is low therfore the well-being of the contestants is quite normal")
    else:
        print("There is an anonamly in the data meaning some young people have low attention span or older people having higher attention span, in the case of the young people they need to improve their mental well-being.")
        
def specific_age(list_age1,list_memory1,user_age1,user_score1,age_unit1):
    sum1 = 0
    count = 0
    num=0
    limit = len(list_age1) - 64
    for i in list_age1:
    # This for loop gets the age value and its corresponding memory value by selecting its index
        if int(i / 10) == age_unit1 and count >= limit:
            index1 = len(list_age1) - list_age1.index(i)
            if index1 < 68:
                index2 = index1 - 37
                num+=1
                sum1 += list_memory1[index1]
        count += 1
    gen_sum = int(sum1/num)
    # Calculates the percentage of your memory score compared to your age group    
    percent = int((gen_sum/user_memory)*100-100)*-1
    print(gen_sum, "The memory score of your age group")
    print(user_memory, "Your memory score")
    if percent > 100:
        percent = percent - 100
    if gen_sum < user_memory:
        print("You have better attention span than your average age group, that means your mental well-being is strong")
        print("You have",percent,"% more attention span than your age group")
    if gen_sum < user_memory:
        print("You have worser attention span than your average age group, that means your mental well-being is not that strong. I advise you do practice more mental well-being activities.")
        print("You have",percent,"% less attention span than your age group")
    else:
        print("You are spot on the average memory score of your age group, its up to you if you want to improve your mental well-being.")
    
# the folllowing code extracts memory, light and age values from firebase
list_memory = []
list_memory_stat = []
list_light = []
list_age = []
count = 0
ok = 0
ok1 = 0
z=0
z1=0
if data:
    for k,v in data.items():
        list1 = list(str(v.items()).split("'"))
        for i in list1:
            if i == "Age":
                ok += 1
            elif ok == 1 and i != 'Age':
                num1 = list(i.split(" "))
                x = num1[1].replace(",","")
                if x.isnumeric():
                    # validates if the data is an integer    
                    list_age.append(int(x))
                #print(num1)
                ok = 0
                if i == ": ":
                    
                    ok1 += 1
            elif ok1 == 1:
                # There is a memory key in the age node because they need to be connected when finding the overall age with the memory score.
                ok1 = 0
                #print(i)
                num1 = list(i.split(" "))
                if num1[0].isnumeric():
                    # validates if the data is an integer    
                        list_age.append(int(num1[0]))
            if i == "Memory_level":
                z += 1
            elif z == 1 and i != 'Memory_level':
                num1 = list(i.split(" "))
                x = num1[1]
                listx = list(str(x).split("}"))
                #print(x)
                if listx[0].isnumeric():
                    # validates if the data is an integer    
                    list_memory_stat.append(int(listx[0]))
                #print(num1)
                z = 0
                if i == ": ":
                    
                    z1 += 1
            elif z1 == 1:
                z1 = 0
                #print(i)
                num1 = list(i.split(" "))
                if num1[0].isnumeric():
                    # validates if the data is an integer    
                        list_memory_stat.append(int(num1[0]))    
            
        if k == "Light":
            count = 0
            for i in list1:
                if i == "Light_level":
                    string_element = list1[count+2].strip()
                    num1 = list(string_element.split(" "))
                    if num1[0].isnumeric():
                    # validates if the data is an integer    
                        list_light.append(int(num1[0]))
                    #else:
                        #print("Data is not an integer.")
                count += 1
        elif k == "Memory":
            count = 0
            for i in list1:
                if i == "Memory_level":
                    string_element = list1[count+2].strip()
                    num1 = list(string_element.split(" "))
                    if num1[0].isnumeric():
                    # validates if the data is an integer    
                        list_memory.append(int(num1[0]))
                    #else:
                        #print("Data is not an integer.")    
                count += 1        
else:
    print("Data from firebase is not there")   
'''        
Getting all the required the infromation from the user in order to fill all the parameters
'''
Sum = sum(list_memory)
average_memory = Sum / len(list_memory) #average memory
median = round(len(list_memory) / 2) - 1 #median memory
list_memory2 = list_memory
list_memory.sort()
memory_level(average_memory,list_memory2[median],statistics.mode(list_memory2)) # average, median and mode
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

  
user_age = int(input("Input your age"))
age_unit = int(user_age/10)

user_score = int(input("input your score"))
user_level = int(input("input your level"))
user_memory = int((user_score+user_level)/2)

specific_age(list_age,list_memory2,user_age,user_memory,age_unit)    
