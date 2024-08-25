import tkinter as tk
from tkinter import ttk

class RegisterToVotePage(tk.Frame):
    def __init__(self, master, show_homepage):
        super().__init__(master)
        self.configure(bg='grey')

        # Title
        title_label = tk.Label(self, text="Register to Vote", font=("Arial", 24, "bold"), bg='grey', fg='black')
        title_label.pack(pady=20)

        # Create a PanedWindow widget to manage the layout
        paned_window = ttk.PanedWindow(self, orient=tk.HORIZONTAL)
        paned_window.pack(expand=True, pady=10, padx=10, fill=tk.BOTH)

        # Create a Notebook widget (tabbed interface)
        notebook = ttk.Notebook(paned_window)
        paned_window.add(notebook, weight=1)

        # Important Deadlines Tab
        deadlines_frame = ttk.Frame(notebook)
        deadlines_frame.pack(fill=tk.BOTH, expand=True)
        notebook.add(deadlines_frame, text="Important Deadlines")

        # Eligibility Tab
        eligibility_frame = ttk.Frame(notebook)
        eligibility_frame.pack(fill=tk.BOTH, expand=True)
        notebook.add(eligibility_frame, text="Eligibility")

        # Game Tab (Placeholder)
        game_frame = ttk.Frame(notebook)
        game_frame.pack(fill=tk.BOTH, expand=True)
        notebook.add(game_frame, text="Game")

        # Back button with the same style as the other pages
        submit_button_style = {
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
        
        back_button = tk.Button(self, text="Back", command=show_homepage, **submit_button_style)
        back_button.pack(side=tk.BOTTOM, anchor=tk.SE, padx=10, pady=10)

        # Dropdown menu for state selection (Important Deadlines Tab)
        state_label_deadlines = tk.Label(deadlines_frame, text="Select Your State:", font=("Arial", 18), bg='grey', fg='black')
        state_label_deadlines.pack(pady=10)

        states = [
            "Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut", "Delaware", 
            "Florida", "Georgia", "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa", "Kansas", "Kentucky", 
            "Louisiana", "Maine", "Maryland", "Massachusetts", "Michigan", "Minnesota", "Mississippi", 
            "Missouri", "Montana", "Nebraska", "Nevada", "New Hampshire", "New Jersey", "New Mexico", 
            "New York", "North Carolina", "North Dakota", "Ohio", "Oklahoma", "Oregon", "Pennsylvania", 
            "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah", "Vermont", 
            "Virginia", "Washington", "West Virginia", "Wisconsin", "Wyoming"
        ]

        state_var_deadlines = tk.StringVar()
        state_dropdown_deadlines = ttk.Combobox(deadlines_frame, textvariable=state_var_deadlines, values=states, state="readonly", font=("Arial", 12))
        state_dropdown_deadlines.set("Select State")
        state_dropdown_deadlines.pack(pady=10)

        # Function to display the table when the submit button is pressed (Important Deadlines Tab)
        def show_table():
            table_frame.pack(pady=10, padx=10, fill=tk.NONE, expand=False)

        # Submit button (Important Deadlines Tab)
        submit_button_deadlines = tk.Button(deadlines_frame, text="Submit", command=show_table, **submit_button_style)
        submit_button_deadlines.pack(pady=10)

        # Create the table under the "Important Deadlines" Tab (initially hidden)
        table_frame = tk.Frame(deadlines_frame, bg='grey')

        # Create the columns and rows
        methods = ["In Person", "By Mail", "Online"]
        deadlines = [
            "Through the Saturday before Election Day at the county clerk's office (or other location the county clerk authorizes). 28 days before Election Day otherwise.",
            "Postmarked 28 days before Election Day. An application may be accepted through the Friday following the deadline if the application is postmarked before the deadline.",
            "28 days before Election Day."
        ]

        for i, method in enumerate(methods):
            method_label = tk.Label(table_frame, text=method, font=("Arial", 20, "bold"), bg='grey', fg='black', borderwidth=1, relief="solid", wraplength=400)
            method_label.grid(row=i, column=0, sticky="nsew", padx=2, pady=2, ipady=5)

            deadline_label = tk.Label(table_frame, text=deadlines[i], font=("Arial", 20), bg='grey', fg='black', borderwidth=1, relief="solid", wraplength=600)
            deadline_label.grid(row=i, column=1, sticky="nsew", padx=2, pady=2, ipady=5)

        # Make columns expand equally
        table_frame.grid_columnconfigure(0, weight=1)
        table_frame.grid_columnconfigure(1, weight=2)

        # Set uniform row height by setting row weights
        for i in range(len(methods)):
            table_frame.grid_rowconfigure(i, weight=1)

        # Dropdown menu for state selection (Eligibility Tab)
        state_label_eligibility = tk.Label(eligibility_frame, text="Select Your State:", font=("Arial", 18), bg='grey', fg='black')
        state_label_eligibility.pack(pady=10)

        state_var_eligibility = tk.StringVar()
        state_dropdown_eligibility = ttk.Combobox(eligibility_frame, textvariable=state_var_eligibility, values=states, state="readonly", font=("Arial", 12))
        state_dropdown_eligibility.set("Select State")
        state_dropdown_eligibility.pack(pady=10)

        # Function to display eligibility text when the submit button is pressed (Eligibility Tab)
        def show_eligibility_text():
            eligibility_text.pack(pady=10, padx=10)

        # Submit button (Eligibility Tab)
        submit_button_eligibility = tk.Button(eligibility_frame, text="Submit", command=show_eligibility_text, **submit_button_style)
        submit_button_eligibility.pack(pady=10)

        # Eligibility text (initially hidden)
        eligibility_text = tk.Label(
            eligibility_frame, 
            text="(1) a New Mexico driver’s license or New Mexico identification card issued through the motor vehicle division of the taxation and revenue department;\n\n"
                 "(2) any document that contains an address in the county together with a photo identification card; or\n\n"
                 "(3) a current valid student photo identification card from a post-secondary educational institution in New Mexico accompanied by a current student fee statement that contains the student’s address in the county.",
            font=("Arial", 14),
            bg='grey',
            fg='black',
            justify=tk.LEFT,
            wraplength=800
        )

# Example usage
if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("1200x800")

    def show_homepage():
        for widget in root.winfo_children():
            widget.pack_forget()
        main_frame.pack(fill="both", expand=True)

    main_frame = tk.Frame(root)
    main_frame.pack(fill="both", expand=True)

    register_to_vote_page = RegisterToVotePage(root, show_homepage)
    register_to_vote_page.pack(fill="both", expand=True)

    root.mainloop()
