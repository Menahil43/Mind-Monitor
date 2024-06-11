import tkinter as tk
import webbrowser

def open_therapeutic_content():
    def open_article(url):
        webbrowser.open_new(url)

    # Create a new window using Tk
    window = tk.Toplevel()
    window.title("Therapeutic Content")
    window.geometry('400x650+400+100')
    window.configure(bg='#F49DA2')
    window.resizable(False, False)

    # icon
    Image_icon = tk.PhotoImage(file="images/logo.png")
    window.iconphoto(False, Image_icon)

    # top bar
    TopImage = tk.PhotoImage(file=r"images/topbar.png")
    top_label = tk.Label(window, image=TopImage)
    top_label.image = TopImage  # Keep a reference to the image
    top_label.pack()

    heading = tk.Label(window, text="Therapeutic Content", font=("Times New Roman", 24, "bold"), fg="#F5F6FA", bg="#F49DA2")
    heading.pack(pady=20)  # Adjust pady to position the label

    # Define your articles and their corresponding links
    articles = [
        {"title": "A Breath of Fresh Air", "link": "https://amiquebec.org/wp-content/uploads/2013/02/Newsletter2009Summer.pdf"},
        {"title": "Coping with Depression in Old Age", "link": "https://karger.com/dem/article/35/3-4/121/99170/Coping-and-Depression-in-Old-Age-A-Literature"},
        {"title": "Stop-Think-Relax", "link": "https://www.sciencedirect.com/science/article/abs/pii/S1077722906000654"},
        {"title": "Guidelines for Therapies", "link": "https://journals.lww.com/indianjpsychiatry/fulltext/2020/62002/Clinical_Practice_Guidelines_for_Yoga_and_Other.15.aspx"},
        {"title": "The Happiness Advantage", "link": "https://www.shawnachor.com/books/happiness-advantage/"},
        {"title": "The Mindful Way through Depression", "link": "https://www.goodreads.com/book/show/112588.The_Mindful_Way_through_Depression"},
        {"title": "The Relaxation Response", "link": "https://en.wikipedia.org/wiki/The_Relaxation_Response"},
        {"title": "The-Power-of-Now", "link": "https://www.adphc.gov.ae/-/media/Project/ADPHC/ADPHC/Books-and-Publications/The-Power-of-now-Eng.pdf"},
    ]

    # Create and display article titles as labels with "Read More" links
    for article in articles:
        # Add bullet character before the article title
        title_text = "• " + article["title"]
        title_label = tk.Label(window, text=title_text, cursor="hand2", foreground="black", bg="#F49DA2", font=("Times New Roman", 16))
        title_label.pack(anchor="w", padx=15, pady=5)
        title_label.bind("<Button-1>", lambda e, url=article["link"]: open_article(url))

    # Add label at the bottom
    bottom_label = tk.Label(window, text="Choose any of them to read", font=("Times New Roman", 14), fg="#F5F6FA", bg="#F49DA2")
    bottom_label.pack(side=tk.BOTTOM, pady=10)

    window.mainloop()
