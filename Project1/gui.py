import functions
import PySimpleGUI
PySimpleGUI.theme('DarkPurple4')
label = PySimpleGUI.Text("Type in a to-do")
input_box = PySimpleGUI.InputText(tooltip="Enter todo")
add_button=PySimpleGUI.Button("Add")
edit_button = PySimpleGUI.Button("Edit")
complete_button= PySimpleGUI.Button("Button")
exit_button = PySimpleGUI.Button("Exit")
todos=functions.get_todos()

window = PySimpleGUI.Window('ToDo List', layout=[[label],[input_box, add_button],
                            [PySimpleGUI.Listbox(values=todos,font='helvetica',size=10),[edit_button],[complete_button]],
                            [exit_button]])
window.read()
window.close()
