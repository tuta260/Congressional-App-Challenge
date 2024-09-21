import tkinter as tk
from tkinter import ttk

class LegislativeProcessPage(tk.Frame):
    def __init__(self, master, show_homepage, ID):
        super().__init__(master)
        self.configure(bg='grey')

        # Title
        title_label = tk.Label(self, text="Legislative Process", font=("Arial", 24, "bold"), bg='grey', fg='black')
        title_label.pack(pady=20)

        # Login info
        self.username_display_label = tk.Label(self, text=f"User: {ID}", font=("Arial", 14, "bold"), bg='grey', fg='black')
        self.username_display_label.place(relx=1.0, y=20, anchor="ne", x=-20)

        # Create a PanedWindow widget to manage the layout
        paned_window = ttk.PanedWindow(self, orient=tk.HORIZONTAL)
        paned_window.pack(expand=True, pady=10, padx=10, fill=tk.BOTH)

        # Create a Notebook widget (tabbed interface)
        notebook = ttk.Notebook(paned_window)
        paned_window.add(notebook, weight=1)

        # Stages Tab with Scrollable Flowchart
        stages_frame = ttk.Frame(notebook)
        stages_frame.pack(fill=tk.BOTH, expand=True)
        notebook.add(stages_frame, text="Stages")

        stages_canvas = tk.Canvas(stages_frame, bg='grey')
        stages_scrollbar = tk.Scrollbar(stages_frame, orient="vertical", command=stages_canvas.yview)
        stages_scrollable_frame = tk.Frame(stages_canvas, bg='grey')

        stages_scrollable_frame.bind(
            "<Configure>",
            lambda e: stages_canvas.configure(
                scrollregion=stages_canvas.bbox("all")
            )
        )

        stages_canvas.create_window((0, 0), window=stages_scrollable_frame, anchor="nw")
        stages_canvas.configure(yscrollcommand=stages_scrollbar.set)

        stages_canvas.pack(side="left", fill="both", expand=True)
        stages_scrollbar.pack(side="right", fill="y")

        # Flowchart Stages of the Legislative Process
        stages_of_legislation = [
            ("Bill Introduction", "A bill is introduced in either the House of Representatives or the Senate by a member of Congress."),
            ("Committee Action", "The bill is referred to the relevant committee(s), where it is studied, and hearings may be held. The committee may amend, pass, or reject the bill."),
            ("Floor Action", "The bill is debated and voted on by the full chamber (House or Senate). Amendments may be proposed and voted on."),
            ("Conference Committee", "If the House and Senate pass different versions of the bill, a conference committee is formed to reconcile the differences."),
            ("Final Approval", "The reconciled bill is sent back to both chambers for final approval. It must pass both chambers in identical form."),
            ("Presidential Action", "The bill is sent to the President, who can sign it into law, veto it, or take no action (leading to a 'pocket veto' if Congress adjourns)."),
            ("Law Implementation", "Once signed into law, the relevant government agencies implement the new law, and it is enforced accordingly."),
        ]

        for stage_name, description in stages_of_legislation:
            stage_label = tk.Label(stages_scrollable_frame, text=stage_name, font=("Arial", 16, "bold"), bg='grey', fg='black', anchor="w")
            stage_label.pack(fill="x", padx=10, pady=10)

            description_label = tk.Label(stages_scrollable_frame, text=description, font=("Arial", 14), bg='grey', fg='black', wraplength=900, justify="left", anchor="w")
            description_label.pack(fill="x", padx=10, pady=5)

            separator = tk.Frame(stages_scrollable_frame, height=2, bd=1, relief="sunken", bg='black')
            separator.pack(fill="x", padx=20, pady=20)

        # Types Tab with Scrollable Glossary
        types_frame = ttk.Frame(notebook)
        types_frame.pack(fill=tk.BOTH, expand=True)
        notebook.add(types_frame, text="Types")

        types_canvas = tk.Canvas(types_frame, bg='grey')
        types_scrollbar = tk.Scrollbar(types_frame, orient="vertical", command=types_canvas.yview)
        types_scrollable_frame = tk.Frame(types_canvas, bg='grey')

        types_scrollable_frame.bind(
            "<Configure>",
            lambda e: types_canvas.configure(
                scrollregion=types_canvas.bbox("all")
            )
        )

        types_canvas.create_window((0, 0), window=types_scrollable_frame, anchor="nw")
        types_canvas.configure(yscrollcommand=types_scrollbar.set)

        types_canvas.pack(side="left", fill="both", expand=True)
        types_scrollbar.pack(side="right", fill="y")

        # Glossary of Types of Legislation
        types_of_legislation = {
            "Bill": "A proposal for a new law, or a proposal to amend or repeal an existing law, presented for debate and approval by a legislative body.",
            "Joint Resolution": "A legislative measure that requires approval by both the House and Senate and is submitted to the president for approval or disapproval. Joint resolutions generally deal with limited matters or temporary issues.",
            "Concurrent Resolution": "A legislative measure adopted by both houses that does not have the force of law and does not require the president's signature. It is often used to make or amend rules that apply to both houses or to express the sentiment of Congress.",
            "Simple Resolution": "A legislative measure passed by either the House or Senate that addresses matters entirely within the prerogative of the house concerned. It does not have the force of law and does not require the president's signature.",
            "Appropriation Bill": "A bill that provides the legal authority to spend or obligate the government's money for a particular purpose.",
            "Authorization Bill": "A bill that establishes, continues, or modifies a federal program or agency. It may set specific policies or limits on the programs and authorize appropriations for carrying out the policies.",
            "Omnibus Bill": "A bill that combines multiple areas of legislation into one document that is voted on as a single item. Omnibus bills can be used to pass controversial changes that might not pass as individual bills.",
            "Private Bill": "A bill that applies to a specific individual or group of individuals, often providing relief or addressing issues such as immigration, taxation, or compensation claims.",
            "Public Bill": "A bill that applies to the general public or a broad class of citizens. Public bills often deal with issues such as taxation, national defense, or social programs.",
            "Revenue Bill": "A bill focused on raising money for the government through taxes or tariffs. According to the U.S. Constitution, all revenue bills must originate in the House of Representatives.",
            "Rider": "An additional provision added to a bill or other measure under the consideration of a legislature, having little connection with the subject matter of the bill. Riders are often used to pass controversial provisions that would not pass on their own.",
            "Sunset Provision": "A clause in a law that sets an expiration date for the law unless further legislative action is taken to extend it. Sunset provisions are often included in bills as a way to force periodic review and reevaluation."
        }

        for type_name, description in types_of_legislation.items():
            type_label = tk.Label(types_scrollable_frame, text=type_name, font=("Arial", 14, "bold"), bg='grey', fg='black', anchor="w")
            type_label.pack(fill="x", padx=10, pady=5)

            description_label = tk.Label(types_scrollable_frame, text=description, font=("Arial", 12), bg='grey', fg='black', wraplength=900, justify="left", anchor="w")
            description_label.pack(fill="x", padx=10, pady=5)

        # Jargon Tab with Scrollable Glossary
        jargon_frame = ttk.Frame(notebook)
        jargon_frame.pack(fill=tk.BOTH, expand=True)
        notebook.add(jargon_frame, text="Jargon")

        jargon_canvas = tk.Canvas(jargon_frame, bg='grey')
        jargon_scrollbar = tk.Scrollbar(jargon_frame, orient="vertical", command=jargon_canvas.yview)
        jargon_scrollable_frame = tk.Frame(jargon_canvas, bg='grey')

        jargon_scrollable_frame.bind(
            "<Configure>",
            lambda e: jargon_canvas.configure(
                scrollregion=jargon_canvas.bbox("all")
            )
        )

        jargon_canvas.create_window((0, 0), window=jargon_scrollable_frame, anchor="nw")
        jargon_canvas.configure(yscrollcommand=jargon_scrollbar.set)

        jargon_canvas.pack(side="left", fill="both", expand=True)
        jargon_scrollbar.pack(side="right", fill="y")

        # Glossary of Legislative Jargon
        glossary_terms = {
            "Amendment": "A change or addition proposed during debate on a bill in a legislative assembly.",
            "Bicameral": "A legislature consisting of two houses, such as the U.S. Congress, which is made up of the Senate and House of Representatives.",
            "Bill": "A proposal for a new law or a change to an existing law presented for debate before a legislative body.",
            "Cloture": "A procedure used in the Senate to bring debate to an end, requiring a supermajority vote.",
            "Filibuster": "A tactic used by senators to delay or block legislative action by extending debate on the measure.",
            "Quorum": "The minimum number of members required to be present for the legislative body to conduct official business.",
            "Rider": "An additional provision added to a bill or other measure under the consideration of a legislature, having little connection with the subject matter of the bill.",
            "Veto": "The constitutional right of a president or governor to reject a decision or proposal made by a law-making body.",
            "Conference Committee": "A temporary, joint committee formed to resolve differences between the House and Senate versions of a bill.",
            "Markup": "The process by which a congressional committee or subcommittee debates, amends, and rewrites proposed legislation.",
            "Gerrymandering": "The practice of manipulating the boundaries of an electoral constituency to favor one party or class.",
            "Hearing": "A meeting or session of a Senate, House, joint, or special committee of Congress, usually open to the public, to obtain information and opinions on proposed legislation.",
            "Incumbent": "The current holder of a political office.",
            "Lobbying": "The act of attempting to influence the actions, policies, or decisions of officials in their daily life, most often legislators or members of regulatory agencies.",
            "Majority Leader": "The head of the majority party in a legislative body, especially the US Senate or House of Representatives.",
            "Minority Leader": "The head of the minority party in a legislative body, especially the US Senate or House of Representatives.",
            "Resolution": "A legislative measure passed by only either the Senate or the House. It does not have the force of law.",
            "Whip": "An official of a political party whose task is to ensure party discipline in a legislature."
        }

        for term, definition in glossary_terms.items():
            term_label = tk.Label(jargon_scrollable_frame, text=term, font=("Arial", 14, "bold"), bg='grey', fg='black', anchor="w")
            term_label.pack(fill="x", padx=10, pady=5)

            definition_label = tk.Label(jargon_scrollable_frame, text=definition, font=("Arial", 12), bg='grey', fg='black', wraplength=900, justify="left", anchor="w")
            definition_label.pack(fill="x", padx=10, pady=5)

        # Back button with a simpler style
        back_button = tk.Button(self, text="Back", command=show_homepage, font=("Arial", 12), bg="#1bc3cc", fg="black", activebackground="#139c9f", activeforeground="black", width=10, height=2, bd=0, highlightthickness=0)
        back_button.pack(side=tk.BOTTOM, anchor=tk.SE, padx=10, pady=10)

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

    legislative_process_page = LegislativeProcessPage(root, show_homepage)
    legislative_process_page.pack(fill="both", expand=True)

    root.mainloop()
