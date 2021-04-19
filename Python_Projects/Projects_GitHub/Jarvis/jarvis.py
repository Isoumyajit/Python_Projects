import datetime
import pyttsx3 as pp
import speech_recognition as sr
import wikipedia
import webbrowser
import cv2
import os
import re
import smtplib
import random

# //////////////////////////////////////

wishList = ["I am good", "I am going well", "I am doing well", "All is fine", "Everything is perfect",
            "Life is "
            "going like "
            "butter",
            "haha haha i am a machine never upset like humans"
            ]
recipientDic = {"soumyajit": 'soumyo.chak1999@gmail.com'}
engine = pp.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[-1].id)
engine.setProperty('volume', 10.0)


def sendEmail(recipient_address, summary_content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('soumyo.chak1999@gmail.com', 'Chak2096@#')
    server.sendmail('soumyo.chak1999@gmail.com', recipient_address, summary_content)
    server.close()
    speak("successfully sent")


def wishMe():
    """
    It Always wish at the time of first start of execution
    depending on the time of the day
    """

    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning Soumyajit")
    elif 12 <= hour < 18:
        speak("Good Afternoon Soumyajit")
    else:
        speak("Good Evening Soumyajit")
    speak("How May i help you")


def take_command():
    """
    Take voice command from the mic
    """
    helper = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        helper.pause_threshold = 1
        audio = helper.listen(source)
    query_parser = None
    try:
        print("Recognizing...")
        query_parser = helper.recognize_google(audio, language='en-in')
        print(f"user said :: {query_parser}\n")

    except Exception as E:
        print(E)
        print("Say that again please...")

    return query_parser


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


if __name__ == "__main__":
    wishMe()
    while True:
        query = take_command()
        if query is not None:
            query = query.lower()
            lst = query.split()
            if "wikipedia" in query:
                print("Searching in Wikipedia....Please wait")
                query = query.replace("wikipedia", "")
                result = wikipedia.summary(query, sentences=3)
                speak("According to Wikipedia " + result)

            elif re.search(r"([a-z])*webcam([a-z])*", query) or re.search(r"([a-z])*picture([a-z])*", query) or \
                    re.search(r"([a-z])*take([a-z])*"):
                print(lst)
                cv2.namedWindow("preview")
                capture = cv2.VideoCapture(0)
                ret, frame = capture.read()
                cv2.imshow('img1', frame)
                filename = "image" + str(random.random()) + ".jpg"
                cv2.imwrite(filename, frame)
                cv2.destroyAllWindows()
                capture.release()

            elif re.search(r"([a-z])*search([a-z])*", query):
                destination = lst[-1]
                destination += ".com"
                webbrowser.open(destination)

            elif re.search(r"([a-z])*bye([a-z])*", query):
                speak("Thank you  " + "Good bye")
                speak("Remember me when required")
                break

            elif re.search(r"([a-z])*play([a-z])*", query):
                music_dir = 'Songs'
                print("yes")
                songs = os.listdir(music_dir)
                print(songs)
                os.startfile(os.path.join(music_dir, songs[0]))

            elif re.search(r"([a-z])*calculator([a-z])*", query):
                os.system("calc")

            elif re.search(r"([a-z])*the time([a-z])*", query):
                time = datetime.datetime.now().strftime("%H:%M:%S")
                print(time)
                speak(f"right now it is")
                speak(time[0:2] + "hours")
                speak(time[3:5] + " minutes")
                speak(time[-1:-3:-1] + " seconds")

            elif re.search(r"([a-z])*send email([a-z])*", query):
                # speak("whom to send email")
                to = 'soumyajit'
                to = recipientDic.get(to)
                speak("what to send")
                content = take_command()
                try:
                    sendEmail(to, content)
                except Exception as e:
                    print(e)
                    speak("Sorry !! currently email is not sent")

            elif re.search(r"([a-z])*you doing([a-z])*", query) or re.search(r"([a-z])*are you([a-z])*", query):
                speak("Hi")
                speak(random.choice(wishList))
                speak("What about you hm hm ")

            elif re.search(r"([a-z])*recording([a-z])*", query):
                frame_width = 400
                frame_height = 400
                cap = cv2.VideoCapture()
                while True:
                    pass
