import PySimpleGUI as sg

sg.theme('LightGrey1')

# Layout da calculadora
layout = [
    [sg.Input(size=(18, 1), key="-DISPLAY-", justification="right", font=("Arial", 22))],
    [sg.Button("C", key="C", size=(5, 2), font=("Arial", 14), button_color=("white", "orange")), sg.Button("DEL", key="DEL", size=(5, 2), font=("Arial", 14)), sg.Button("%",             key="%", size=(5, 2), font=("Arial", 14)), sg.Button("/", key="/", size=(5, 2), font=("Arial", 14))],
    [sg.Button("7", key="7", size=(5, 2), font=("Arial", 14)), sg.Button("8", key="8", size=(5, 2), font=("Arial", 14)), sg.Button("9", key="9", size=(5, 2), font=("Arial", 14)),        sg.Button("*", key="*", size=(5, 2), font=("Arial", 14))],
    [sg.Button("4", key="4", size=(5, 2), font=("Arial", 14)), sg.Button("5", key="5", size=(5, 2), font=("Arial", 14)), sg.Button("6", key="6", size=(5, 2), font=("Arial", 14)),        sg.Button("-", key="-", size=(5, 2), font=("Arial", 14))],
    [sg.Button("1", key="1", size=(5, 2), font=("Arial", 14)), sg.Button("2", key="2", size=(5, 2), font=("Arial", 14)), sg.Button("3", key="3", size=(5, 2), font=("Arial", 14)),        sg.Button("+", key="+", size=(5, 2), font=("Arial", 14))],
    [sg.Button(".", key=".", size=(5, 2), font=("Arial", 14)), sg.Button("0", key="0", size=(5, 2), font=("Arial", 14)), sg.Button("=", key="=", size=(12, 2), font=("Arial", 14))]
]

# Config. Janela
window = sg.Window("Calculadora", layout)

# Loop para processar os eventos
expression = ""
last_number_has_decimal = False
while True:
    event, values = window.read(timeout=0)
    if event == sg.WINDOW_CLOSED:
        break
    elif event in "1234567890":
        expression += event
        window["-DISPLAY-"].update(expression)
    elif event == ".":
        if not last_number_has_decimal:
            expression += "."
            window["-DISPLAY-"].update(expression)
            last_number_has_decimal = True
    elif event in "+-*/":
        expression += " " + event + " "
        window["-DISPLAY-"].update(expression)
        last_number_has_decimal = False
    elif event == "%":
        try:
            result = eval(expression) / 100
            window["-DISPLAY-"].update(result)
            expression = str(result)
        except:
            window["-DISPLAY-"].update("Erro")
            expression = ""
        last_number_has_decimal = False
    elif event == "=":
        try:
            result = eval(expression)
            window["-DISPLAY-"].update(result)
            expression = str(result)
        except:
            window["-DISPLAY-"].update("Erro")
            expression = ""
        last_number_has_decimal = False
    elif event == "C":
        window["-DISPLAY-"].update("")
        expression = ""
        last_number_has_decimal = False
    elif event == "DEL":
        if expression:
            expression = expression[:-1]
            window["-DISPLAY-"].update(expression)
            if expression and expression[-1] == ".":
                last_number_has_decimal = True
            else:
                last_number_has_decimal = False

# Quit janela
window.close()
