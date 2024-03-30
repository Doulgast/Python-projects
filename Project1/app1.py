while True:
    user_action=input("Choose if you want to add,show,edit,complete or exit: ")
    user_action=user_action.strip()

    match user_action:
        case 'add':
            todo = input("Enter a todo: ") + "\n"
            file = open('todos.txt' , 'r')
            todos = file.readlines()
            file.close()

            todos.append(todo)
            file=open('todos.txt', 'w')
            file.writelines(todos)
            file.close()
        case 'show':
            file = open('todos.txt', 'r')
            todos = file.readlines()
            file.close()
#meow
            for index, item in enumerate(todos):
                item=item.strip('\n')
                row = f"{index + 1}-{item}"
                print(row)
        case 'edit':
            try:
                file = open('todos.txt', 'r')
                todos = file.readlines()
                file.close()

                number = int(input("Number of the todo to edit: "))
                if number < 1 or number > len(todos):
                    print("Invalid todo number.")
                else:
                    number -= 1  # Adjusting to zero-based index
                    new_todo = input("Enter a new todo: ")
                    todos[number] = new_todo.strip() + '\n'  # Adding a newline character
                    file = open('todos.txt', 'w')
                    file.writelines(todos)
                    file.close()
                    print("Todo item updated successfully.")
            except FileNotFoundError:
                print("Error: File 'todos.txt' not found.")
            except ValueError:
                print("Error: Please enter a valid number.")
            except Exception as e:
                print("An error occurred:", e)
        case 'complete':
            try:
                file = open('todos.txt', 'r')
                todos = file.readlines()
                file.close()

                for index, item in enumerate(todos):
                    row = f"{index + 1}-{item}"
                    print(row)

                number = int(input("Number of the todo to edit: "))

                if number < 1 or number > len(todos):
                    print("Invalid todo number.")
                else:
                    number -= 1  # Adjusting to zero-based index
                    todos.pop(number)  # Remove the item at the specified index
                    file = open('todos.txt', 'w')
                    file.writelines(todos)
                    file.close()
                    print("Item removed successfully.")
            except FileNotFoundError:
                print("Error: File 'todos.txt' not found.")
            except ValueError:
                print("Error: Please enter a valid number.")
            except Exception as e:
                print("An error occurred:", e)

        case 'exit':
            break
        case whatever:
            print("You didn't give a correct input . Please try again")


print("Bye :) !")


