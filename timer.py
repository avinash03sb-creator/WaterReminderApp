from assistant import show_assistant
import json

timer_id = None

def start_timer(app):

    print("⏰ Timer started...")

    with open("config.json", "r") as file:
        data = json.load(file)

    reminder_time = data["reminder_time"]

    milliseconds = reminder_time * 60 * 1000

    print(f"Reminder in {reminder_time} minutes")

    global timer_id

    timer_id = app.after(milliseconds, lambda: remind(app))

def remind(app):

    print("🔔 Showing reminder...")

    show_assistant()

    # Read the latest reminder time from config.json
    with open("config.json", "r") as file:
        data = json.load(file)

    reminder_time = data["reminder_time"]

    milliseconds = reminder_time * 60 * 1000

    print(f"Next reminder in {reminder_time} minutes")

    app.after(milliseconds, lambda: remind(app))

def restart_timer(app):
    global timer_id

    # Cancel the previous timer
    if timer_id is not None:
        app.after_cancel(timer_id)

    # Start a new timer
    start_timer(app)