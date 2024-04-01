from functions import *
import PySimpleGUI
PySimpleGUI.theme('DarkPurple4')
label = PySimpleGUI.Text("Type in a to-do")
input_box = PySimpleGUI.InputText(tooltip="Enter todo")
add_button=PySimpleGUI.Button("Add")

window = PySimpleGUI.Window('ToDo List', layout=[[label],[input_box, add_button]])
window.read()
window.close()
