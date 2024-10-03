import tkinter as tk
from PIL import Image, ImageTk

Aarushtext= "Aarush is a junior at Albuquerque Academy. He has a deep love of civics, being a former Congressional Intern for the office of Congresswoman Melanie Stansbury, a Youth and Government Outstanding Delegate, and a captain of his school debate team. Outside of school, he loves playing chess, hiking with his friends, and playing video games."
Harrisontext="Harrison is a junior at Albuquerque Academy. He has been programming for most of his life, and thoroughly enjoys learning and understanding abstract numeric concepts, having placed second in the 2024 New Mexico Supercomputing challenge. He is also a nationally ranked fencer and a qualifier to International Career Development Conference. "

class AboutUsPage(tk.Frame):
    def __init__(self, master, show_homepage, ID):
        super().__init__(master)
        self.configure(bg='grey')

        # Title
        title_label = tk.Label(self, text="About Us", font=("Arial", 24, "bold"), bg='grey', fg='black')
        title_label.pack(pady=20)

        # Login info
        self.username_display_label = tk.Label(self, text=f"User: {ID}", font=("Arial", 14, "bold"), bg='grey', fg='black')
        self.username_display_label.place(relx=1.0, y=20, anchor="ne", x=-20)

        # Frame for content (including images and text)
        content_frame = tk.Frame(self, bg='grey')
        content_frame.pack(pady=20, padx=20, anchor='w')

        # Load and resize the first image (Aarush's image)
        img1 = Image.open("aarush_image.jpg")  # Path to the first image
        img1 = img1.resize((400, 300), Image.ANTIALIAS)  # Increased image size
        img1 = ImageTk.PhotoImage(img1)
        img1_label = tk.Label(content_frame, image=img1, bg='grey')
        img1_label.image = img1  # Keep a reference to avoid garbage collection
        img1_label.grid(row=0, column=0, padx=20, pady=10)

        # Load and resize the second image (Harrison's image)
        img2 = Image.open("harrison_image.jpg")  # Path to the second image
        img2 = img2.resize((400, 300), Image.ANTIALIAS)  # Same size as the first image
        img2 = ImageTk.PhotoImage(img2)
        img2_label = tk.Label(content_frame, image=img2, bg='grey')
        img2_label.image = img2  # Keep a reference to avoid garbage collection
        img2_label.grid(row=1, column=0, padx=20, pady=10)

        # Aarush Tutiki heading and blurb
        aarush_label = tk.Label(content_frame, text="Aarush Tutiki", font=("Arial", 18, "bold"), bg='grey', fg='black')
        aarush_label.grid(row=0, column=1, padx=10, pady=(10, 0), sticky='nw')  # Align top with image

        aarush_blurb = tk.Label(content_frame, text=Aarushtext, 
                                font=("Arial", 14), bg='grey', fg='black', wraplength=500, justify='left')
        aarush_blurb.grid(row=0, column=1, padx=10, pady=(40, 10), sticky='nw')

        # Harrison Schiek heading and blurb
        harrison_label = tk.Label(content_frame, text="Harrison Schiek", font=("Arial", 18, "bold"), bg='grey', fg='black')
        harrison_label.grid(row=1, column=1, padx=10, pady=(10, 0), sticky='nw')  # Align top with image

        harrison_blurb = tk.Label(content_frame, text=Harrisontext, 
                                  font=("Arial", 14), bg='grey', fg='black', wraplength=500, justify='left')
        harrison_blurb.grid(row=1, column=1, padx=10, pady=(40, 10), sticky='nw')

        # Back button
        back_button = tk.Button(self, text="Back", command=show_homepage, font=("Arial", 12), bg="#1bc3cc", fg="black", activebackground="#139c9f", width=10, height=2)
        back_button.pack(side=tk.BOTTOM, pady=10)