import tkinter as tk
from tkinter import messagebox, PhotoImage
import color_game
import therapeutic_content  # Ensure this is the correct name of your module

def on_image_click(image_name):
    if image_name == "Game 1":
        color_game.open_game()
    elif image_name == "Therapeutic content":
        therapeutic_content.open_therapeutic_content()  # Call the function from your module
    else:
        messagebox.showinfo("Image Clicked", f"You clicked on {image_name}")

def create_main_window():
    # Create the main window
    window = tk.Tk()
    window.title("Mind Monitor")
    window.geometry('400x650+400+100')
    window.configure(bg='#F49DA2')
    window.resizable(0, 0)

    # icon
    Image_icon = PhotoImage(file="images/logo.png")
    window.iconphoto(False, Image_icon)

    # top bar
    TopImage = PhotoImage(file=r"images/topbar.png")
    top_label = tk.Label(window, image=TopImage)
    top_label.image = TopImage  # Keep a reference to the image
    top_label.pack()

    heading = tk.Label(window, text="Categories", font=("Times New Roman", 24, "bold"), fg="#F5F6FA", bg="#F49DA2")
    heading.pack(pady=20)  # Adjust pady to position the label

    # Create a frame for the buttons
    button_frame = tk.Frame(window, bg='#F49DA2')
    button_frame.pack(pady=20)  # Adjust pady to position the frame

    # Load images
    image1 = PhotoImage(file="images/game1.png")
    image2 = PhotoImage(file="images/thera.png")

    # Create image buttons and place them in the frame using grid
    button1 = tk.Button(button_frame, image=image1, command=lambda: on_image_click("Game 1"))
    button2 = tk.Button(button_frame, image=image2, command=lambda: on_image_click("Therapeutic content"))

    button1.grid(row=0, column=0, padx=20, pady=10)
    button2.grid(row=1, column=0, padx=20, pady=10)

    window.mainloop()

# Ensure create_main_window is not called when the module is imported
if __name__ == "__main__":
    create_main_window()
