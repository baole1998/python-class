import speech_recognition as sr
import pyttsx3

r = sr.Recognizer()

def SpeakText(command):
	engine = pyttsx3.init()
	engine.say(command)
	engine.runAndWait()

while(1):
    try:
        with sr.Microphone() as source2:
            print("\n============================")
            print("Bắt đầu lắng nghe ...")
            r.adjust_for_ambient_noise(source2, duration=0.2)
            audio2 = r.listen(source2)

            # Vietnamese recognizer
            my_words = r.recognize_google(audio2, language="vi-VN")
            
            # English recognizer
            # my_words = r.recognize_google(audio2, language="en-US")
            
            my_words = my_words.lower()

            print("\n============================")
            print(f'Có phải bạn vừa nói là: "{my_words}"')
            
            log=open(r"speaking_logs.txt", 'a')
            log.write(my_words)
            log.close()
            
            # SpeakText(my_words)
    except sr.RequestError as e:
        print("Hiện tại tôi chỉ nhận diện được Tiếng Anh; {0}".format(e))
		
    except sr.UnknownValueError:
        print("Âm thanh không hợp lệ, bạn nói lại được không ?")