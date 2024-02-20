class ToDoList:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)
        print(f"Item '{item}' added to the to-do list.")

    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)
            print(f"Item '{item}' removed from the to-do list.")
        else:
            print(f"Item '{item}' not found in the to-do list.")

    def view_list(self):
        if self.items:
            print("To-Do List:")
            for idx, item in enumerate(self.items, start=1):
                print(f"{idx}. {item}")
        else:
            print("To-Do List is empty.")

if __name__ == "__main__":
    todo_list = ToDoList()

    while True:
        print("\n1. Add Item\n2. Remove Item\n3. View List\n4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            item = input("Enter the item to add: ")
            todo_list.add_item(item)
        elif choice == '2':
            item = input("Enter the item to remove: ")
            todo_list.remove_item(item)
        elif choice == '3':
            todo_list.view_list()
        elif choice == '4':
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please enter a valid option.")
