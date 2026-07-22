import customtkinter as ctk
from PIL import Image
from tkinter import messagebox
from timer import start_timer
from settings import open_settings
from tracker import load_data, save_data
# Set appearance
ctk.set_appearance_mode("light")   # Options: "light", "dark", "system"
ctk.set_default_color_theme("blue")

# Create window
app = ctk.CTk()
app.title("Water Reminder")
app.geometry("500x800")
data = load_data()
water_count = data["count"]
daily_goal = 8
daily_goal = 8

# Heading
title = ctk.CTkLabel(
    app,
    text="💧 Water Reminder",
    font=("Arial", 28, "bold")
)
title.pack(pady=20)

# Message
message = ctk.CTkLabel(
    app,
    text="Stay hydrated!\nYour assistant will remind you to drink water.",
    font=("Arial", 18)
)
message.pack(pady=20)
counter_label = ctk.CTkLabel(
    app,
    text="Today's Water: 0 / 8 glasses",
    font=("Arial", 16, "bold")
)
counter_label.pack(pady=10)
progress = ctk.CTkProgressBar(app, width=300)
progress.pack(pady=10)

progress.set(0)
image = Image.open("images/boy.png")
image = image.resize((180, 180))

photo = ctk.CTkImage(light_image=image,
                     dark_image=image,
                     size=(180,180))

boy = ctk.CTkLabel(app, image=photo, text="")
boy.pack(pady=15)

# Button frame
def drank_water():
    global water_count

    water_count += 1
    save_data(water_count)

    counter_label.configure(
        text=f"Today's Water: {water_count} / {daily_goal} glasses"
    )

    progress.set(water_count / daily_goal)

    if water_count >= daily_goal:
        messagebox.showinfo(
            "Congratulations! 🎉",
            "You completed today's water goal!"
        )
    else:
        messagebox.showinfo(
            "Great Job! 💧",
            "Keep yourself hydrated!"
        )

def remind_later():
    messagebox.showinfo(
        "Reminder",
        "Okay! I'll remind you again in 5 minutes."
    )

button_frame = ctk.CTkFrame(app, fg_color="transparent")
button_frame.pack(pady=20)

# Yes button
yes_button = ctk.CTkButton(
    button_frame,
    text="✅ I Drank Water",
    width=160,
    command=drank_water
)


# Remind button
remind_button = ctk.CTkButton(
    button_frame,
    text="⏰ Remind Me in 5 Min",
    width=170,
    command=remind_later
)
yes_button.grid(row=0, column=0, padx=10)

remind_button.grid(row=0, column=1, padx=10)


settings_button = ctk.CTkButton(
    app,
    text="⚙ Settings",
    command=lambda: open_settings(app)
)

settings_button.pack(pady=15)
start_timer(app)
app.mainloop()