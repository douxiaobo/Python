import pyttsx3
text="Hello, World! How are you today?"

engine = pyttsx3.init()
engine.setProperty('rate', 120)
# engine.setProperty('voice', 'en')
engine.say(text)
engine.runAndWait()