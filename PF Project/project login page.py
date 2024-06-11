import tkinter as tk
from tkinter import messagebox, PhotoImage
import openpyxl
from openpyxl import Workbook
import os
import main_window  # Ensure this is the correct name of your module

# Function to store data in Excel file
def store_data(username):
    file_path = 'user_data.xlsx'
    
    try:
        if not os.path.exists(file_path):
            workbook = Workbook()
            sheet = workbook.active
            sheet.title = 'User Data'
            sheet.append(["Username"])  # Add headers
            workbook.save(file_path)
        
        workbook = openpyxl.load_workbook(file_path)
        sheet = workbook.active
        
        sheet.append([username])
        
        workbook.save(file_path)
        
        print("Data stored successfully.")
    except Exception as e:
        print(f"Error storing data: {e}")

def login():
    input_username = username_entry.get()

    
    if input_username:
        store_data(input_username)
        messagebox.showinfo(title="Login Success", message="You successfully logged in.")
        window.destroy()  # Close the login window
        main_window.create_main_window()  # Open the main window
    else:
        messagebox.showerror(title="Error", message="Please enter username.")

# Create the login window
window = tk.Tk()
window.title("Login")
window.geometry('400x650+400+100')
window.configure(bg='#F49DA2')
window.resizable(False, False)

# Icon
try:
    Image_icon = PhotoImage(file="images/logo.png")
    window.iconphoto(False, Image_icon)
except Exception as e:
    print(f"Error loading icon: {e}")

# Create a frame to contain the widgets
frame = tk.Frame(bg='#F49DA2')

# Creating widgets
login_label = tk.Label(
    frame, text="Login", bg='#F49DA2', fg="#F5F6FA", font=("Times New Roman", 30))
username_label = tk.Label(
    frame, text="Username", bg='#F49DA2', fg="#F5F6FA", font=("Arial", 16))
username_entry = tk.Entry(frame, font=("Arial", 16))

# Function to create a rounded rectangle on the Canvas
def round_rectangle(x1, y1, x2, y2, radius=25, **kwargs):
    points = [x1 + radius, y1,
              x1 + radius, y1,
              x2 - radius, y1,
              x2 - radius, y1,
              x2, y1,
              x2, y1 + radius,
              x2, y1 + radius,
              x2, y2 - radius,
              x2, y2 - radius,
              x2, y2,
              x2 - radius, y2,
              x2 - radius, y2,
              x1 + radius, y2,
              x1 + radius, y2,
              x1, y2,
              x1, y2 - radius,
              x1, y2 - radius,
              x1, y1 + radius,
              x1, y1 + radius,
              x1, y1]
    return button_canvas.create_polygon(points, **kwargs, smooth=True)

# Create the canvas for the rounded rectangle button
button_canvas = tk.Canvas(frame, width=200, height=70, bg='#F49DA2', highlightthickness=0)
round_rectangle(10, 10, 190, 60, radius=20, fill="#F5F6FA")
button_canvas.create_text(100, 35, text="Login", fill="#F49DA2", font=("Times New Roman", 22))

# Bind the login function to the canvas button
button_canvas.bind("<Button-1>", lambda event: login())

# Placing widgets on the screen
login_label.grid(row=1, column=0, columnspan=2, sticky="news", pady=60)
username_label.grid(row=2, column=0)
username_entry.grid(row=2, column=1, pady=40)
button_canvas.grid(row=4, column=0, columnspan=2, pady=60)

# Add the frame to the window
frame.pack()

# Run the application
window.mainloop()
