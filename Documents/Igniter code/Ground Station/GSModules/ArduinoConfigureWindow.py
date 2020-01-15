import PySimpleGUI as sg

configureWindow = sg.Window('Arduino Configuration', resizable=True)

diagram = sg.Image('ArduinoUnoImg1.png', key='DIAGRAM')

left_col_buttons = [[sg.Button("Pin A" + str(0), button_color=('White', 'Red'), key="Pin A" + str(0))],
                    [sg.Button("Pin A" + str(1), button_color=('White', 'Red'), key="Pin A" + str(1))],
                    [sg.Button("Pin A" + str(2), button_color=('White', 'Red'), key="Pin A" + str(2))],
                    [sg.Button("Pin A" + str(3), button_color=('White', 'Red'), key="Pin A" + str(3))],
                    [sg.Button("Pin A" + str(4), button_color=('White', 'Red'), key="Pin A" + str(4))],
                    [sg.Button("Pin A" + str(5), button_color=('White', 'Red'), key="Pin A" + str(5))],]

right_col_buttons = [[sg.Button("Pin " + str(13), button_color=('White', 'Red'), key="Pin " + str(13))],
                    [sg.Button("Pin " + str(12), button_color=('White', 'Red'), key="Pin " + str(12))],
                    [sg.Button("Pin " + str(11), button_color=('White', 'Red'), key="Pin " + str(11))],
                    [sg.Button("Pin " + str(10), button_color=('White', 'Red'), key="Pin " + str(10))],
                    [sg.Button("Pin " + str(9), button_color=('White', 'Red'), key="Pin " + str(9))],
                    [sg.Button("Pin " + str(8), button_color=('White', 'Red'), key="Pin " + str(8))],
                    [sg.Button("Pin " + str(7), button_color=('White', 'Red'), key="Pin " + str(7))],
                    [sg.Button("Pin " + str(6), button_color=('White', 'Red'), key="Pin " + str(6))],
                    [sg.Button("Pin " + str(5), button_color=('White', 'Red'), key="Pin " + str(5))],
                    [sg.Button("Pin " + str(4), button_color=('White', 'Red'), key="Pin " + str(4))],
                    [sg.Button("Pin " + str(3), button_color=('White', 'Red'), key="Pin " + str(3))],
                    [sg.Button("Pin " + str(2), button_color=('White', 'Red'), key="Pin " + str(2))],
                    [sg.Button("Pin " + str(1), button_color=('White', 'Red'), key="Pin " + str(1))],
                    [sg.Button("Pin " + str(0), button_color=('White', 'Red'), key="Pin " + str(0))],]

layout = [[sg.Column(left_col_buttons), diagram, sg.Column(right_col_buttons)]]

configureWindow = sg.Window('Arduino Configuration', layout, grab_anywhere=True, resizable=True)
event, values = configureWindow.read()
configureWindow.Close()