import PySimpleGUI as sg
import pyshorteners as shrt

# The color of the GUI
sg.theme('Black')

# URL shortening python object
tiny_url = shrt.Shortener()
# URL shortening python object that requires an API key
bitly_url = shrt.Shortener(api_key='6a06ef1fcbdc2531aeff563e104fcc978163911b')

# The list of GUI elements this panel uses
layout = [  [sg.Text('Please enter a URL', font=("Arial", 11))],
            [sg.Text(size=(12, 1))],
            [sg.Input(key='INPUT')],
            [sg.Text(size=(12, 1))],
            [sg.Button('Shorten URL with Bitly')],
            [sg.Button('Shorten URL with TinyURL')],
            [sg.InputText(key='OUTPUT')],
            [sg.Button('Clear')]]

# Make the window
window = sg.Window('Url Shortener', layout)

# Event Loop to handle the buttons
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:  # Exit loop if the user presses the default close button
        break
    if event == 'Clear':  # Clears all of the fields
        window['INPUT'].update("")
        window['OUTPUT'].update("")
    if event == 'Shorten URL with TinyURL':  # Shortenes the URL using TinyURL
        short_url = tiny_url.tinyurl.short(layout[2][0].get())  # Recives the link that the user put in and shortens it
        window['OUTPUT'].update(short_url)  # Output the new shortened link
    if event == 'Shorten URL with Bitly':  # Shorten the URL using Bitly
        # Try, except and else to handle invalid url's that the user might enter
        try:
            short_url = bitly_url.bitly.short(layout[2][0].get())  # Recieves the link that the user put in and shortenes it
        except:
            window['OUTPUT'].update("Invalid URL has been entered") # To handle invalid urls that the user might input
        else:
            window['OUTPUT'].update(short_url)  # Output the new shortened link
