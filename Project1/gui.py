from _ast import match_case

import functions
import PySimpleGUI
PySimpleGUI.theme('DarkPurple4')
label = PySimpleGUI.Text("Type in a to-do")
input_box = PySimpleGUI.InputText(tooltip="Enter todo", key='todo')
add_button=PySimpleGUI.Button("Add")
edit_button = PySimpleGUI.Button("Edit")
complete_button= PySimpleGUI.Button("Button")
exit_button = PySimpleGUI.Button("Exit")
todos=functions.get_todos()

window = PySimpleGUI.Window('ToDo List', layout=[[label],[input_box, add_button],
                            [PySimpleGUI.Listbox(values=todos,font='helvetica',size=10),[edit_button],[complete_button]],
                            [exit_button]])

while True:
event,values=window.read()
print(event)
print(values)
match event:
    case 'Add':
        todos=functions.get_todos();
        
window.close()
