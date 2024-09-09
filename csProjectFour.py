# organizing a holiday party for your family and need to keep track of the guest list and their dietary preferences
# 1. Initialize an empty guest list dictionary
# 2. add guests to the list along with their dietary preferences (vegetarian, vegan, gluten-free, carnivore, etc)
# 3. Allow the user to check if a specific person is on the guest list and display their dietary preference if they are
# 4. Display the entire guest list with their dietary preferences
# 5. Allow the user to remove a guest from the list

print("""
Welcome to the Party Manager App!!!

1.) Add a guest to the list
2.) Check a guest's dietary preference
3.) Display the guest list
4.) Remove a guest from the list
5.) Exit """)

guestList = []

while True:
    print("")
    request = int(input("Enter (1,2,3,4,or 5) Here: "))
    if request == 1:
        name = input("Type the name of your guest here: ")
        diet = input("Type their diet preferences here (vegetarian, vegan, gluten-free, carnivore, etc): ")
        guestList.append([name, diet])
        print(f"{name} had been added to the list")
    elif request == 2:
        checkName = input("Who's diet would you like to check?: ")
        inList = False
        for i in range(len(guestList)):
            if checkName in guestList[i][0]:
                inList = True
                print(f"{checkName}'s diet is {guestList[i][1]}")
                break
        if not inList:
            print(f"{checkName} was not on the guest list")
    elif request == 3:
        if len(guestList) == 1:
            print(f"There is 1 guest on the list so far!")
        else:
            print(f"There are {len(guestList)} guests on the list so far")
        for i in range(len(guestList)):
            print(f"{i+1}.) {guestList[i][0]} (Dietary Preference: {guestList[i][1]})")
    elif request == 4:
        remove = input("Who do you want to remove: ")
        inList = False
        for i in range(len(guestList)):
            if remove in guestList[i][0]:
                del guestList[i]
                inList = True
                print(f"{remove} was removed from the guest list")
                break
        if not inList:
            print(f"{remove} was not on the guest list")
    elif request == 5:
        print("(You completed the list!)")
        break
    else:
        print("You did not input the correct number!")
