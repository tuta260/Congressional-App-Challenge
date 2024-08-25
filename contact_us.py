import tkinter as tk

class ContactUsPage(tk.Frame):
    def __init__(self, master, show_homepage):
        super().__init__(master)
        self.configure(bg='grey')

        # Title
        title_label = tk.Label(self, text="Contact Us", font=("Arial", 24, "bold"), bg='grey', fg='black')
        title_label.pack(pady=20)

        # Description
        description = "This is the Contact Us page. Include contact information or a form here for users to reach out."
        description_label = tk.Label(self, text=description, font=("Arial", 14), bg='grey', fg='black', wraplength=800)
        description_label.pack(pady=20)

        # Back button
        back_button = tk.Button(self, text="Back", command=show_homepage, font=("Arial", 12), bg="#1bc3cc", fg="black", activebackground="#139c9f", width=10, height=2)
        back_button.pack(side=tk.BOTTOM, pady=10)
