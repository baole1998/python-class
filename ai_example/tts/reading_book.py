import pyttsx3

book=open(r"book.txt")
book_content = book.readlines()
engine = pyttsx3.init()
for i in book_content:
    print("BOT:", i)
    engine.say(i)
    engine.runAndWait()