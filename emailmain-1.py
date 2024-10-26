#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Administrator
#
# Created:     27/01/2024
# Copyright:   (c) Administrator 2024
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import smtplib
import speech_recognition as sr
import pyttsx3  # Text-to-speech library

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        text = recognizer.recognize_google(audio)
        text= text.replace("at the rate","@").replace("dash","-")
        text=text.strip()
        text=text.replace(" ","")
        text=text.lower()
        print("You said:", text)
        return text
    except sr.UnknownValueError:
        print("Could not understand audio.")
        return None
    except sr.RequestError as e:
        print("Error with the speech recognition service; {0}".format(e))
        return None

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

#def send_email(sender_email, sender_password, to_email, subject, body):
    #message = f"Subject: {subject}\n\n{body}"
def send_email(to_email, subject, body):
    sender_email="mrudulaligade05@gmail.com"
    sender_password= "pcnt xivo html jxoy"
    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            message = f"Subject: {subject}\n\n{body}"
            server.sendmail(sender_email, to_email, message)
        speak("Email sent successfully!")
        print("Email sent sucessfully!")

    except Exception as e:
        speak("error sending email")
        print("Error sending email: {e}")
        


'''    # Get sender's email address
    print("Please say the sender's email address:")
    speak("Please say the sender's email address:")
    sender_email = listen()
    if not sender_email:
        print("Exiting.")
        return
    speak(f"You said the sender's email address is {sender_email}")

    # Get sender's email password
    print("Please say the sender's email password:")
    speak("Please say the sender's email password:")
    sender_password = listen()
    if not sender_password:
        print("Exiting.")
        return
    speak("You said the sender's email password.")'''
def main():
    print("Email Voice Assistant")

    # Get recipient's email address
    print("Please say the recipient's email address:")
    speak("Please say the recipient's email address:")
    to_email = listen()
    if not to_email:
        print("Exiting.")
        return
    speak(f"You said the recipient's email address is {to_email}")

    # Get email subject
    speak("Please say the email subject:")
    subject = listen()
    if not subject:
        print("Exiting.")
        return
    speak(f"You said the email subject is {subject}")

    # Get email body
    speak("Please say the email body:")
    body = listen()
    if not body:
        print("Exiting.")
        return
    speak(f"You said the email body is {body}")

    # Send the email
    send_email(to_email, subject, body)

if __name__ == "__main__":
    main()
