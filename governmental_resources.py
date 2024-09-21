import tkinter as tk
from tkinter import ttk

class GovernmentalResourcesPage(tk.Frame):
    def __init__(self, master, show_homepage):
        super().__init__(master)
        self.configure(bg='grey')  # Set the background color to grey

        # Title
        title_label = tk.Label(self, text="Governmental Resources", font=("Arial", 24, "bold"), bg='grey', fg='black')
        title_label.pack(pady=20)

        # Login info
        self.username_display_label = tk.Label(self, text="User: Harrison", font=("Arial", 14, "bold"), bg='grey', fg='black')
        self.username_display_label.place(relx=1.0, y=20, anchor="ne", x=-20)

        # Create a PanedWindow widget to manage vertical layout
        paned_window = ttk.PanedWindow(self, orient=tk.HORIZONTAL)
        paned_window.pack(expand=True, pady=10, padx=10, fill=tk.BOTH)

        # Create a Notebook widget (tabbed interface)
        notebook = ttk.Notebook(paned_window)
        paned_window.add(notebook, weight=1)

        # Tab 1: Local Resources
        local_frame = ttk.Frame(notebook)
        local_text = "Information and links to local governmental resources."
        tk.Label(local_frame, text=local_text, font=("Arial", 14), wraplength=600, justify="left").pack(pady=10)
        notebook.add(local_frame, text="Local Resources")

        # Tab 2: State Resources
        state_frame = ttk.Frame(notebook)
        state_text = "Information and links to state governmental resources."
        tk.Label(state_frame, text=state_text, font=("Arial", 14), wraplength=600, justify="left").pack(pady=10)
        notebook.add(state_frame, text="State Resources")

        # Tab 3: Federal Resources
        federal_frame = ttk.Frame(notebook)
        federal_text = "Information and links to federal governmental resources."
        tk.Label(federal_frame, text=federal_text, font=("Arial", 14), wraplength=600, justify="left").pack(pady=10)
        notebook.add(federal_frame, text="Federal Resources")

        # Back button with the same style as the About Us button on the home page
        back_button_style = {
            "font": ("Arial", 12),
            "bg": "#1bc3cc",
            "fg": "black",
            "activebackground": "#139c9f",
            "activeforeground": "black",
            "width": 10,
            "height": 2,
            "bd": 0,
            "highlightthickness": 0,
        }

        back_button = tk.Button(self, text="Back", command=show_homepage, **back_button_style)
        back_button.pack(side=tk.BOTTOM, anchor=tk.SE, padx=10, pady=10)

# Example usage
if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("800x600")

    def show_homepage():
        for widget in root.winfo_children():
            widget.pack_forget()
        main_frame.pack(fill="both", expand=True)

    main_frame = tk.Frame(root)
    main_frame.pack(fill="both", expand=True)
    
    governmental_resources_page = GovernmentalResourcesPage(root, show_homepage)
    governmental_resources_page.pack(fill="both", expand=True)
    
    root.mainloop()
