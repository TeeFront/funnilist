import time

some = [""]
some = [item.lower() for item in some] # make all items lowercase(for the computer)
triggered = False # for if you did something wrong


for i in some:
    print(i)

print("Welcome to the funnilist")
print("Write 'show' if you want to see how the list is so far")
print("Write 'add' if you want to add something to your list")
print("Write 'delete' if you want to delete something from your list")

while True:
    choice = input("> ").strip().lower()
    if choice == "show":
        for i in some:
            print(i)
    elif choice == "add":
        item = input("What do you want to add? ")
        if item == "":
            print("That's empty.")
            triggered = True
        else:
            triggered = False
        if not triggered:
            some.append(item)
            print("Item added succesfully!")
    elif choice == "delete":
        item2 = input("What do you want to delete? ").strip().lower()
        try: 
            some.remove(item2)
            print("Item deleted succesfully")
        except:
                print("Item failed to delete")
    else:
        print("Unknown command.")
