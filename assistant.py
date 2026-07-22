import customtkinter as ctk
from PIL import Image
from voice import speak
assistant = None

def show_assistant():
    global assistant

    if assistant is not None and assistant.winfo_exists():
        return

    assistant = ctk.CTkToplevel()

    assistant.overrideredirect(True)
    assistant.attributes("-topmost", True)

    width = 220
    height = 260

    screen_width = assistant.winfo_screenwidth()
    screen_height = assistant.winfo_screenheight()

    x = screen_width - width - 20
    y = screen_height - height - 60

    assistant.geometry(f"{width}x{height}+{x}+{y}")

    frame = ctk.CTkFrame(
    assistant,
    fg_color="transparent")
    frame.pack(fill="both", expand=True)

    image = Image.open("images/boy.png")

    photo = ctk.CTkImage(
        light_image=image,
        dark_image=image,
        size=(150, 150)
    )

    boy = ctk.CTkLabel(frame, image=photo, text="")
    boy.pack(pady=10)

    bubble = ctk.CTkFrame(
    frame,
    corner_radius=15,
    fg_color="white")
    bubble.pack(pady=5)

    label = ctk.CTkLabel(
    bubble,
    text="💧 Time to drink water!",
    font=("Arial", 16, "bold"),
    text_color="black")
    label.pack(padx=15, pady=8)

    yes = ctk.CTkButton(
        frame,
        text="💧 I Drank Water",
        command=assistant.destroy
    )
    yes.pack(pady=5)

    later = ctk.CTkButton(
        frame,
        text="⏰ Later",
        command=assistant.destroy
    )
    later.pack(pady=5)
    speak("Hey! It's time to drink water.")


if __name__ == "__main__":
    app = ctk.CTk()
    app.withdraw()
    show_assistant()
    app.mainloop()