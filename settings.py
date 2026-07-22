import customtkinter as ctk
import json
from timer import restart_timer

reminder_time = 30
daily_goal = 8

def open_settings(app):

    global reminder_time

    window = ctk.CTkToplevel()
    window.title("Settings")
    window.geometry("350x350")

    label = ctk.CTkLabel(
        window,
        text="Reminder Interval",
        font=("Arial",20,"bold")
    )

    label.pack(pady=15)

    option = ctk.CTkOptionMenu(
        window,
        values=["1","2","5","15","30","45","60"]
    )

    option.pack(pady=20)
    goal_label = ctk.CTkLabel(
    window,
    text="Daily Water Goal",
    font=("Arial", 18, "bold"))

    goal_label.pack(pady=10)

    goal_option = ctk.CTkOptionMenu(
    window,
    values=["6", "8", "10", "12"])

    goal_option.pack(pady=10)

    def save():

        global reminder_time
        global daily_goal

        reminder_time = int(option.get())
        daily_goal = int(goal_option.get())
        data = {
        "reminder_time": reminder_time,
        "daily_goal": daily_goal
        }

        with open("config.json", "w") as file:
            json.dump(data, file, indent=4)

        print("Reminder:", reminder_time)
        print("Goal:", daily_goal)
        print("Settings Saved!!")


        restart_timer(app)
        window.destroy()

    button = ctk.CTkButton(
        window,
        text="Save",
        command=save
    )

    button.pack(pady=20)