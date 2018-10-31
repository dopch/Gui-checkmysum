#!/usr/bin/python3.6
## python3.6 Gui-checkmysum.py
##
import PySimpleGUI as sg
import subprocess


def result_report(result: str):
    if result == "Checksum MATCH\n":
        sg.Popup('Gui-checkmysum !','CHECKSUM MATCH', background_color='green')
    elif result == "Checksum DOEST MATCH DROP THIS FILE !\n":
        sg.Popup('Gui-checkmysum !','CHECKSUM DOESNT MATCH DROP THE FILE', background_color='red')


def main():
    MainLayout = [[sg.Text('Original checksum')],
                  [sg.InputText()],
                  [sg.Text('Path to file')],
                  [sg.Input(), sg.FileBrowse()],
                  [sg.Text('Hash_algorithm')],
                  [sg.InputCombo(['md5', 'sha1', 'sha256', 'sha512'], size=(20, 5))],
                  [sg.Submit(), sg.Exit()]]
    window = sg.Window('Gui-checkmysum').Layout(MainLayout)
    while True:
        event, (oc, file, algo) = window.Read()
        if event is None or event == 'Exit':
            break
        elif not oc or not file or not algo:
            sg.Popup('Gui-checkmysum !', 'Checksum validation tool \nUsage: checkmysum.py [-h] Original_checksum Your_file Hash_algorithm')
            break
        result = subprocess.check_output(["./checkmysum.py", oc, file, algo])
        result = result.decode("utf-8")
        result_report(result)


if __name__ == '__main__':
    main()