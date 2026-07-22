import pyttsx3

engine = pyttsx3.init()

engine.setProperty("rate", 160)

print("Speaking...")

engine.say("Hello Avinash. This is a voice test.")

engine.runAndWait()

print("Finished")