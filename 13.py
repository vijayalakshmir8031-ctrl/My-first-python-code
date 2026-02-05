#while loop
i = 1
while i<= 5:
    print(i)
    i += 1
sheep_count = 1
while sheep_count<= 10:
    print(f"sheep {sheep_count}")
    sheep_count += 1
#using break to exit a while loop
sheep_count = 1
while sheep_count<= 10:
    print(f"sheep {sheep_count}")
    if sheep_count == 5:
        print("thats enough counting")
        break
    sheep_count += 1   
#using continue to skip an iteration
sheep_count = 1
while sheep_count<= 10:
    if sheep_count == 5:
        sheep_count += 1
        continue
    print(f"sheep {sheep_count}")   
    sheep_count += 1
    #using while loop for user input
    pin = ""
    correct_pin = "1234"
    while pin != correct_pin:
        pin = input("enter your pin")
        if pin != correct_pin:
            print("incorrect pin. try again")
            print("pin accepted. you can proceed")