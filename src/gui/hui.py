import tkinter as tk
#get manual_input from Manualinput.py
from .pages.manualInput import manual_input

window = tk.Tk()
window.title('AWP')
window.attributes('-fullscreen',True)
width = window.winfo_screenwidth()
height = window.winfo_screenheight()

# Setting the background color
canvas = tk.Canvas(window, width = width, height = height, bg ='#545454')
canvas.place(relx = 0.5, rely = 0.5, anchor = 'center')

# Adding the font
#pyglet.font.add_file('src\gui\fonts\Montserrat.ttf')

# Creating the main text
label = tk.Label(window, text='AUTOMATED FOREST', bg='#545454', fg='white', font=('Montserrat', 30))
label.place(relx = 0.25,rely = 0.47, anchor = 'center')
label = tk.Label(window, text='FIRE PREDICTION', bg='#545454', fg='white',  font=('Montserrat', 30))
label.place(relx = 0.25,rely = 0.53, anchor = 'center')

# Creating the Rectangle
canvas = tk.Canvas(window, width = width/2, height = height, bg ='#323466')
canvas.place(relx = 0.75, rely = 0.5, anchor = 'center')

# Creating buttons
button1 = tk.Button(window, text='MANUAL PREDICTION', font=('Montserrat', 20), borderwidth=0, command = manual_input)
button1.place(relx = 0.76, rely = 0.32, anchor = 'center')
button2 = tk.Button(window, text='AUTOMATED PREDICTION', font=('Montserrat', 20), borderwidth=0, command = window.destroy)
button2.place(relx = 0.76, rely = 0.63, anchor = 'center')

window.mainloop()
