import os
import sys
import csv
options = ["Add task", "Delete/Complete task", "View task(s)", "Exit (Save)"]
tasks =[]
with open("tasks.csv", "r") as file:
    reader = csv.DictReader(file)
    for line in file:
        tasks.append(line)
new_tasks = []

def clear_screen():
    while True:
        clear = input("Clear screen? (Y/N) ").lower()
        if "y" in clear:
            os.system("cls")
            break

while True:
    print("-------Task Manager-------")
    for i in range(len(options)):
        print(f"{i+1}. {options[i]}")
    choice = input("Which one do you want to do? ")

    if choice == "1":
        add_task = input("What task would you like to add? ")
        tasks.append(add_task)
        new_tasks.append(add_task)
        print("Task added.")
        clear_screen()

    elif choice == "2":
        for i in range(len(tasks)):
            print(f"{i+1}. {tasks[i]}", end="")
        try:
            remove_task = int(input("Which task do you want to remove? (Index) ")) - 1
            tasks.pop(remove_task)
            new_tasks.pop(remove_task)
            print("Task removed.")
            clear_screen()
        except IndexError:
            print("Invalid index.")
            clear_screen()

    elif choice == "3":
        if len(tasks) > 0:
            for j in range(len(tasks)):
                if tasks[j].endswith("\n"):
                    print(f"{j + 1}. {tasks[j]}", end="")
                else:
                    print(f"{j + 1}. {tasks[j]}")
        else:
            print("No tasks yet.")
        clear_screen()


    elif choice == "4":
        with open("tasks.csv", "a", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=["task"])
            for i in new_tasks:
                writer.writerow({"task": i})
        sys.exit("Exited program.")

    else:
        print("Invalid choice.")
        clear_screen()