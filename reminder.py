import customtkinter as ctk
from PIL import Image
from voice import speak

def show_reminder(app):

    speak("Hey! It's time to drink water.")
    reminder = ctk.CTkToplevel()
    reminder.overrideredirect(True)

    reminder.title("Drink Water")
    width = 350
    height = 420

    screen_width = reminder.winfo_screenwidth()
    screen_height = reminder.winfo_screenheight()

    x = screen_width - width - 20
    y = screen_height - height - 60

    reminder.geometry(f"{width}x{height}+{x}+{y}")
    frame = ctk.CTkFrame(
    reminder,
    corner_radius=20
    )
    frame.pack(fill="both", expand=True)
    reminder.attributes("-topmost", True)
    reminder.resizable(False, False)

    image = Image.open("images/boy.png")

    photo = ctk.CTkImage(
        light_image=image,
        dark_image=image,
        size=(150,150)
    )

    boy = ctk.CTkLabel(frame, image=photo, text="")
    boy.pack(pady=15)

    label = ctk.CTkLabel(
        frame,
        text="Hey!\nDid you drink water?",
        font=("Arial",20,"bold")
    )

    label.pack(pady=10)

    def drank():
        speak("Great job! Keep yourself hydrated.")
        reminder.destroy()

    yes = ctk.CTkButton(
    frame,
    text="💧 I Drank Water",
    command=drank
    )

    yes.pack(pady=10)

    def remind_again():
        speak("Okay! I'll remind you again in five minutes.")
        reminder.destroy()

    later = ctk.CTkButton(
    frame,
    text="⏰ Remind Me Later",
    command=remind_again
    )
    

    later.pack()

    reminder.mainloop()