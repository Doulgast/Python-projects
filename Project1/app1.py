from functions import *
import time

now=time.strftime("%b %d, %Y %H:%M:%S")
print("It is ",now)
""""While loop with out main operations"""""
# Main loop
while True:
    # User input
    user_action = input("Choose if you want to add, show, edit, complete, or exit: ")
    user_action = user_action.strip()

    # 'add' action
    if user_action.startswith('add'):
        todo = user_action[4:]
        todos = get_todos()
        if todo != '':
            todos.append(todo + '\n')
            write_todos(todos)

    # 'show' action
    elif user_action.startswith('show'):
        todos = get_todos()
        show_list(todos)

    # 'edit' action
    elif user_action.startswith('edit'):
        try:
            todos = get_todos()
            show_list(todos)

            number = int(input("Number of the todo to edit: "))
            if number < 1 or number > len(todos):
                print("Invalid todo number.")
            else:
                number -= 1  # Adjusting to zero-based index
                new_todo = input("Enter a new todo: ")
                todos[number] = new_todo.strip() + '\n'  # Adding a newline character
                write_todos(todos)
                print("Todo item updated successfully.")
        except FileNotFoundError:
            print("Error: File not found.")
        except ValueError:
            print("Error: Please enter a valid number.")
        except Exception as e:
            print("An error occurred:", e)

    # 'complete' action
    elif user_action.startswith('complete'):
        try:
            todos = get_todos()
            show_list(todos)

            number = int(input("Number of the todo to mark as completed: "))

            if number < 1 or number > len(todos):
                print("Invalid todo number.")
            else:
                number -= 1  # Adjusting to zero-based index
                todos.pop(number)  # Remove the item at the specified index
                write_todos(todos)

                print("Item removed successfully.")
        except FileNotFoundError:
            print("Error: File not found.")
        except ValueError:
            print("Error: Please enter a valid number.")
        except Exception as e:
            print("An error occurred:", e)

    # 'exit' action
    elif user_action.startswith('exit'):
        break

    # Invalid command
    else:
        print("Command is not valid")

print("Bye :) !")