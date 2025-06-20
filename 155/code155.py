# https://img-c.udemycdn.com/redactor/raw/article_lecture/2022-06-17_16-00-50-950c6e645d507334f9ffc30f8ea184a0.png

import FreeSimpleGUI as sg

layout = [
    [sg.Text("Enter feet:"), sg.Input()],    
    [sg.Text("Enter inches"), sg.Input()],
    [sg.Button("Convert")]
]

window = sg.Window("Convertor", layout)
window.read()
window.close()
#