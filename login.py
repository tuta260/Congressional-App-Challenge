import tkinter as tk

class LoginPage(tk.Frame):
    def __init__(self, master, show_homepage):
        super().__init__(master)
        self.configure(bg='grey')

        # Title centered
        title_label = tk.Label(self, text="Login", font=("Arial", 24, "bold"), bg='grey', fg='black')
        title_label.pack(pady=20)

        # Username label and entry
        username_label = tk.Label(self, text="Username", font=("Arial", 14), bg='grey', fg='black')
        username_label.pack(pady=10)
        self.username_entry = tk.Entry(self, font=("Arial", 14), width=30)
        self.username_entry.pack(pady=5)

        # Password label and entry
        password_label = tk.Label(self, text="Password", font=("Arial", 14), bg='grey', fg='black')
        password_label.pack(pady=10)
        self.password_entry = tk.Entry(self, font=("Arial", 14), width=30, show="*")  # show="*" hides the password
        self.password_entry.pack(pady=5)

        # Submit button
        submit_button = tk.Button(self, text="Submit", font=("Arial", 12), bg="#1bc3cc", fg="black", activebackground="#139c9f", activeforeground="black", width=10, height=2, command=self.on_submit)
        submit_button.pack(pady=20)

        # Success message label (initially empty)
        self.success_label = tk.Label(self, text="", font=("Arial", 14), bg='grey', fg='black')
        self.success_label.pack(pady=10)

        # Username display label (initially empty)
        self.username_display_label = tk.Label(self, text="", font=("Arial", 14, "bold"), bg='grey', fg='black')
        self.username_display_label.place(relx=1.0, y=20, anchor="ne", x=-20)

        # Back button
        back_button = tk.Button(self, text="Back", command=show_homepage, font=("Arial", 12), bg="#1bc3cc", fg="black", activebackground="#139c9f", activeforeground="black", width=10, height=2)
        back_button.pack(side=tk.BOTTOM, pady=10)

    def on_submit(self):
        # Display the success message
        self.success_label.config(text="Successfully Logged in")

        # Get the username from the entry field and display it on the top right in bold
        username = self.username_entry.get()
        self.username_display_label.config(text=f"User: {username}")

