from _ast import match_case

import functions
import PySimpleGUI
PySimpleGUI.theme('DarkPurple4')
label = PySimpleGUI.Text("Type in a to-do")
input_box = PySimpleGUI.InputText(tooltip="Enter todo", key='todo')
add_button=PySimpleGUI.Button("Add")
edit_button = PySimpleGUI.Button("Edit")
complete_button= PySimpleGUI.Button("Complete")
exit_button = PySimpleGUI.Button("Exit")
list_box=PySimpleGUI.Listbox(values=functions.get_todos(),key='todos',enable_events=True,size=[45,10])
window = PySimpleGUI.Window('ToDo List',
                            layout=[[label],[input_box, add_button],
                            [list_box , edit_button,complete_button],
                            [exit_button]],
                            font=('helvetica',20))

while True:
    event , values=window.read()
    match event:
        case "Add":
          if(values['todo']!=""):
            todos=functions.get_todos()
            new_todo=values['todo']+ "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
            window['todo'].update(value='')
        case "Edit":
          try:
            todo_to_edit = values['todos'][0]
            new_todo = values['todo'] + "\n"
            todos=functions.get_todos()
            index=todos.index(todo_to_edit)
            todos[index]=new_todo
            functions.write_todos(todos)
            window['todos'].update(values=todos)
          except IndexError:
              PySimpleGUI.popup("Please select an item first")
        case 'todos':
            window['todo'].update(value=values['todos'][0])
        case 'Complete':
          try:
            todo_to_complete=values['todos'][0]
            todos = functions.get_todos()
            todos.remove(todo_to_complete)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
            window['todo'].update(value='')
          except IndexError:
              PySimpleGUI.popup("Please select an item first")
        case 'Exit':
            break;

        case PySimpleGUI.WINDOW_CLOSED:
            break;

window.close()
