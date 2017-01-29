from gtts import gTTS
import serial
import pyttsx
import os
ser = serial.Serial('/dev/ttyACM0', 9600)
engine = pyttsx.init()
while True:
    num = int(ser.read(1))
    num = int(ser.read(1))
    num = int(ser.read(1)) 
    print num
    left = num & (1<<2)
    right = num & (1<<1)
    center = num & 01
    print left,center,right
    if left and right and center:
        #engine = pyttsx.init()
        #engine.say('No path ahead.')
        tts = gTTS(text='No path. Move back', lang='en')
        tts.save("good.mp3")
        os.system("mpg321 good.mp3")
        #engine.runAndWait()
    elif left and right:
        #engine = pyttsx.init()
        #engine.say('Continue straight.')
        tts = gTTS(text='Continue straight.', lang='en')
        tts.save("good.mp3")
        os.system("mpg321 good.mp3")
        #engine.runAndWait()
    elif left and center:
        tts = gTTS(text='Move Right.', lang='en')
        tts.save("good.mp3")
        os.system("mpg321 good.mp3")
    elif center and right:
        tts = gTTS(text='Move Left.', lang='en')
        tts.save("good.mp3")
        os.system("mpg321 good.mp3")
    elif left:
        #engine = pyttsx.init()
        #engine.say('Obsticle left.')
        tts = gTTS(text='Obstacle left.', lang='en')
        tts.save("good.mp3")
        os.system("mpg321 good.mp3")
        #engine.runAndWait()
    elif center:
        #engine = pyttsx.init()
        #engine.say('Obsticle left.')
        tts = gTTS(text='Obstacle ahead.', lang='en')
        tts.save("good.mp3")
        os.system("mpg321 good.mp3")
        #engine.runAndWait()
    elif right:
        #engine = pyttsx.init()
        #engine.say('Obsticle right.')
        tts = gTTS(text='Obstacle right.', lang='en')
        tts.save("good.mp3")
        os.system("mpg321 good.mp3")
        #engine.runAndWait()
