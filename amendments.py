import tkinter as tk
from tkinter import ttk

class AmendmentsPage(tk.Frame):
    def __init__(self, master, show_homepage, ID):
        super().__init__(master)
        self.configure(bg='grey')  # Set the background color to grey

        # Title
        title_label = tk.Label(self, text="The Amendments", font=("Arial", 24, "bold"), bg='grey', fg='black')
        title_label.pack(pady=20)

        # Login info
        self.username_display_label = tk.Label(self, text=f"User: {ID}", font=("Arial", 14, "bold"), bg='grey', fg='black')
        self.username_display_label.place(relx=1.0, y=20, anchor="ne", x=-20)

        # Create a PanedWindow widget to manage vertical layout
        paned_window = ttk.PanedWindow(self, orient=tk.HORIZONTAL)
        paned_window.pack(expand=True, pady=10, padx=10, fill=tk.BOTH)

        # Create a Notebook widget (tabbed interface)
        notebook = ttk.Notebook(paned_window)
        paned_window.add(notebook, weight=1)

        # Introduction Tab
        intro_frame = ttk.Frame(notebook)
        intro_text = "The Amendments are changes or additions made to the U.S. Constitution."
        tk.Label(intro_frame, text=intro_text, font=("Arial", 14), wraplength=600, justify="left").pack(pady=10)
        notebook.add(intro_frame, text="Introduction")

        # History Tab with Horizontal Scrolling Timeline
        history_frame = ttk.Frame(notebook)
        history_canvas = tk.Canvas(history_frame, bg='grey', height=300)
        history_scrollbar = ttk.Scrollbar(history_frame, orient=tk.HORIZONTAL, command=history_canvas.xview)
        history_canvas.configure(xscrollcommand=history_scrollbar.set)

        timeline_frame = ttk.Frame(history_canvas, padding=10)
        timeline_frame.bind(
            "<Configure>",
            lambda e: history_canvas.configure(
                scrollregion=history_canvas.bbox("all")
            )
        )

        history_canvas.create_window((0, 0), window=timeline_frame, anchor="nw")

        events = [
            {"year": "1791", "event": "1st Amendment: Freedom of Speech, Press, Religion and Petition"},
            {"year": "1791", "event": "2nd Amendment: Right to keep and bear arms"},
            {"year": "1791", "event": "3rd Amendment: Conditions for quarters of soldiers"},
            {"year": "1791", "event": "4th Amendment: Right of search and seizure regulated"},
            {"year": "1791", "event": "5th Amendment: Provisions concerning prosecution"},
            {"year": "1791", "event": "6th Amendment: Right to a speedy trial, witnesses, etc."},
            {"year": "1791", "event": "7th Amendment: Right to a trial by jury"},
            {"year": "1791", "event": "8th Amendment: Excessive bail, cruel punishment"},
            {"year": "1791", "event": "9th Amendment: Rule of construction of Constitution"},
            {"year": "1791", "event": "10th Amendment: Rights of the States under Constitution"},
            {"year": "1795", "event": "11th Amendment: Judicial limits"},
            {"year": "1804", "event": "12th Amendment: Choosing the President, Vice-President"},
            {"year": "1865", "event": "13th Amendment: Slavery abolished"},
            {"year": "1868", "event": "14th Amendment: Citizenship rights"},
            {"year": "1870", "event": "15th Amendment: Race no bar to vote"},
            {"year": "1913", "event": "16th Amendment: Status of income tax clarified"},
            {"year": "1913", "event": "17th Amendment: Senators elected by popular vote"},
            {"year": "1919", "event": "18th Amendment: Liquor abolished"},
            {"year": "1920", "event": "19th Amendment: Women's suffrage"},
            {"year": "1933", "event": "20th Amendment: Presidential, Congressional terms"},
            {"year": "1933", "event": "21st Amendment: 18th Amendment repealed"},
            {"year": "1951", "event": "22nd Amendment: Presidential term limits"},
            {"year": "1961", "event": "23rd Amendment: Presidential vote for D.C."},
            {"year": "1964", "event": "24th Amendment: Poll tax barred"},
            {"year": "1967", "event": "25th Amendment: Presidential disability and succession"},
            {"year": "1971", "event": "26th Amendment: Voting age set to 18 years"},
            {"year": "1992", "event": "27th Amendment: Limiting changes to Congressional pay"}
        ]

        for i, event in enumerate(events):
            event_frame = ttk.Frame(timeline_frame, padding=10, relief="raised", borderwidth=2)
            event_frame.grid(row=0, column=i, padx=10, pady=20)
            tk.Label(event_frame, text=event["year"], font=("Arial", 14, "bold"), wraplength=150, justify="center").pack(pady=(0, 5))
            tk.Label(event_frame, text=event["event"], font=("Arial", 12), wraplength=150, justify="center").pack()

        history_canvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        history_scrollbar.pack(side=tk.BOTTOM, fill=tk.X)

        notebook.add(history_frame, text="History")

        # Game Tab
        game_frame = ttk.Frame(notebook)
        game_paned_window = ttk.PanedWindow(game_frame, orient=tk.HORIZONTAL)
        game_paned_window.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)

        flashcard_frame = FlashcardFrame(game_paned_window)
        game_paned_window.add(flashcard_frame, weight=1)

        notebook.add(game_frame, text="Game")

        # Back button with the same style as the Governmental Resources page
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


class FlashcardFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.configure(bg='grey')  # Set the background color to grey

        self.amendments = [
            {"front": "1st Amendment", "back": "Congress shall make no law respecting an establishment of religion, or prohibiting the free exercise thereof; or abridging the freedom of speech, or of the press; or the right of the people peaceably to assemble, and to petition the Government for a redress of grievances."},
            {"front": "2nd Amendment", "back": "A well regulated Militia, being necessary to the security of a free State, the right of the people to keep and bear Arms, shall not be infringed."},
            {"front": "3rd Amendment", "back": "No Soldier shall, in time of peace be quartered in any house, without the consent of the Owner, nor in time of war, but in a manner to be prescribed by law."},
            {"front": "4th Amendment", "back": "The right of the people to be secure in their persons, houses, papers, and effects, against unreasonable searches and seizures, shall not be violated, and no Warrants shall issue, but upon probable cause, supported by Oath or affirmation, and particularly describing the place to be searched, and the persons or things to be seized."},
            {"front": "5th Amendment", "back": "No person shall be held to answer for a capital, or otherwise infamous crime, unless on a presentment or indictment of a Grand Jury, except in cases arising in the land or naval forces, or in the Militia, when in actual service in time of War or public danger; nor shall any person be subject for the same offence to be twice put in jeopardy of life or limb; nor shall be compelled in any criminal case to be a witness against himself, nor be deprived of life, liberty, or property, without due process of law; nor shall private property be taken for public use, without just compensation."},
            {"front": "6th Amendment", "back": "In all criminal prosecutions, the accused shall enjoy the right to a speedy and public trial, by an impartial jury of the State and district wherein the crime shall have been committed, which district shall have been previously ascertained by law, and to be informed of the nature and cause of the accusation; to be confronted with the witnesses against him; to have compulsory process for obtaining witnesses in his favor, and to have the Assistance of Counsel for his defence."},
            {"front": "7th Amendment", "back": "In Suits at common law, where the value in controversy shall exceed twenty dollars, the right of trial by jury shall be preserved, and no fact tried by a jury, shall be otherwise re-examined in any Court of the United States, than according to the rules of the common law."},
            {"front": "8th Amendment", "back": "Excessive bail shall not be required, nor excessive fines imposed, nor cruel and unusual punishments inflicted."},
            {"front": "9th Amendment", "back": "The enumeration in the Constitution, of certain rights, shall not be construed to deny or disparage others retained by the people."},
            {"front": "10th Amendment", "back": "The powers not delegated to the United States by the Constitution, nor prohibited by it to the States, are reserved to the States respectively, or to the people."},
            {"front": "11th Amendment", "back": "The Judicial power of the United States shall not be construed to extend to any suit in law or equity, commenced or prosecuted against one of the United States by Citizens of another State, or by Citizens or Subjects of any Foreign State."},
            {"front": "12th Amendment", "back": "The Electors shall meet in their respective states and vote by ballot for President and Vice-President..."},
            {"front": "13th Amendment", "back": "Neither slavery nor involuntary servitude, except as a punishment for crime whereof the party shall have been duly convicted, shall exist within the United States, or any place subject to their jurisdiction."},
            {"front": "14th Amendment", "back": "All persons born or naturalized in the United States, and subject to the jurisdiction thereof, are citizens of the United States and of the State wherein they reside..."},
            {"front": "15th Amendment", "back": "The right of citizens of the United States to vote shall not be denied or abridged by the United States or by any State on account of race, color, or previous condition of servitude."},
            {"front": "16th Amendment", "back": "The Congress shall have power to lay and collect taxes on incomes, from whatever source derived, without apportionment among the several States, and without regard to any census or enumeration."},
            {"front": "17th Amendment", "back": "The Senate of the United States shall be composed of two Senators from each State, elected by the people thereof, for six years; and each Senator shall have one vote."},
            {"front": "18th Amendment", "back": "After one year from the ratification of this article the manufacture, sale, or transportation of intoxicating liquors within, the importation thereof into, or the exportation thereof from the United States and all territory subject to the jurisdiction thereof for beverage purposes is hereby prohibited."},
            {"front": "19th Amendment", "back": "The right of citizens of the United States to vote shall not be denied or abridged by the United States or by any State on account of sex."},
            {"front": "20th Amendment", "back": "The terms of the President and the Vice President shall end at noon on the 20th day of January, and the terms of Senators and Representatives at noon on the 3d day of January, of the years in which such terms would have ended if this article had not been ratified; and the terms of their successors shall then begin."},
            {"front": "21st Amendment", "back": "The eighteenth article of amendment to the Constitution of the United States is hereby repealed."},
            {"front": "22nd Amendment", "back": "No person shall be elected to the office of the President more than twice, and no person who has held the office of President, or acted as President, for more than two years of a term to which some other person was elected President shall be elected to the office of the President more than once."},
            {"front": "23rd Amendment", "back": "The District constituting the seat of Government of the United States shall appoint in such manner as the Congress may direct: A number of electors of President and Vice President equal to the whole number of Senators and Representatives in Congress to which the District would be entitled if it were a State..."},
            {"front": "24th Amendment", "back": "The right of citizens of the United States to vote in any primary or other election for President or Vice President, for electors for President or Vice President, or for Senator or Representative in Congress, shall not be denied or abridged by the United States or any State by reason of failure to pay any poll tax or other tax."},
            {"front": "25th Amendment", "back": "In case of the removal of the President from office or of his death or resignation, the Vice President shall become President."},
            {"front": "26th Amendment", "back": "The right of citizens of the United States, who are eighteen years of age or older, to vote shall not be denied or abridged by the United States or by any State on account of age."},
            {"front": "27th Amendment", "back": "No law, varying the compensation for the services of the Senators and Representatives, shall take effect, until an election of Representatives shall have intervened."}
        ]
        self.current_amendment_index = 0
        self.is_front = True

        self.flashcard_width = 400
        self.flashcard_height = 300

        self.flashcard_canvas = tk.Canvas(self, width=self.flashcard_width, height=self.flashcard_height, bg="grey", bd=0, highlightthickness=0)
        self.flashcard_canvas.pack(pady=20)

        self.flashcard_canvas.create_rectangle(10, 10, self.flashcard_width - 10, self.flashcard_height - 10, fill="#1bc3cc", outline="")

        self.flashcard = self.flashcard_canvas.create_text(self.flashcard_width // 2, self.flashcard_height // 2, text=self.amendments[self.current_amendment_index]["front"],
                                                      font=("Arial", 18, "bold"), width=self.flashcard_width - 40, justify="center", fill="white")

        self.flashcard_canvas.bind("<Button-1>", self.flip_flashcard)

        caret_frame = tk.Frame(self, bg='grey')
        caret_frame.pack(pady=10)

        backward_caret_canvas = tk.Canvas(caret_frame, width=50, height=50, bg='grey', bd=0, highlightthickness=0)
        backward_caret_canvas.pack(side=tk.LEFT, padx=10)
        backward_caret_canvas.create_oval(5, 5, 45, 45, fill="white", outline="#1bc3cc")
        self.backward_caret = backward_caret_canvas.create_text(25, 25, text="<", font=("Arial", 18, "bold"), fill="#1bc3cc")
        backward_caret_canvas.tag_bind(self.backward_caret, "<Button-1>", self.show_previous_amendment)

        forward_caret_canvas = tk.Canvas(caret_frame, width=50, height=50, bg='grey', bd=0, highlightthickness=0)
        forward_caret_canvas.pack(side=tk.RIGHT, padx=10)
        forward_caret_canvas.create_oval(5, 5, 45, 45, fill="white", outline="#1bc3cc")
        self.forward_caret = forward_caret_canvas.create_text(25, 25, text=">", font=("Arial", 18, "bold"), fill="#1bc3cc")
        forward_caret_canvas.tag_bind(self.forward_caret, "<Button-1>", self.show_next_amendment)

    def flip_flashcard(self, event):
        current_amendment = self.amendments[self.current_amendment_index]
        if self.is_front:
            self.flashcard_canvas.itemconfig(self.flashcard, text=current_amendment["back"], font=("Arial", 16, "italic"))
        else:
            self.flashcard_canvas.itemconfig(self.flashcard, text=current_amendment["front"], font=("Arial", 18, "bold"))
        self.is_front = not self.is_front

    def show_next_amendment(self, event):
        self.current_amendment_index = (self.current_amendment_index + 1) % len(self.amendments)
        self.update_flashcard()

    def show_previous_amendment(self, event):
        self.current_amendment_index = (self.current_amendment_index - 1) % len(self.amendments)
        self.update_flashcard()

    def update_flashcard(self):
        current_amendment = self.amendments[self.current_amendment_index]
        self.flashcard_canvas.itemconfig(self.flashcard, text=current_amendment["front"], font=("Arial", 18, "bold"))
        self.is_front = True

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
    
    amendments_page = AmendmentsPage(root, show_homepage)
    amendments_page.pack(fill="both", expand=True)
    
    root.mainloop()
