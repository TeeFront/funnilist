import time
from rich import print # for colors

some = [""]
some = [item.lower() for item in some] # make all items lowercase(for the computer)
triggered = False # for if you did something wrong


for i in some:
    print(i)

print("Welcome to the [yellow]funnilist[/yellow]")
print("Write [bright_yellow]'show'[/bright_yellow] if you want to see how the list is so far")
print("Write [green]'add'[/green] if you want to add something to your list")
print("Write [red3]'delete'[/red3] if you want to delete something from your list")

while True:
    choice = input("> ").strip().lower()
    if choice == "show":
        for i in some:
            print(i)
    elif choice == "add":
        item = input("What do you want to add? ")
        if item == "":
            print("[red3]That's empty.[/red3]")
            triggered = True
        else:
            triggered = False
        if not triggered:
            some.append(item)
            print("[sea_green3]Item added succesfully![/sea_green3]")
    elif choice == "delete":
        item2 = input("What do you want to delete? ").strip().lower()
        try: 
            some.remove(item2)
            print("[dark_red]Item deleted succesfully[/dark_red]")
        except:
                print("Item failed to delete")
    else:
        print("[grey3]Unknown command.[/grey3]")