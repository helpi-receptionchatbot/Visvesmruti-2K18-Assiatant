import os
from gtts import gTTS
import speech_recognition as sr


# Record Audio
def Query():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)
        r.adjust_for_ambient_noise(source, duration=1)

    try:
        v = r.recognize_google(audio)
        print("You said: " + v)
        lang='en-in'
    
    except sr.UnknownValueError:
        v = Query();

    return v


def Answer(v):
    if(v.find('certificate')!=-1):
        os.system("mpg321 sounds/g1.mp3")
    elif(v.find('prize')!=-1 or v.find('price')!=-1):
        os.system("mpg321 sounds/g2.mp3")


# computer start
# start of programming date
    elif(v.find('programming date')!=-1 or v.find('programming')!=-1 or v.find('Programming')!=-1 or v.find('programming data')!=-1):
        if(v.find('faculty')!=-1):
            os.system("mpg321 sounds/pd2.mp3")
        elif(v.find('student')!=-1):
            os.system("mpg321 sounds/pd3.mp3")
        elif(v.find('department')!=-1):
            os.system("mpg321 sounds/pd4.mp3")
        elif(v.find('criteria')!=-1 or v.find('eligiblity')!=-1 or v.find('eligible')!=-1):
            os.system("mpg321 sounds/pd5.mp3")
        elif(v.find('fee')!=-1 or v.find('ammount')!=-1 or v.find('pay')!=-1 or v.find('Fee')!=-1):
            os.system("mpg321 sounds/pd6.mp3")
        elif(v.find('time')!=-1 or v.find('timing')!=-1):
            if(v.find('round 1')!=-1 or v.find('round one')!=-1):
                os.system("mpg321 sounds/pd13.mp3")
            elif(v.find('round 2')!=-1 or v.find('round two')!=-1):
                os.system("mpg321 sounds/pd14.mp3")
            elif(v.find('round 3')!=-1 or v.find('round three')!=-1):
                os.system("mpg321 sounds/pd15.mp3")
            else:
                os.system("mpg321 sounds/pd12.mp3")
        elif(v.find('describe')!=-1 or v.find('tell')!=-1 or v.find('what')!=-1 or v.find('about')!=-1):
            if(v.find('rule')!=-1):
                os.system("mpg321 sounds/pd16.mp3")
            elif(v.find('round 1')!=-1 or v.find('round one')!=-1):
                os.system("mpg321 sounds/pd9.mp3")
            elif(v.find('round 2')!=-1 or v.find('round two')!=-1):
                os.system("mpg321 sounds/pd10.mp3")
            elif(v.find('round 3')!=-1 or v.find('round three')!=-1):
                os.system("mpg321 sounds/pd11.mp3")
            elif(v.find('round')!=-1):
                os.system("mpg321 sounds/pd8.mp3")
            elif(v.find('team')!=-1 or v.find('number')!=-1 or v.find('group')!=-1 or v.find('individual')!=-1):
                os.system("mpg321 sounds/pd7.mp3")
            else:
                os.system("mpg321 sounds/pd1.mp3")
        elif(v.find('participant')!=-1 or v.find('participate')!=-1):
            if(v.find('team')!=-1 or v.find('number')!=-1 or v.find('group')!=-1 or v.find('individual')!=-1):
                os.system("mpg321 sounds/pd7.mp3")
            else:
                os.system("mpg321 sounds/pd5.mp3")
        else:
            os.system("mpg321 sounds/excep.mp3")
# end of programming date

