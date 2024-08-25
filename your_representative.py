import tkinter as tk
import webbrowser
from tkinter import ttk
from PIL import Image, ImageTk  # Import the necessary modules from PIL

class YourRepresentativesPage(tk.Frame):
    def __init__(self, master, show_homepage):
        super().__init__(master)
        self.configure(bg='grey')  # Set the background color to grey

        # Title
        title_label = tk.Label(self, text="Your Representatives", font=("Arial", 24, "bold"), bg='grey', fg='black')
        title_label.pack(pady=20)

        # Create a PanedWindow widget to manage the layout
        paned_window = ttk.PanedWindow(self, orient=tk.HORIZONTAL)
        paned_window.pack(expand=True, pady=10, padx=10, fill=tk.BOTH)

        # Create a Notebook widget (tabbed interface)
        notebook = ttk.Notebook(paned_window)
        paned_window.add(notebook, weight=1)

        # State Representatives Tab
        state_frame = ttk.Frame(notebook)
        state_frame.pack(fill=tk.BOTH, expand=True)
        notebook.add(state_frame, text="State")

        # Federal Representatives Tab with Address Input Fields
        federal_frame = ttk.Frame(notebook)
        federal_frame.pack(fill=tk.BOTH, expand=True)
        notebook.add(federal_frame, text="Federal")

        # Address Input Fields
        def create_address_input(frame):
            address_label = tk.Label(frame, text="Enter Your Address:", font=("Arial", 16))
            address_label.pack(pady=10)

            input_frame = tk.Frame(frame)
            input_frame.pack(pady=10)

            entry_width = 50  # Uniform width for all input boxes

            street_label = tk.Label(input_frame, text="Street Address:", font=("Arial", 14))
            street_label.grid(row=0, column=0, sticky="e", padx=(0, 10))
            street_entry = tk.Entry(input_frame, width=entry_width, font=("Arial", 12))
            street_entry.grid(row=0, column=1, pady=5)

            city_label = tk.Label(input_frame, text="City:", font=("Arial", 14))
            city_label.grid(row=1, column=0, sticky="e", padx=(0, 10))
            city_entry = tk.Entry(input_frame, width=entry_width, font=("Arial", 12))
            city_entry.grid(row=1, column=1, pady=5)

            state_label = tk.Label(input_frame, text="State:", font=("Arial", 14))
            state_label.grid(row=2, column=0, sticky="e", padx=(0, 10))
            state_entry = tk.Entry(input_frame, width=entry_width, font=("Arial", 12))
            state_entry.grid(row=2, column=1, pady=5)

            zip_label = tk.Label(input_frame, text="ZIP Code:", font=("Arial", 14))
            zip_label.grid(row=3, column=0, sticky="e", padx=(0, 10))
            zip_entry = tk.Entry(input_frame, width=entry_width, font=("Arial", 12))
            zip_entry.grid(row=3, column=1, pady=5)

        # Function to open a web link
        def open_link(url):
            webbrowser.open_new(url)

        # Function to display the images with text, contact information, and website links
        def show_images(frame, image_paths, captions, urls, size=(250, int(250 * 2048 / 1638))):
            # Load and resize images while maintaining aspect ratio
            images = []
            for path in image_paths:
                image = Image.open(path)
                image = image.resize(size, Image.ANTIALIAS)
                photo = ImageTk.PhotoImage(image)
                images.append(photo)

            # Create a frame for each image and its caption
            images_frame = tk.Frame(frame, bg='grey')
            images_frame.pack(pady=10)

            # Display images with captions and links below each
            for idx, (photo, caption, url) in enumerate(zip(images, captions, urls)):
                image_caption_frame = tk.Frame(images_frame, bg='grey')
                image_caption_frame.pack(side=tk.LEFT, padx=100)  # Increased spacing between images

                image_label = tk.Label(image_caption_frame, image=photo, bg='grey', bd=0)
                image_label.image = photo  # Keep a reference to the image to avoid garbage collection
                image_label.pack()

                caption_label = tk.Label(image_caption_frame, text=caption, font=("Arial", 15, "bold"), bg='grey', fg='black', justify=tk.CENTER)
                caption_label.pack()

                # Add clickable website link
                if url:
                    link_label = tk.Label(image_caption_frame, text="Website", font=("Arial", 15, "bold", "underline"), bg='grey', fg="blue", cursor="hand2", justify=tk.CENTER)
                    link_label.pack()
                    link_label.bind("<Button-1>", lambda e, url=url: open_link(url))

        # Create address inputs and submit buttons for both State and Federal tabs
        create_address_input(state_frame)
        create_address_input(federal_frame)

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

        def add_submit_button(frame, image_paths, captions, urls):
            submit_button = tk.Button(frame, text="Submit", command=lambda: show_images(frame, image_paths, captions, urls), **submit_button_style)
            submit_button.pack(pady=20)

        # Define images and captions for the State Tab
        state_image_paths = ["Governor.jpg", "StateHouse.jpg", "StateSenate.jpg"]
        state_captions = [
            "Governor\nMichelle Lujan Grisham\nElected 2022\nCall: (505) 476-2200",
            "State Representative\nMarian Matthews\nEmail: marian.matthews@nmlegis.gov",
            "State Senator\nMark Moores\nEmail: mark.moores@nmlegis.gov"
        ]
        state_urls = [
            "https://www.governor.state.nm.us/",
            "",
            ""
        ]

        # Define images and captions for the Federal Tab
        federal_image_paths = ["Representative.jpg", "Senate1.jpg", "Senate2.jpg"]
        federal_captions = [
            "Congresswoman\nMelanie Stansbury\nElected in 2022\nCall: (505) 346-6781",
            "Senator\nBen Ray Luján\nElected in 2020\nCall: 505-230-7040",
            "Senator\nMartin Heinrich\nElected in 2018\nCall: (505) 346-6601"
        ]
        federal_urls = [
            "https://stansbury.house.gov",
            "https://lujan.senate.gov",
            "https://heinrich.senate.gov"
        ]

        # Add submit buttons with appropriate images and captions
        add_submit_button(state_frame, state_image_paths, state_captions, state_urls)
        add_submit_button(federal_frame, federal_image_paths, federal_captions, federal_urls)

        # Back button with the same style as the Governmental Resources page
        back_button = tk.Button(self, text="Back", command=show_homepage, **submit_button_style)
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
    
    your_representatives_page = YourRepresentativesPage(root, show_homepage)
    your_representatives_page.pack(fill="both", expand=True)
    
    root.mainloop()
