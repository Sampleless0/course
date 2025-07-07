# list of captains
captains = [
    #{"captain": "", "starship": ""}
]

# look up function
def lookup():
    
    # check for captains
    if captains:
        
        # check if search contains captains name
        choice = input("Search for Captain: ")
        for captain in captains:
            if captain["captain"] == choice:
                print(f"Captain: {captain["captain"]}, Starship: {captain['starship']}")
            else:
                print("Captain not found")
    else:
        print("No Captains assigned")


# add function
def add():
    
    # input name for new captain
    name = input("Captain: ")

    # check if captain is alr inside
    for captain in captains:
        if captain["captain"] == name:
            print("Captain already has an assigned starship")
            break
    
    # if captain is not inside
    else:
        starship = input("Starship: ")
        captains.append({"captain": name, "starship": starship})

def change():
    # check if captains have assigned starships
    if captains:
        
        # search for specified captain
        name = input("Captain: ")

        for captain in captains:
            if captain["captain"] == name:
                # change starship name
                newStarship = input("New Starship: ")
                captain["starship"] = newStarship
                break
        else:
            print("captain not found")
    else:
        print("no captains assigned")



def viewall():
    # check if captains are in list
    if captains:
        # print captain and starship
        for captain in captains:
            print(f"Captain: {captain["captain"]}, Starship: {captain["starship"]}")
    else:
        print("no captains assigned")




def menu():
    while True:
        # menu
        print(f"\n\ncaptains and starships\n{'-'*20}\n1. look up a starship\n2. add a new starship\n3. change a starship\n4. view all captains and starships assigned\n5. quit the program")
        
        # select option
        try:
            selection = int(input("Select an option: "))
        except Exception:
            print("Invalid selection")
            continue


        # run a function based on option selected
        if selection == 1:
            lookup()
        elif selection == 2:
            add()
        elif selection == 3:
            change()
        elif selection == 4:
            viewall()
        elif selection == 5:
            print("exiting...")
            break
        else:
            print("Invalid selection")
            continue

menu()
