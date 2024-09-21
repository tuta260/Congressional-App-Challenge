import tkinter as tk

class AboutUsPage(tk.Frame):
    def __init__(self, master, show_homepage):
        super().__init__(master)
        self.configure(bg='grey')

        # Title
        title_label = tk.Label(self, text="About Us", font=("Arial", 24, "bold"), bg='grey', fg='black')
        title_label.pack(pady=20)

        # Login info
        self.username_display_label = tk.Label(self, text="User: Harrison", font=("Arial", 14, "bold"), bg='grey', fg='black')
        self.username_display_label.place(relx=1.0, y=20, anchor="ne", x=-20)

        # Description
        description = "This is the About Us page. Here you would typically include information about the organization or app."
        description_label = tk.Label(self, text=description, font=("Arial", 14), bg='grey', fg='black', wraplength=800)
        description_label.pack(pady=20)

        # Back button
        back_button = tk.Button(self, text="Back", command=show_homepage, font=("Arial", 12), bg="#1bc3cc", fg="black", activebackground="#139c9f", width=10, height=2)
        back_button.pack(side=tk.BOTTOM, pady=10)
