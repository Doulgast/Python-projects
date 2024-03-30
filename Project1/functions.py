
def get_todos(filepath='todos.txt'):
    """"Read a file and return the string with the read file"""
    with open(filepath, 'r') as file:
        todos = file.readlines()
    return todos
print("Hello dear :).")

def write_todos(todos_arg,filepath='todos.txt'):
    """"write on the file specified"""
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)

def show_list(todos):
    """"show the list of ToDos"""
    for index, item in enumerate(todos):
        item = item.strip('\n')
        row = f"{index + 1}-{item}"
        print(row)