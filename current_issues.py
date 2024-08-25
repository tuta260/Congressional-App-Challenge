import tkinter as tk

class CurrentIssuesPage(tk.Frame):
    def __init__(self, master, show_homepage):
        super().__init__(master)
        self.configure(bg='light blue')

        title_label = tk.Label(self, text="Current Issues", font=("Arial", 24, "bold"), bg='light blue')
        title_label.pack(pady=20)

        back_button = tk.Button(self, text="Back", command=show_homepage, font=("Arial", 14), width=10, height=1)
        back_button.pack(side=tk.BOTTOM, anchor=tk.SE, padx=20, pady=20)