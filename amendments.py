import threading
import tkinter as tk
from tkinter import ttk
from tkinter import Label
import cv2
from PIL import Image, ImageTk
from legislative_data import amendments, events

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
        paned_window.pack(expand=False, pady=10, padx=10, fill=tk.BOTH)

        # Create a Notebook widget (tabbed interface)
        notebook = ttk.Notebook(paned_window)
        paned_window.add(notebook, weight=1)

        # History Tab with Horizontal Scrolling Timeline
        history_frame = ttk.Frame(notebook)
        history_canvas = tk.Canvas(history_frame, bg = "#393a3a", height=150)
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

        for i, event in enumerate(events):
            event_frame = ttk.Frame(timeline_frame, padding=10, relief="raised", borderwidth=2)
            event_frame.grid(row=0, column=i, padx=10, pady=20)
            tk.Button(event_frame, text=event["year"], font=("Arial", 14, "bold"), wraplength=150, justify="center", command=self.show_video).pack(pady=(0, 5))
            tk.Button(event_frame, text=event["event"], font=("Arial", 12), wraplength=150, justify="center", command=self.show_video).pack()

        
        history_canvas.pack(side=tk.TOP, fill=tk.BOTH, expand=False)
        history_scrollbar.pack(side=tk.BOTTOM, fill=tk.X)
        
        # Set fixed video dimensions
        self.video_width = 760
        self.video_height = 460

        # Create a label for displaying video in fixed dimensions
        self.video_frame = tk.Label(history_frame, bg = "#393a3a", width=self.video_width, height=self.video_height)
        self.video_frame.pack(side=tk.BOTTOM, fill=tk.NONE, expand=False, pady=20)

        notebook.add(history_frame, text="History")

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

    def show_video(self):
        # Start a new thread to play the video without freezing the UI
        threading.Thread(target=self.load_video, daemon=True).start()

    def load_video(self):
        # Load video using OpenCV
        video_path = "video.mp4"
        cap = cv2.VideoCapture(video_path)
        
        if not cap.isOpened():
            print("Error: Could not open video file", video_path)
            return

        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            # Convert the frame to RGB and resize it to fit the label
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame = cv2.resize(frame, (self.video_frame.winfo_width(), self.video_frame.winfo_height()))

            # Convert the frame to an ImageTk format
            img = Image.fromarray(frame)
            imgtk = ImageTk.PhotoImage(image=img)

            # Display the frame in the video_label
            self.video_frame.imgtk = imgtk
            self.video_frame.config(image=imgtk)

            # Control frame rate
            self.video_frame.update()
            cv2.waitKey(20)  # Adjust frame rate

        cap.release()


class FlashcardFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.configure(bg='grey')  # Set the background color to grey

        self.amendments = amendments
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

# Establishes Relation of Pages
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