# start of quiz with snakes and ladders
    elif(v.find('quiz with snakes and ladders')!=-1 or v.find('snakes and ladders')!=-1 or v.find('snake')!=-1 or v.find('ladder')!=-1):
        if(v.find('faculty')!=-1):
            os.system("mpg321 sounds/snl2.mp3")
        elif(v.find('student')!=-1):
            os.system("mpg321 sounds/snl3.mp3")
        elif(v.find('department')!=-1):
            os.system("mpg321 sounds/snl4.mp3")
        elif(v.find('criteria')!=-1 or v.find('eligiblity')!=-1 or v.find('eligible')!=-1):
            os.system("mpg321 sounds/snl5.mp3")
        elif(v.find('fee')!=-1 or v.find('ammount')!=-1 or v.find('pay')!=-1 or v.find('Fee')!=-1):
            os.system("mpg321 sounds/snl6.mp3")
        elif(v.find('time')!=-1 or v.find('timing')!=-1):
            os.system("mpg321 sounds/snl9.mp3")
        elif(v.find('describe')!=-1 or v.find('tell')!=-1 or v.find('what')!=-1 or v.find('about')!=-1):
            if(v.find('rule')!=-1):
                os.system("mpg321 sounds/snl10.mp3")
            elif(v.find('round')!=-1):
                os.system("mpg321 sounds/snl8.mp3")
            elif(v.find('team')!=-1 or v.find('number')!=-1 or v.find('group')!=-1 or v.find('individual')!=-1):
                os.system("mpg321 sounds/snl7.mp3")
            else:
                os.system("mpg321 sounds/snl1.mp3")
        elif(v.find('participant')!=-1 or v.find('participate')!=-1):
            if(v.find('team')!=-1 or v.find('number')!=-1 or v.find('group')!=-1 or v.find('individual')!=-1):
                os.system("mpg321 sounds/snl7.mp3")
            else:
                os.system("mpg321 sounds/snl5.mp3")
        else:
            os.system("mpg321 sounds/excep.mp3")
# end of quiz with snakes and ladders

# start of virtual placement
    elif(v.find('virtual placement')!=-1 or v.find('Virtual Placement')!=-1 or v.find('Virtual placement')!=-1 or v.find('virtual')!=-1 or v.find('placement')!=-1):
        if(v.find('faculty')!=-1):
            os.system("mpg321 sounds/vp2.mp3")
        elif(v.find('student')!=-1):
            os.system("mpg321 sounds/vp3.mp3")
        elif(v.find('department')!=-1):
            os.system("mpg321 sounds/vp4.mp3")
        elif(v.find('criteria')!=-1 or v.find('eligiblity')!=-1 or v.find('eligible')!=-1):
            os.system("mpg321 sounds/vp5.mp3")
        elif(v.find('fee')!=-1 or v.find('ammount')!=-1 or v.find('pay')!=-1 or v.find('Fee')!=-1):
            os.system("mpg321 sounds/vp6.mp3")
        elif(v.find('time')!=-1 or v.find('timing')!=-1):
            if(v.find('round 1')!=-1 or v.find('round one')!=-1 or v.find('aptitude')!=-1):
                os.system("mpg321 sounds/vp12.mp3")
            elif(v.find('round 2')!=-1 or v.find('round two')!=-1 or v.find('discussion')!=-1):
                os.system("mpg321 sounds/vp14.mp3")
            elif(v.find('round 3')!=-1 or v.find('round three')!=-1 or v.find('interview')!=-1):
                os.system("mpg321 sounds/vp15.mp3")
            else:
                os.system("mpg321 sounds/vp12.mp3")
        elif(v.find('describe')!=-1 or v.find('tell')!=-1 or v.find('what')!=-1 or v.find('about')!=-1):
            if(v.find('rule')!=-1):
                os.system("mpg321 sounds/vp16.mp3")
            elif(v.find('round 1')!=-1 or v.find('round one')!=-1 or v.find('aptitute')!=-1):
                os.system("mpg321 sounds/vp9.mp3")
            elif(v.find('round 2')!=-1 or v.find('round two')!=-1 or v.find('discussion')!=-1):
                os.system("mpg321 sounds/vp10.mp3")
            elif(v.find('round 3')!=-1 or v.find('round three')!=-1 or v.find('interview')!=-1):
                os.system("mpg321 sounds/vp11.mp3")
            elif(v.find('round')!=-1):
                os.system("mpg321 sounds/vp8.mp3")
            elif(v.find('team')!=-1 or v.find('number')!=-1 or v.find('group')!=-1 or v.find('individual')!=-1):
                os.system("mpg321 sounds/vp7.mp3")
            else:
                os.system("mpg321 sounds/vp1.mp3")
        elif(v.find('participant')!=-1 or v.find('participate')!=-1):
            if(v.find('team')!=-1 or v.find('number')!=-1 or v.find('group')!=-1 or v.find('individual')!=-1):
                os.system("mpg321 sounds/vp7.mp3")
            else:
                os.system("mpg321 sounds/vp5.mp3")
        else:
            os.system("mpg321 sounds/excep.mp3")
# end of virtual placement

