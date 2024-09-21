import tkinter as tk
from amendments import AmendmentsPage
from register_to_vote import RegisterToVotePage
from your_representative import YourRepresentativesPage
from about_us import AboutUsPage  # Import About Us page
from contact_us import ContactUsPage  # Import Contact Us page
from login import LoginPage  # Import Login page
from legislative_process import LegislativeProcessPage

# Constants for easy customization
TITLE_COLOR = "black"
BACKGROUND_COLOR = "grey"
ROUNDED_BUTTON_COLOR = "#1bc3cc"
INTERNAL_BUTTON_COLOR = "#139c9f"
INTERNAL_BUTTON_TEXT_COLOR = "black"


class MainApplication(tk.Frame):
    userID = "Not Signed In"

    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.configure(bg=BACKGROUND_COLOR)
        self.pack(fill="both", expand=True)

        self.master.attributes('-fullscreen', True)

        

        title_label = tk.Label(self, text="Civic Engagement App", font=("Arial", 24, "bold"), bg=BACKGROUND_COLOR, fg=TITLE_COLOR)
        title_label.pack(pady=20)

        button_frame = tk.Frame(self, bg=BACKGROUND_COLOR)
        button_frame.pack(expand=True)

        button_style = {
            "font": ("Futura", 28),
            "bg": ROUNDED_BUTTON_COLOR,
            "fg": INTERNAL_BUTTON_TEXT_COLOR,
            "activebackground": INTERNAL_BUTTON_COLOR,
            "activeforeground": INTERNAL_BUTTON_TEXT_COLOR,
            "width": 70,
            "height": 10,
            "bd": 3,
            "highlightthickness": 0,
        }

        small_button_style = {
            "font": ("Arial", 12),
            "bg": ROUNDED_BUTTON_COLOR,
            "fg": INTERNAL_BUTTON_TEXT_COLOR,
            "activebackground": INTERNAL_BUTTON_COLOR,
            "activeforeground": INTERNAL_BUTTON_TEXT_COLOR,
            "width": 10,
            "height": 2,
            "bd": 0,
            "highlightthickness": 0,
        }

        buttons_info = [
            ("Your Representative", self.show_rep_page),
            ("The Amendments", self.show_amendments_page),
            ("Register to Vote", self.show_register_to_vote_page),
            ("The Legislative Process", self.show_legis_process_page),
        ]

        self.username_display_label = tk.Label(self, text=f"User: {self.userID}", font=("Arial", 14, "bold"), bg='grey', fg='black')
        self.username_display_label.place(relx=1.0, y=20, anchor="ne", x=-20)

        def create_rounded_button(row, col, text, command):
            canvas = tk.Canvas(button_frame, width=300, height=100, bg=BACKGROUND_COLOR, highlightthickness=0)
            canvas.grid(row=row, column=col, padx=20, pady=20)

            radius = 20
            canvas.create_arc((0, 0, radius * 2, radius * 2), start=90, extent=90, fill=ROUNDED_BUTTON_COLOR, outline="")
            canvas.create_arc((300 - radius * 2, 0, 300, radius * 2), start=0, extent=90, fill=ROUNDED_BUTTON_COLOR, outline="")
            canvas.create_arc((0, 100 - radius * 2, radius * 2, 100), start=180, extent=90, fill=ROUNDED_BUTTON_COLOR, outline="")
            canvas.create_arc((300 - radius * 2, 100 - radius * 2, 300, 100), start=270, extent=90, fill=ROUNDED_BUTTON_COLOR, outline="")
            canvas.create_rectangle((radius, 0, 300 - radius, 100), fill=ROUNDED_BUTTON_COLOR, outline="")
            canvas.create_rectangle((0, radius, 300, 100 - radius), fill=ROUNDED_BUTTON_COLOR, outline="")

            button = tk.Button(canvas, text=text, command=command, **button_style)
            button.place(x=150, y=50, anchor="center")

        def create_button(row, col, text, command):
            canvas = tk.Canvas(button_frame, width=300, height=100, bg=BACKGROUND_COLOR, highlightthickness=0)
            canvas.grid(row=row, column=col, padx=20, pady=20)

            button = tk.Button(canvas, text=text, command=command, **button_style)
            button.place(x=150, y=50, anchor="center")

        for i, (text, command) in enumerate(buttons_info):
            row = i // 2
            col = i % 2
            create_button(row, col, text, command)

        bottom_frame = tk.Frame(self, bg=BACKGROUND_COLOR)
        bottom_frame.pack(side=tk.BOTTOM, anchor=tk.SE, padx=10, pady=10)

        about_us_button = tk.Button(bottom_frame, text="About Us", command=self.show_about_us_page, **small_button_style)
        about_us_button.pack(side=tk.LEFT, padx=5)

        contact_us_button = tk.Button(bottom_frame, text="Contact Us", command=self.show_contact_us_page, **small_button_style)
        contact_us_button.pack(side=tk.LEFT, padx=5)

        login_button = tk.Button(bottom_frame, text="Login", command=self.show_login_page, **small_button_style)
        login_button.pack(side=tk.LEFT, padx=5)


    def open_page(self, page_class):
        self.pack_forget()
        page_frame = page_class(self.master, self.show_homepage, self.userID)
        page_frame.pack(fill="both", expand=True)

    def show_homepage(self):
        for widget in self.master.winfo_children():
            widget.pack_forget()
        self.pack(fill="both", expand=True)
        f = open('users.txt')
        text = f.read()
        if(text!=""):
            self.userID = text
            self.username_display_label.config(text = f"User: {self.userID}")

    def show_amendments_page(self):
        self.open_page(AmendmentsPage)

    def show_register_to_vote_page(self):
        self.open_page(RegisterToVotePage)

    def show_rep_page(self):
        self.open_page(YourRepresentativesPage)

    def show_legis_process_page(self):
        self.open_page(LegislativeProcessPage)

    def show_about_us_page(self):
        self.open_page(AboutUsPage)

    def show_contact_us_page(self):
        self.open_page(ContactUsPage)

    def show_login_page(self):
        self.open_page(LoginPage)

# Setup as main
if __name__ == "__main__":
    root = tk.Tk()
    app = MainApplication(root)
    root.mainloop()
