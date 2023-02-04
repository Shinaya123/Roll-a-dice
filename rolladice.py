import random
response = "y"
while(response == "y"):
    yes_or_no = input("Press Y to Roll the dice again and press N to exit: ")
    response = yes_or_no.lower()
    if(response == "y"):
        random_number = random.randint(1, 6)
        if(random_number == 1):
            print("[- - -]")
            print("[     ]")
            print("[  0  ]")
            print("[     ]")
            print("[- - -]")
        if(random_number == 2):
            print("[- - -]")
            print("[     ]")
            print("[0   0]")
            print("[     ]")
            print("[- - -]")
        if(random_number == 3):
            print("[- - -]")
            print("[0    ]")
            print("[  0  ]")
            print("[    0]")
            print("[- - -]")
        if(random_number == 4):
            print("[- - -]")
            print("[0   0]")
            print("[     ]")
            print("[0   0]")
            print("[- - -]")
        if(random_number == 5):
            print("[- - -]")
            print("[0   0]")
            print("[  0  ]")
            print("[0   0]")
            print("[- - -]")
        if(random_number == 6):
            print("[- - -]")
            print("[0   0]")
            print("[0   0]")
            print("[0   0]")
            print("[- - -]")                    
    else:
        print("The End :)")    