# start of web design
    elif(v.find('web design')!=-1 or v.find('web designing')!=-1 or v.find('design')!=-1 or v.find('web')!=-1):
        if(v.find('faculty')!=-1):
            os.system("mpg321 sounds/wd2.mp3")
        elif(v.find('student')!=-1):
            os.system("mpg321 sounds/wd3.mp3")
        elif(v.find('department')!=-1):
            os.system("mpg321 sounds/wd4.mp3")
        elif(v.find('criteria')!=-1 or v.find('eligiblity')!=-1 or v.find('eligible')!=-1):
            os.system("mpg321 sounds/wd5.mp3")
        elif(v.find('fee')!=-1 or v.find('ammount')!=-1 or v.find('pay')!=-1 or v.find('Fee')!=-1):
            os.system("mpg321 sounds/wd6.mp3")
        elif(v.find('time')!=-1 or v.find('timing')!=-1):
            if(v.find('round 1')!=-1 or v.find('round one')!=-1):
                os.system("mpg321 sounds/wd12.mp3")
            elif(v.find('round 2')!=-1 or v.find('round two')!=-1):
                os.system("mpg321 sounds/wd13.mp3")
            else:
                os.system("mpg321 sounds/wd11.mp3")
        elif(v.find('describe')!=-1 or v.find('tell')!=-1 or v.find('what')!=-1 or v.find('about')!=-1):
            if(v.find('rule')!=-1):
                os.system("mpg321 sounds/wd14.mp3")
            elif(v.find('round 1')!=-1 or v.find('round one')!=-1):
                os.system("mpg321 sounds/wd9.mp3")
            elif(v.find('round 2')!=-1 or v.find('round two')!=-1):
                os.system("mpg321 sounds/wd10.mp3")
            elif(v.find('round')!=-1):
                os.system("mpg321 sounds/wd8.mp3")
            elif(v.find('team')!=-1 or v.find('number')!=-1 or v.find('group')!=-1 or v.find('individual')!=-1):
                os.system("mpg321 sounds/wd7.mp3")
            else:
                os.system("mpg321 sounds/wd1.mp3")
        elif(v.find('participant')!=-1 or v.find('participate')!=-1):
            if(v.find('team')!=-1 or v.find('number')!=-1 or v.find('group')!=-1 or v.find('individual')!=-1):
                os.system("mpg321 sounds/wd7.mp3")
            else:
                os.system("mpg321 sounds/wd5.mp3")
        else:
            os.system("mpg321 sounds/excep.mp3")
# end of web design



