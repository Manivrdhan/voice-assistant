import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia 
import webbrowser
import pywhatkit
import os
import screen_brightness_control as src
import phonenumbers
import requests

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
'print(voices[1].id)'
engine.setProperty('voice',voices[1].id)

def speak(audio):
      engine.say(audio)
      engine.runAndWait()

def wishMe():
     hour = int(datetime.datetime.now().hour)
     if hour>=0 and hour<12:
          speak("Good Morning,had your breakfast?")
     elif hour>=12 and hour<18:
          speak("Good Afternoon,had your lunch?")
     else:
          speak("good Evening,had your snackes")
     speak(" I am shailaja ,srikar's friend how may i help you")

def takeCommand():
     r = sr.Recognizer()
     with sr.Microphone() as source:
          print("Listening...")
          r.energy_threshold = 580
          r.pause_threshold = 0.8
          audio = r.listen(source)
     try:
          print("recognizing..")
          query = r.recognize_google(audio, language='en-in')
          print(f"user said:{query}\n")

     except Exception as e:
          print("say that again please..")
          return "none"
     return query

def sendEmail(to, content):

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('srikarsravan112@gmail.com', 'neenucheppa')
    server.sendmail('srikarsravan112@gmail.com', to, content)
    server.close()




if __name__  == "__main__" :
     speak("Srikar is a good boy")
     wishMe()
     while True:
          query=takeCommand().lower()

          if 'wikipedia' in query:
               speak('Searching Wikipedia...')
               query = query.replace("wikipedia", "")
               results = wikipedia.summary(query, sentences=2)
               speak("According to Wikipedia")
               print(results)
               speak(results)
          elif 'open youtube' in query:
               webbrowser.open("youtube.com")
          elif 'open google' in query:
                webbrowser.open("google.com")
          elif 'play  local music' in query:
                music_dir = 'E:\\local songs\\D'
                songs = os.listdir(music_dir)
                print(songs)
                os.startfile(os.path.join(music_dir, songs[0]))
                speak(songs)
          elif 'song in youtube' in query:
                song = query.replace('play', '')
                speak('playing ' + song)
                pywhatkit.playonyt(song)
          elif 'the time' in query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"sir,the time is {strTime}")
          elif 'send email' in query:
                try:
                      speak("What should I say?")
                      content = takeCommand()
                      to = "srikarsravan112@gmail.com"
                      sendEmail(to, content)
                      speak("Email has been sent!")
                except Exception as e:
                      print(e)
                      speak("Sorry  srikar . I am not able to send this email")

          elif 'increase brightness' in query:
                      src.fade_brightness(0)
                      src.fade_brightness(95, start=0)
                      speak("Brightness is adjusted  , enjoy the day screen light master")

          elif 'decrease brightness' in query:
                      src.fade_brightness(0)
                      src.fade_brightness(25, start=0)
                      speak("Brightness is adjusted , Take care,yourself master")

          elif 'number' in query:
                
                      speak("enter number master")
                      number=input('enter number')
                      from phonenumbers import geocoder
                      ch_number = phonenumbers.parse(number, "CH")
                      i=geocoder.description_for_number(ch_number, "en")
                      print(i)
                      speak("country"+i)
                      from phonenumbers import carrier
                      service_number = phonenumbers.parse(number, "RO")
                      j=carrier.name_for_number(service_number, "en")
                      print(j)
                      speak("sim "+j)

          elif 'current location' in query:
                            res = requests.get('https://ipinfo.io/')
                            data = res.json()
                            city = data['city']
                            location = data['loc'].split(',')
                            latitude = location[0]
                            longitude = location[1]
                            print("Latitude : ", latitude)
                            speak("Latitude" + latitude)
                            print("Longitude : ", longitude)
                            speak("Longitude" + longitude)
                            print("City : ", city)
                            speak("City" + city)

          

          elif ' I love you ' in query:
                speak("i love only srikar")
          elif 'love you shailaja' in query:
                speak("love you too srikar")      


        






               



      
