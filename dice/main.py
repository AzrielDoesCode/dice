import tkinter as tk 
from PIL import Image, ImageTk
import random 

window = tk.Tk()
window.geometry("500x350")
window.title("Dice Roll Sim")

# Title and Subtitle
title_label = tk.Label(window, text="Dice Roll", font=("Helvetica", 24, "bold"), bg='white', fg='black')
title_label.place(x=180, y=10)

subtitle_label = tk.Label(window, text="Simulator", font=("Helvetica", 14), bg='white', fg='black')
subtitle_label.place(x=210, y=50)

dice = ["1.png", "2.png", "3.png", "4.png", "5.png", "6.png"]

# Define the desired size for the dice images
image_size = (100, 100)  # Width, Height

# Load and resize the images
image1 = ImageTk.PhotoImage(Image.open(random.choice(dice)).resize(image_size)) 
image2 = ImageTk.PhotoImage(Image.open(random.choice(dice)).resize(image_size))

label1 = tk.Label(window, image=image1)
label2 = tk.Label(window, image=image2)

label1.image = image1
label2.image = image2

# Place the dice images side by side with a small gap   
label1.place(x=150, y=150)
label2.place(x=260, y=150)

def droll():
    image1 = ImageTk.PhotoImage(Image.open(random.choice(dice)).resize(image_size))
    label1.configure(image=image1)
    label1.image = image1

    image2 = ImageTk.PhotoImage(Image.open(random.choice(dice)).resize(image_size))
    label2.configure(image=image2)
    label2.image = image2
    
    # Hide the button
    button_roll.place_forget()
    
    # Wait for 3 seconds
    window.after(3000, lambda: button_roll.place(x=200, y=300))

# Dark Mode         
def switch_mode():
    if window.cget('bg') == 'white':
        window.configure(bg='black')
        title_label.configure(bg='black', fg='white')
        subtitle_label.configure(bg='black', fg='white')
        button.configure(bg='white', fg='black', text="LIGHT MODE")
        button_roll.configure(bg='white', fg='black')
    else:
        window.configure(bg='white')
        title_label.configure(bg='white', fg='black')
        subtitle_label.configure(bg='white', fg='black')
        button.configure(bg='black', fg='green', text="DARK MODE")
        button_roll.configure(bg='black', fg='green')

button_roll = tk.Button(window, text="ROLL IT", bg="black", fg="green", command=droll)
button_roll.place(x=200, y=300)

button = tk.Button(window, text="DARK MODE", bg="black", fg="green", command=switch_mode)
button.place(x=350, y=300)

window.mainloop()