#general quries
    elif(v.find('principal')!=-1 or v.find('principle')!=-1 or v.find('princi')!=-1):
        os.system("mpg321 sounds/in2.mp3")
    elif(v.find('head')!=-1 or v.find('HOD')!=-1 or v.find('H O D')!=-1 or v.find('hod')!=-1):
        if(v.find('computer')!=-1 or v.find('Computer')!=-1):
            os.system("mpg321 sounds/in3.mp3")
        elif(v.find('civil')!=-1 or v.find('Civil')!=-1):
            os.system("mpg321 sounds/in4.mp3")
        elif(v.find('chemical')!=-1 or v.find('Chemical')!=-1):
            os.system("mpg321 sounds/in5.mp3")
        elif(v.find('mechanical')!=-1 or v.find('Mechanical')!=-1):
            os.system("mpg321 sounds/in6.mp3")
        elif(v.find('electrical')!=-1 or v.find('Electrical')!=-1):
            os.system("mpg321 sounds/in7.mp3")
        elif(v.find('science')!=-1 or v.find('Science')!=-1):
            os.system("mpg321 sounds/in8.mp3")
    elif(v.find('hello')!=-1 or v.find('hi there')!=-1 or v.find('hello bot')!=-1 or v.find('hey')!=-1):
        os.system("mpg321 sounds/f1.mp3")
    elif(v.find('how are you')!=-1 or v.find('how you')!=-1 or v.find('are you ok')!=-1 or v.find('are you fine')!=-1):
        os.system("mpg321 sounds/f2.mp3")
    elif(v.find('superintendent')!=-1 or v.find('superint')!=-1 or v.find('Superintendent')!=-1):
        os.system("mpg321 sounds/in1.mp3")
    elif(v.find('hello')!=-1 or v.find('hi there')!=-1 or v.find('hello bot')!=-1 or v.find('hey')!=-1):
        os.system("mpg321 sounds/f1.mp3")
    elif(v.find('how are you')!=-1 or v.find('how you')!=-1 or v.find('are you ok')!=-1 or v.find('are you fine')!=-1):
        os.system("mpg321 sounds/f2.mp3")
    elif(v.find('computer')!=-1 and v.find('events')!=-1):
        os.system("mpg321 sounds/e1.mp3")
    elif(v.find('civil')!=-1 and v.find('events')!=-1):
        os.system("mpg321 sounds/e2.mp3")
    elif(v.find('chemical')!=-1 and v.find('events')!=-1):
        os.system("mpg321 sounds/e3.mp3")
    elif(v.find('electrical')!=-1 and v.find('events')!=-1):
        os.system("mpg321 sounds/e4.mp3")
    elif(v.find('mechanical')!=-1 and v.find('events')!=-1):
        os.system("mpg321 sounds/e5.mp3")
    elif(v.find('science')!=-1 and v.find('events')!=-1):
        os.system("mpg321 sounds/e6.mp3")
    elif(v.find('computer')!=-1 and v.find('technical')!=-1):
        os.system("mpg321 sounds/vs1.mp3")
    elif(v.find('civil')!=-1 and v.find('technical')!=-1):
        os.system("mpg321 sounds/vs2.mp3")
    elif(v.find('chemical')!=-1 and v.find('technical')!=-1):
        os.system("mpg321 sounds/vs3.mp3")
    elif(v.find('electrical')!=-1 and v.find('technical')!=-1):
        os.system("mpg321 sounds/vs4.mp3")
    elif(v.find('mechanical')!=-1 and v.find('technical')!=-1):
        os.system("mpg321 sounds/vs5.mp3")
    elif(v.find('science')!=-1 and v.find('technical')!=-1):
        os.system("mpg321 sounds/vs6.mp3")
    elif(v.find('central')!=-1 or v.find('coordinator')!=-1 or v.find('technical')!=-1):
        os.system("mpg321 sounds/vs7.mp3")
        os.system("mpg321 sounds/vs8.mp3")
    elif(v.find('chief')!=-1 and v.find('patron')!=-1):
        os.system("mpg321 sounds/vs9.mp3")
    elif(v.find('visvesmruti')!=-1 or v.find('visva')!=-1 or v.find('vishva')!=-1 or v.find('smruti')!=-1 or v.find('Visvesmruti')!=-1):
        os.system("mpg321 sounds/vs10.mp3")
    else:
        os.system("mpg321 sounds/ex.mp3")


def wakeword():
    w=''
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say Something:")
        audio = r.listen(source)
        r.adjust_for_ambient_noise(source, duration=1)
    
    try:
        w = r.recognize_google(audio)
        print("You said: " + w)
        lang='hi'

    except sr.UnknownValueError:
        print("a")

    if(w.find('LP')!=-1 or w.find('helpi')!=-1 or w.find('lp')!=-1 or w.find('Lp')!=-1 or w.find('lP')!=-1 or w.find('helpi')!=-1 or w.find('helpme')!=-1 or w.find('help me')!=-1 or w.find('help')!=-1 or w.find('healthy')!=-1):
        return 1;
    else:
        return 0;

    

while True:
    t=wakeword()
    i=4
    if(t):
        os.system("mpg321 waketune.mp3")
        os.system("mpg321 wakeword.mp3")
        while(i>0):
            v=Query()
            if(v==None):
                i=i-1
                sleep(1)
            elif(v.find('thank')!=-1 or v.find('Thank')!=-1 or v.find('bye')!=-1 or v.find('Bye')!=-1 or v.find('bike')!=-1 or v.find('Bike')!=-1 or v.find('buy')!=-1):
                i=0;
                os.system("mpg321 sounds/f3.mp3")
            elif(v.find('LP')!=-1 or v.find('helpi')!=-1 or v.find('lp')!=-1 or v.find('Lp')!=-1 or v.find('lP')!=-1 or v.find('helpi')!=-1 or v.find('helpme')!=-1 or v.find('help me')!=-1 or v.find('help')!=-1 or v.find('healthy')!=-1):
                os.system("mpg321 waketune.mp3")
                os.system("mpg321 wakeword.mp3")
                Answer(Query())
                i=4
            else:
                Answer(v);
