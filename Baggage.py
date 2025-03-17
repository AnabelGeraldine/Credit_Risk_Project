import random

bag=[["BG903","Mr.Abraham","First-Class",8,15],
     ["BG542","Ms.Lincoln","Bussiness",20,40]]

def menu():
    print("------------------------")
    print("Airplane Baggage Manager")
    print("------------------------")
    view()
    print("------------------------")
    print("1. Register Baggage     ")
    print("2. Close Registration   ")
    print("------------------------")
    opt=-1
    while opt<1 or opt>2:
        opt=int(input("Choose: "))

    return opt

def view():
    if bag==[]:
        print("No Baggages")
        
    else:
        print("+======+=========================+==================+===========+=================")
        print("|  ID  |      Baggage Owner      |    Ticket Type   |   Weight  |   Total Cost   |")
        print("+======+=========================+==================+===========+=================")
        mydata= "| {:4s} | {:23s} | {:15s} | {:9d} | ${:13.2f} |"
        for i in range(len(bag)):
            print(mydata.format(bag[i][0],bag[i][1],bag[i][2],bag[i][3],bag[i][4]))
        print("+======+=========================+==================+===========+=================")
        
        
        

def regbag():
    ti=str(random.randint(0,9))
    ex=str(random.randint(0,9))
    ty=str(random.randint(0,9))
    '''
    for i in range(3):
        udin += str(random.randint(0,9))
    '''
    udin="BG"+ti+ex+ty
    print("Your ID:",udin) 
    
    nem=" "
    while nem[:3]!="Mr." and nem[:3]!="Ms.":
        nem=input("Your name (Mr./Ms.): ")

    taip=" "
    while taip!="Economy" and taip!="Business" and taip!="First-Class":
        taip=input("Ticket Type (Economy | Business | First-Class): ")

    weh=-1
    while weh<=7:
        weh=int(input("Baggage Total Weight(kg): "))

    tbc=-1
    if taip=="Economy":
        tbc=25+(weh/8)
        

    elif taip=="Business":
        tbc=20+(weh/8)
        

    elif taip=="First-Class":
        tbc=15+(weh/8)
        

    
    '''
    nek weh>=7 dimasukin bag[]
    yg taip nek misale = Economy or taip=Business or taip=First-Class
    while nem[:3]=="Mr." or nem[:3]=="Ms.":
        tarok bawah e

    
    ti=str(random.randint(000,999))
    udin="BG",ti
    print("Your ID:",udin)
    
    '''
    print()
    print("==================================================")
    print("Baggage ID                     : ",udin            )
    print("Baggage Owner                  : ",nem             )
    print("Baggage Owner Ticket           : ",taip            )
    print("Baggage Total Weight           : ",weh,"kg")
    print("--------------------------------------------------")
    print("Total Baggage Cost             :  $",tbc           )
    print("==================================================")
    bag.append([udin,nem,taip,weh,tbc])
    print()
    print()
    print("Baggage Registered...                             ")
    print()

    
    
    
    
    
    

opt=-1
while opt!=0:
    opt=menu()
    
    if opt==1:
        regbag()
        
print("Have a nice flight :')")

