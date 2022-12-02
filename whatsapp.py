import speech_recognition as sr
import pyttsx3 as p
import datetime
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import pickle

engine = p.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate",150)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
        try:
            recognised_audio = r.recognize_google(audio)
            print("User said: "+recognised_audio)
        except Exception as e:
            speak("Sorry i didn't recognized it")
            recognised_audio2 = takeCommand()
            return recognised_audio2
        return recognised_audio

if __name__=='__main__':

    
    # Opciones de navegación
    options =  webdriver.ChromeOptions()
    options.add_argument('--start-maximized')
    options.add_argument("user-data-dir=selenium") 
    #options.add_experimental_option("detach", True)

    driver_path = 'C:\\Users\\aleja\\Desktop\\Jarvis\\APP\\chromedriver.exe'

    driver = webdriver.Chrome(executable_path=driver_path, options=options)

    # Iniciarla en la pantalla 2
    driver.set_window_position(2000, 0)
    driver.maximize_window()
    time.sleep(1)

    # Inicializamos el navegador
    driver.get('https://web.whatsapp.com/')
    cookies = pickle.load(open("cookies.pkl", "rb"))
    for cookie in cookies:
        driver.add_cookie(cookie)
    #WebDriverWait(driver, 5)\
    #    .until(EC.element_to_be_clickable((By.CSS_SELECTOR,
    #                                      'button.aOOlW.bIiDR'.replace(' ', '.'))))\
    #    .click()

    speak('Who do you want to send a message?')
    nombre = takeCommand().lower()

    time.sleep(5)

    if 'mom' in nombre:
        nombre = 'Mama'
    elif 'father' in nombre:
        nombre = 'Papa'
    elif 'brother' in nombre:
        nombre = 'Iván Cana'
    elif 'sister' in nombre:
        nombre = 'Tata'
    elif 'real g' in nombre:
        nombre = 'Aleme'
    else:
        nombre = 'Notas'


    user = driver.find_element_by_xpath('//span[@title="{}"]'.format(nombre))
    user.click()

    time.sleep(1)

    speak("What's the message?")
    mens = takeCommand()


    message_box = driver.find_element_by_xpath('//div[@class="_2A8P4"]')
    message_box.send_keys(mens)

    time.sleep(2)

    message_box = driver.find_element_by_xpath('//div[@class="EBaI7"]')
    message_box.click()
    pickle.dump(driver.get_cookies(), open("cookies.pkl", "wb"))

    












