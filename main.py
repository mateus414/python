import speech_recognition as sr 
import pyttsx3 

audio = sr.Recognizer() 
maquina = pyttsx3.init()
maquina.say("Olá Mateus,Tudo bem")
maquina.say("Eu Sou a Tina,Sua assistente Virtual")
maquina.say("Como Posso Ajudar")
maquina.runAndWait()


try : 
    with sr.Microphone() as source:
        print('Ouvindo..')
        voz = audio.listen(source)
        comando = audio.recognize_google(voz,language='pt-BR')
        comando = comando.lower()

        if "tina" in comando: 
            print(comando)
            maquina.say(comando)
            maquina.runAndWait()


except:
    print ("Microfone não está OK")