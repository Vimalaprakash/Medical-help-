def fever():
    
    f=open("fever.txt","r")
    print(f.read())

def headache ():
    f=open("headache.txt","r")
    print(f.read())

def stmoach_pain():
    f=open("stomach pain.txt","r")
    print(f.read())

def leg_pain():
    f=open("leg pain.txt","r")
    print(f.read())
    
print("Hello!")
a=input("What is your problem ")
print("you have ",a)
print("This is say helpfull tips to you")

if (a == "fever" or a == "Fever"):
    fever()
    
elif (a == "headache" or a == "Headache"):
    headache()

elif (a == "stomach pain" or a=="Stmoach Pain"):
    stmoach_pain()

elif (a == "leg pain"):    
         leg_pain()

