import random
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


# elctrical start
# start of  e google
    elif(v.find(' e google')!=-1 or v.find('E google')!=-1 or v.find('Google')!=-1 or v.find('google')!=-1):
        if(v.find('faculty')!=-1):
            os.system("mpg321 sounds/eg2.mp3")
        elif(v.find('student')!=-1):
            os.system("mpg321 sounds/eg3.mp3")
        elif(v.find('department')!=-1):
            os.system("mpg321 sounds/eg4.mp3")
        elif(v.find('criteria')!=-1 or v.find('eligiblity')!=-1 or v.find('eligible')!=-1):
            os.system("mpg321 sounds/eg5.mp3")
        elif(v.find('fee')!=-1 or v.find('ammount')!=-1 or v.find('pay')!=-1 or v.find('Fee')!=-1):
            os.system("mpg321 sounds/eg6.mp3")
        elif(v.find('time')!=-1 or v.find('timing')!=-1):
            os.system("mpg321 sounds/eg12.mp3")
        elif(v.find('describe')!=-1 or v.find('tell')!=-1 or v.find('what')!=-1 or v.find('about')!=-1):
            if(v.find('rule')!=-1):
                os.system("mpg321 sounds/eg13.mp3")
            elif(v.find('round 1')!=-1 or v.find('round one')!=-1):
                os.system("mpg321 sounds/eg9.mp3")
            elif(v.find('round 2')!=-1 or v.find('round two')!=-1):
                os.system("mpg321 sounds/eg10.mp3")
            elif(v.find('round 3')!=-1 or v.find('round three')!=-1):
                os.system("mpg321 sounds/eg11.mp3")
            elif(v.find('round')!=-1):
                os.system("mpg321 sounds/eg8.mp3")
            elif(v.find('team')!=-1 or v.find('number')!=-1 or v.find('group')!=-1 or v.find('individual')!=-1):
                os.system("mpg321 sounds/eg7.mp3")
            else:
                os.system("mpg321 sounds/eg1.mp3")
        elif(v.find('participant')!=-1 or v.find('participate')!=-1):
            if(v.find('team')!=-1 or v.find('number')!=-1 or v.find('group')!=-1 or v.find('individual')!=-1):
                os.system("mpg321 sounds/eg7.mp3")
            else:
                os.system("mpg321 sounds/eg5.mp3")
        else:
            os.system("mpg321 sounds/excep.mp3")
# end of  e google

# start of robo climber
    elif(v.find('robo climber')!=-1 or v.find('Robo Climber')!=-1 or v.find('climber')!=-1 or v.find('Climber')!=-1):
        if(v.find('faculty')!=-1):
            os.system("mpg321 sounds/rc2.mp3")
        elif(v.find('student')!=-1):
            os.system("mpg321 sounds/rc3.mp3")
        elif(v.find('department')!=-1):
            os.system("mpg321 sounds/rc4.mp3")
        elif(v.find('criteria')!=-1 or v.find('eligiblity')!=-1 or v.find('eligible')!=-1):
            os.system("mpg321 sounds/rc5.mp3")
        elif(v.find('fee')!=-1 or v.find('ammount')!=-1 or v.find('pay')!=-1 or v.find('Fee')!=-1):
            os.system("mpg321 sounds/rc6.mp3")
        elif(v.find('time')!=-1 or v.find('timing')!=-1):
            os.system("mpg321 sounds/rc9.mp3")
        elif(v.find('describe')!=-1 or v.find('tell')!=-1 or v.find('what')!=-1 or v.find('about')!=-1):
            if(v.find('rule')!=-1):
                os.system("mpg321 sounds/rc10.mp3")
            elif(v.find('arena')!=-1):
                os.system("mpg321 sounds/rc11.mp3")
            elif(v.find('specification')!=-1):
                os.system("mpg321 sounds/rc12.mp3")
            elif(v.find('round')!=-1):
                os.system("mpg321 sounds/rc8.mp3")
            elif(v.find('team')!=-1 or v.find('number')!=-1 or v.find('group')!=-1 or v.find('individual')!=-1):
                os.system("mpg321 sounds/rc7.mp3")
            else:
                os.system("mpg321 sounds/rc1.mp3")
        elif(v.find('participant')!=-1 or v.find('participate')!=-1):
            if(v.find('team')!=-1 or v.find('number')!=-1 or v.find('group')!=-1 or v.find('individual')!=-1):
                os.system("mpg321 sounds/rc7.mp3")
            else:
                os.system("mpg321 sounds/rc5.mp3")
        else:
            os.system("mpg321 sounds/excep.mp3")
# end of robo climber

# start of robo soccer
    elif(v.find('robo soccer')!=-1 or v.find('Robo Soccer')!=-1 or v.find('Soccer')!=-1 or v.find('soccer')!=-1):
        if(v.find('faculty')!=-1):
            os.system("mpg321 sounds/rs2.mp3")
        elif(v.find('student')!=-1):
            os.system("mpg321 sounds/rs3.mp3")
        elif(v.find('department')!=-1):
            os.system("mpg321 sounds/rs4.mp3")
        elif(v.find('criteria')!=-1 or v.find('eligiblity')!=-1 or v.find('eligible')!=-1):
            os.system("mpg321 sounds/rs5.mp3")
        elif(v.find('fee')!=-1 or v.find('ammount')!=-1 or v.find('pay')!=-1 or v.find('Fee')!=-1):
            os.system("mpg321 sounds/rs6.mp3")
        elif(v.find('time')!=-1 or v.find('timing')!=-1):
            if(v.find('round 1')!=-1 or v.find('round one')!=-1):
                os.system("mpg321 sounds/rs16.mp3")
            elif(v.find('round 2')!=-1 or v.find('round two')!=-1):
                os.system("mpg321 sounds/rs17.mp3")
            elif(v.find('round 3')!=-1 or v.find('round three')!=-1):
                os.system("mpg321 sounds/rs18.mp3")
            elif(v.find('round 4')!=-1 or v.find('round four')!=-1):
                os.system("mpg321 sounds/rs19.mp3")
            elif(v.find('round 5')!=-1 or v.find('round five')!=-1):
                os.system("mpg321 sounds/rs20.mp3")
            elif(v.find('round 6')!=-1 or v.find('round six')!=-1):
                os.system("mpg321 sounds/rs21.mp3")
            else:
                os.system("mpg321 sounds/rs15.mp3")
        elif(v.find('describe')!=-1 or v.find('tell')!=-1 or v.find('what')!=-1 or v.find('about')!=-1):
            if(v.find('rule')!=-1):
                os.system("mpg321 sounds/rs22.mp3")
            elif(v.find('arena')!=-1):
                os.system("mpg321 sounds/rs23.mp3")
            elif(v.find('specification')!=-1):
                os.system("mpg321 sounds/rs24.mp3")
            elif(v.find('round 1')!=-1 or v.find('round one')!=-1):
                os.system("mpg321 sounds/rs9.mp3")
            elif(v.find('round 2')!=-1 or v.find('round two')!=-1):
                os.system("mpg321 sounds/rs10.mp3")
            elif(v.find('round 3')!=-1 or v.find('round three')!=-1):
                os.system("mpg321 sounds/rs11.mp3")
            elif(v.find('round 4')!=-1 or v.find('round four')!=-1):
                os.system("mpg321 sounds/rs12.mp3")
            elif(v.find('round 5')!=-1 or v.find('round five')!=-1):
                os.system("mpg321 sounds/rs13.mp3")
            elif(v.find('round 6')!=-1 or v.find('round six')!=-1):
                os.system("mpg321 sounds/rs14.mp3")
            elif(v.find('round')!=-1):
                os.system("mpg321 sounds/rs8.mp3")
            elif(v.find('team')!=-1 or v.find('number')!=-1 or v.find('group')!=-1 or v.find('individual')!=-1):
                os.system("mpg321 sounds/rs7.mp3")
            else:
                os.system("mpg321 sounds/rs1.mp3")
        elif(v.find('participant')!=-1 or v.find('participate')!=-1):
            if(v.find('team')!=-1 or v.find('number')!=-1 or v.find('group')!=-1 or v.find('individual')!=-1):
                os.system("mpg321 sounds/rs7.mp3")
            else:
                os.system("mpg321 sounds/rs5.mp3")
        else:
            os.system("mpg321 sounds/excep.mp3")
# end of robo soccer


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


# mechanical start
# start of arcania
    elif(v.find('arcania')!=-1 or v.find('Arcania')!=-1 or v.find('arc')!=-1 or v.find('Arc')!=-1):
        if(v.find('faculty')!=-1):
            os.system("mpg321 sounds/arc2.mp3")
        elif(v.find('student')!=-1):
            os.system("mpg321 sounds/arc3.mp3")
        elif(v.find('department')!=-1):
            os.system("mpg321 sounds/arc4.mp3")
        elif(v.find('criteria')!=-1 or v.find('eligiblity')!=-1 or v.find('eligible')!=-1):
            os.system("mpg321 sounds/arc5.mp3")
        elif(v.find('fee')!=-1 or v.find('ammount')!=-1 or v.find('pay')!=-1 or v.find('Fee')!=-1):
            os.system("mpg321 sounds/arc6.mp3")
        elif(v.find('time')!=-1 or v.find('timing')!=-1):
            os.system("mpg321 sounds/arc9.mp3")
        elif(v.find('describe')!=-1 or v.find('tell')!=-1 or v.find('what')!=-1 or v.find('about')!=-1):
            if(v.find('rule')!=-1):
                os.system("mpg321 sounds/arc10.mp3")
            elif(v.find('round')!=-1):
                os.system("mpg321 sounds/arc8.mp3")
            elif(v.find('team')!=-1 or v.find('number')!=-1 or v.find('group')!=-1 or v.find('individual')!=-1):
                os.system("mpg321 sounds/arc7.mp3")
            else:
                os.system("mpg321 sounds/arc1.mp3")
        elif(v.find('participant')!=-1 or v.find('participate')!=-1):
            if(v.find('team')!=-1 or v.find('group')!=-1 or v.find('number')!=-1 or v.find('individual')!=-1):
                os.system("mpg321 sounds/arc7.mp3")
            else:
                os.system("mpg321 sounds/arc5.mp3")
        else:
            os.system("mpg321 sounds/excep.mp3")
# end of arcania

# start of junkyard war
    elif(v.find('junkyard war')!=-1 or v.find('junkyard')!=-1 or v.find('junk')!=-1 or v.find('junk yard')!=-1):
        if(v.find('faculty')!=-1):
            os.system("mpg321 sounds/jyw2.mp3")
        elif(v.find('student')!=-1):
            os.system("mpg321 sounds/jyw3.mp3")
        elif(v.find('department')!=-1):
            os.system("mpg321 sounds/jyw4.mp3")
        elif(v.find('criteria')!=-1 or v.find('eligiblity')!=-1 or v.find('eligible')!=-1):
            os.system("mpg321 sounds/jyw5.mp3")
        elif(v.find('fee')!=-1 or v.find('ammount')!=-1 or v.find('pay')!=-1 or v.find('Fee')!=-1):
            os.system("mpg321 sounds/jyw6.mp3")
        elif(v.find('time')!=-1 or v.find('timing')!=-1):
            os.system("mpg321 sounds/jyw9.mp3")
        elif(v.find('describe')!=-1 or v.find('tell')!=-1 or v.find('what')!=-1 or v.find('about')!=-1):
            if(v.find('rule')!=-1):
                os.system("mpg321 sounds/jyw10.mp3")
            elif(v.find('round')!=-1):
                os.system("mpg321 sounds/jyw8.mp3")
            elif(v.find('team')!=-1 or v.find('number')!=-1 or v.find('group')!=-1 or v.find('individual')!=-1):
                os.system("mpg321 sounds/jyw7.mp3")
            else:
                os.system("mpg321 sounds/jyw1.mp3")
        elif(v.find('participant')!=-1 or v.find('participate')!=-1):
            if(v.find('team')!=-1 or v.find('group')!=-1 or v.find('number')!=-1 or v.find('individual')!=-1):
                os.system("mpg321 sounds/jyw7.mp3")
            else:
                os.system("mpg321 sounds/jyw5.mp3")
        else:
            os.system("mpg321 sounds/excep.mp3")
# end of junkyard war

# start of lathe war
    elif(v.find('lathe war')!=-1 or v.find('lathe')!=-1 or v.find('Lathe')!=-1 or v.find('Lathe war')!=-1):
        if(v.find('faculty')!=-1):
            os.system("mpg321 sounds/le2.mp3")
        elif(v.find('student')!=-1):
            os.system("mpg321 sounds/le3.mp3")
        elif(v.find('department')!=-1):
            os.system("mpg321 sounds/le4.mp3")
        elif(v.find('criteria')!=-1 or v.find('eligiblity')!=-1 or v.find('eligible')!=-1):
            os.system("mpg321 sounds/le5.mp3")
        elif(v.find('fee')!=-1 or v.find('ammount')!=-1 or v.find('pay')!=-1 or v.find('Fee')!=-1):
            os.system("mpg321 sounds/le6.mp3")
        elif(v.find('time')!=-1 or v.find('timing')!=-1):
            os.system("mpg321 sounds/le9.mp3")
        elif(v.find('describe')!=-1 or v.find('tell')!=-1 or v.find('what')!=-1 or v.find('about')!=-1):
            if(v.find('rule')!=-1):
                os.system("mpg321 sounds/le10.mp3")
            elif(v.find('round')!=-1):
                os.system("mpg321 sounds/le8.mp3")
            elif(v.find('team')!=-1 or v.find('number')!=-1 or v.find('group')!=-1 or v.find('individual')!=-1):
                os.system("mpg321 sounds/le7.mp3")
            else:
                os.system("mpg321 sounds/le1.mp3")
        elif(v.find('participant')!=-1 or v.find('participate')!=-1):
            if(v.find('team')!=-1 or v.find('group')!=-1 or v.find('number')!=-1 or v.find('individual')!=-1):
                os.system("mpg321 sounds/le7.mp3")
            else:
                os.system("mpg321 sounds/le5.mp3")
        else:
            os.system("mpg321 sounds/excep.mp3")
# end of lathe war


# civil start
# Start of Bridge Structure
    elif(v.find('bridge structure')!=-1 or v.find('bs')!=-1 or v.find('b s')!=-1 or v.find('Bridge structure')!=-1):
        if(v.find('faculty')!=-1):
            os.system("mpg321 sounds/bs2.mp3")
        elif(v.find('student')!=-1):
            os.system("mpg321 sounds/bs3.mp3")
        elif(v.find('department')!=-1):
            os.system("mpg321 sounds/bs4.mp3")
        elif(v.find('criteria')!=-1 or v.find('eligiblity')!=-1 or v.find('eligible')!=-1):
            os.system("mpg321 sounds/bs5.mp3")
        elif(v.find('fee')!=-1 or v.find('ammount')!=-1 or v.find('pay')!=-1 or v.find('Fee')!=-1):
            os.system("mpg321 sounds/bs6.mp3")
        elif(v.find('time')!=-1 or v.find('timing')!=-1):
            os.system("mpg321 sounds/bs9.mp3")
        elif(v.find('describe')!=-1 or v.find('tell')!=-1 or v.find('what')!=-1 or v.find('about')!=-1):
            if(v.find('rule')!=-1):
                os.system("mpg321 sounds/bs10.mp3")
            elif(v.find('round')!=-1):
                os.system("mpg321 sounds/bs8.mp3")
            elif(v.find('team')!=-1 or v.find('number')!=-1 or v.find('group')!=-1 or v.find('individual')!=-1):
                os.system("mpg321 sounds/bs7.mp3")
            else:
                os.system("mpg321 sounds/bs1.mp3")
        elif(v.find('participant')!=-1 or v.find('participate')!=-1):
            if(v.find('team')!=-1 or v.find('number')!=-1 or v.find('group')!=-1 or v.find('individual')!=-1):
                os.system("mpg321 sounds/bs7.mp3")
            else:
                os.system("mpg321 sounds/bs5.mp3")
        else:
            os.system("mpg321 sounds/excep.mp3")
#end of Bridge Structure

# Start of photomania
    elif(v.find('photomania')!=-1 or v.find('PhotoMania')!=-1 or v.find('photo')!=-1 or v.find('poto')!=-1):
        if(v.find('faculty')!=-1):
            os.system("mpg321 sounds/pm2.mp3")
        elif(v.find('student')!=-1):
            os.system("mpg321 sounds/pm3.mp3")
        elif(v.find('department')!=-1):
            os.system("mpg321 sounds/pm4.mp3")
        elif(v.find('criteria')!=-1 or v.find('eligiblity')!=-1 or v.find('eligible')!=-1):
            os.system("mpg321 sounds/pm5.mp3")
        elif(v.find('fee')!=-1 or v.find('ammount')!=-1 or v.find('pay')!=-1 or v.find('Fee')!=-1):
            os.system("mpg321 sounds/pm6.mp3")
        elif(v.find('time')!=-1 or v.find('timing')!=-1):
            os.system("mpg321 sounds/pm9.mp3")
        elif(v.find('describe')!=-1 or v.find('tell')!=-1 or v.find('what')!=-1 or v.find('about')!=-1):
            if(v.find('rule')!=-1):
                os.system("mpg321 sounds/pm10.mp3")
            elif(v.find('round')!=-1):
                os.system("mpg321 sounds/pm8.mp3")
            elif(v.find('team')!=-1 or v.find('number')!=-1 or v.find('group')!=-1 or v.find('individual')!=-1):
                os.system("mpg321 sounds/pm7.mp3")
            else:
                os.system("mpg321 sounds/pm1.mp3")
        elif(v.find('participant')!=-1 or v.find('participate')!=-1):
            if(v.find('team')!=-1 or v.find('number')!=-1 or v.find('group')!=-1 or v.find('individual')!=-1):
                os.system("mpg321 sounds/pm7.mp3")
            else:
                os.system("mpg321 sounds/pm5.mp3")
        else:
            os.system("mpg321 sounds/excep.mp3")
#end of photomania

# Start of Reveal Me
    elif(v.find('Reveal Me')!=-1 or v.find('Reveal')!=-1 or v.find('reveal')!=-1 or v.find('real me')!=-1 or v.find('Reveal me')!=-1 or v.find('reveal me')!=-1 or v.find('realme')!=-1):
        if(v.find('faculty')!=-1):
            os.system("mpg321 sounds/rm2.mp3")
        elif(v.find('student')!=-1):
            os.system("mpg321 sounds/rm3.mp3")
        elif(v.find('department')!=-1):
            os.system("mpg321 sounds/rm4.mp3")
        elif(v.find('criteria')!=-1 or v.find('eligiblity')!=-1 or v.find('eligible')!=-1):
            os.system("mpg321 sounds/rm5.mp3")
        elif(v.find('fee')!=-1 or v.find('ammount')!=-1 or v.find('pay')!=-1 or v.find('Fee')!=-1):
            os.system("mpg321 sounds/rm6.mp3")
        elif(v.find('time')!=-1 or v.find('timing')!=-1):
            os.system("mpg321 sounds/rm9.mp3")
        elif(v.find('describe')!=-1 or v.find('tell')!=-1 or v.find('what')!=-1 or v.find('about')!=-1):
            if(v.find('rule')!=-1):
                os.system("mpg321 sounds/rm10.mp3")
            elif(v.find('round')!=-1):
                os.system("mpg321 sounds/rm8.mp3")
            elif(v.find('team')!=-1 or v.find('number')!=-1 or v.find('group')!=-1 or v.find('individual')!=-1):
                os.system("mpg321 sounds/rm7.mp3")
            else:
                os.system("mpg321 sounds/rm1.mp3")
        elif(v.find('participant')!=-1 or v.find('participate')!=-1):
            if(v.find('team')!=-1 or v.find('number')!=-1 or v.find('group')!=-1 or v.find('individual')!=-1):
                os.system("mpg321 sounds/rm7.mp3")
            else:
                os.system("mpg321 sounds/rm5.mp3")
        else:
            os.system("mpg321 sounds/excep.mp3")
#end of Reveal Me


# chemical start
# Start of CFA
    elif(v.find('Corrosion Failure Analysis')!=-1 or v.find('cfa')!=-1 or v.find('c f a')!=-1 or v.find('corrosion failure analysist')!=-1):
        if(v.find('faculty')!=-1):
            os.system("mpg321 sounds/cfa2.mp3")
        elif(v.find('student')!=-1):
            os.system("mpg321 sounds/cfa3.mp3")
        elif(v.find('department')!=-1):
            os.system("mpg321 sounds/cfa4.mp3")
        elif(v.find('criteria')!=-1 or v.find('eligiblity')!=-1 or v.find('eligible')!=-1):
            os.system("mpg321 sounds/cfa5.mp3")
        elif(v.find('fee')!=-1 or v.find('ammount')!=-1 or v.find('pay')!=-1 or v.find('Fee')!=-1):
            os.system("mpg321 sounds/cfa6.mp3")
        elif(v.find('time')!=-1 or v.find('timing')!=-1):
            os.system("mpg321 sounds/cfa9.mp3")
        elif(v.find('describe')!=-1 or v.find('tell')!=-1 or v.find('what')!=-1 or v.find('about')!=-1):
            if(v.find('rule')!=-1):
                os.system("mpg321 sounds/cfa10.mp3")
            elif(v.find('round')!=-1):
                os.system("mpg321 sounds/cfa8.mp3")
            elif(v.find('team')!=-1 or v.find('number')!=-1 or v.find('group')!=-1 or v.find('individual')!=-1):
                os.system("mpg321 sounds/cfa7.mp3")
            else:
                os.system("mpg321 sounds/cfa1.mp3")
        elif(v.find('participant')!=-1 or v.find('participate')!=-1):
            if(v.find('team')!=-1 or v.find('number')!=-1 or v.find('group')!=-1 or v.find('individual')!=-1):
                os.system("mpg321 sounds/cfa7.mp3")
            else:
                os.system("mpg321 sounds/cfa5.mp3")
        else:
            os.system("mpg321 sounds/excep.mp3")
#end of CFA

# Start of chem-o-car
    elif(v.find('chemo car')!=-1 or v.find('chem car')!=-1 or v.find('chem cart')!=-1 or v.find('chemo cart')!=-1):
        if(v.find('faculty')!=-1):
            os.system("mpg321 sounds/coc2.mp3")
        elif(v.find('student')!=-1):
            os.system("mpg321 sounds/coc3.mp3")
        elif(v.find('department')!=-1):
            os.system("mpg321 sounds/coc4.mp3")
        elif(v.find('criteria')!=-1 or v.find('eligiblity')!=-1 or v.find('eligible')!=-1):
            os.system("mpg321 sounds/coc5.mp3")
        elif(v.find('fee')!=-1 or v.find('ammount')!=-1 or v.find('pay')!=-1 or v.find('Fee')!=-1):
            os.system("mpg321 sounds/coc6.mp3")
        elif(v.find('time')!=-1 or v.find('timing')!=-1):
            os.system("mpg321 sounds/coc9.mp3")
        elif(v.find('describe')!=-1 or v.find('tell')!=-1 or v.find('what')!=-1 or v.find('about')!=-1):
            if(v.find('rule')!=-1):
                os.system("mpg321 sounds/coc10.mp3")
            elif(v.find('round')!=-1):
                os.system("mpg321 sounds/coc8.mp3")
            elif(v.find('team')!=-1 or v.find('number')!=-1 or v.find('group')!=-1 or v.find('individual')!=-1):
                os.system("mpg321 sounds/coc7.mp3")
            else:
                os.system("mpg321 sounds/coc1.mp3")
        elif(v.find('participant')!=-1 or v.find('participate')!=-1):
            if(v.find('team')!=-1 or v.find('number')!=-1 or v.find('group')!=-1 or v.find('individual')!=-1):
                os.system("mpg321 sounds/coc7.mp3")
            else:
                os.system("mpg321 sounds/coc5.mp3")
        else:
            os.system("mpg321 sounds/excep.mp3")
#end of chem-o-car

# Start of chem-o-missile
    elif(v.find('chemo missile')!=-1 or v.find('chem mis')!=-1 or v.find('chemist')!=-1 or v.find('chemo mis')!=-1):
        if(v.find('faculty')!=-1):
            os.system("mpg321 sounds/co2.mp3")
        elif(v.find('student')!=-1):
            os.system("mpg321 sounds/co3.mp3")
        elif(v.find('department')!=-1):
            os.system("mpg321 sounds/co4.mp3")
        elif(v.find('criteria')!=-1 or v.find('eligiblity')!=-1 or v.find('eligible')!=-1):
            os.system("mpg321 sounds/co5.mp3")
        elif(v.find('fee')!=-1 or v.find('ammount')!=-1 or v.find('pay')!=-1 or v.find('Fee')!=-1):
            os.system("mpg321 sounds/co6.mp3")
        elif(v.find('time')!=-1 or v.find('timing')!=-1):
            os.system("mpg321 sounds/co9.mp3")
        elif(v.find('describe')!=-1 or v.find('tell')!=-1 or v.find('what')!=-1 or v.find('about')!=-1):
            if(v.find('rule')!=-1):
                os.system("mpg321 sounds/co10.mp3")
            elif(v.find('round')!=-1):
                os.system("mpg321 sounds/co8.mp3")
            elif(v.find('team')!=-1 or v.find('number')!=-1 or v.find('group')!=-1 or v.find('individual')!=-1):
                os.system("mpg321 sounds/co7.mp3")
            else:
                os.system("mpg321 sounds/co1.mp3")
        elif(v.find('participant')!=-1 or v.find('participate')!=-1):
            if(v.find('team')!=-1 or v.find('number')!=-1 or v.find('group')!=-1 or v.find('individual')!=-1):
                os.system("mpg321 sounds/co7.mp3")
            else:
                os.system("mpg321 sounds/co5.mp3")
        else:
            os.system("mpg321 sounds/excep.mp3")
#end of chem-o-missile

# Start of Contraption
    elif(v.find('Contraption')!=-1 or v.find('contraption')!=-1):
        if(v.find('faculty')!=-1):
            os.system("mpg321 sounds/cont2.mp3")
        elif(v.find('student')!=-1):
            os.system("mpg321 sounds/cont3.mp3")
        elif(v.find('department')!=-1):
            os.system("mpg321 sounds/cont4.mp3")
        elif(v.find('criteria')!=-1 or v.find('eligiblity')!=-1 or v.find('eligible')!=-1):
            os.system("mpg321 sounds/cont5.mp3")
        elif(v.find('fee')!=-1 or v.find('ammount')!=-1 or v.find('pay')!=-1 or v.find('Fee')!=-1):
            os.system("mpg321 sounds/cont6.mp3")
        elif(v.find('time')!=-1 or v.find('timing')!=-1):
            os.system("mpg321 sounds/cont9.mp3")
        elif(v.find('describe')!=-1 or v.find('tell')!=-1 or v.find('what')!=-1 or v.find('about')!=-1):
            if(v.find('rule')!=-1):
                os.system("mpg321 sounds/cont10.mp3")
            elif(v.find('round')!=-1):
                os.system("mpg321 sounds/cont8.mp3")
            elif(v.find('team')!=-1 or v.find('number')!=-1 or v.find('group')!=-1 or v.find('individual')!=-1):
                os.system("mpg321 sounds/cont7.mp3")
            else:
                os.system("mpg321 sounds/cont1.mp3")
        elif(v.find('participant')!=-1 or v.find('participate')!=-1):
            if(v.find('team')!=-1 or v.find('number')!=-1 or v.find('group')!=-1 or v.find('individual')!=-1):
                os.system("mpg321 sounds/cont7.mp3")
            else:
                os.system("mpg321 sounds/cont5.mp3")
        else:
            os.system("mpg321 sounds/excep.mp3")
#end of Contraption

# Start of chem-o-quiz
    elif(v.find('chemo quiz')!=-1 or v.find('chem quiz')!=-1):
        if(v.find('faculty')!=-1):
            os.system("mpg321 sounds/coq2.mp3")
        elif(v.find('student')!=-1):
            os.system("mpg321 sounds/coq3.mp3")
        elif(v.find('department')!=-1):
            os.system("mpg321 sounds/coq4.mp3")
        elif(v.find('criteria')!=-1 or v.find('eligiblity')!=-1 or v.find('eligible')!=-1):
            os.system("mpg321 sounds/coq5.mp3")
        elif(v.find('fee')!=-1 or v.find('ammount')!=-1 or v.find('pay')!=-1 or v.find('Fee')!=-1):
            os.system("mpg321 sounds/coq6.mp3")
        elif(v.find('time')!=-1 or v.find('timing')!=-1):
            os.system("mpg321 sounds/coq9.mp3")
        elif(v.find('describe')!=-1 or v.find('tell')!=-1 or v.find('what')!=-1 or v.find('about')!=-1):
            if(v.find('rule')!=-1):
                os.system("mpg321 sounds/coq10.mp3")
            elif(v.find('round')!=-1):
                os.system("mpg321 sounds/coq8.mp3")
            elif(v.find('team')!=-1 or v.find('number')!=-1 or v.find('group')!=-1 or v.find('individual')!=-1):
                os.system("mpg321 sounds/coq7.mp3")
            else:
                os.system("mpg321 sounds/coq1.mp3")
        elif(v.find('participant')!=-1 or v.find('participate')!=-1):
            if(v.find('team')!=-1 or v.find('number')!=-1 or v.find('group')!=-1 or v.find('individual')!=-1):
                os.system("mpg321 sounds/coq7.mp3")
            else:
                os.system("mpg321 sounds/coq5.mp3")
        else:
            os.system("mpg321 sounds/excep.mp3")
#end of chem-o-quiz

# start of dexter
    elif(v.find('dexter')!=-1 or v.find('Dexter')!=-1):
        if(v.find('faculty')!=-1):
            os.system("mpg321 sounds/dex2.mp3")
        elif(v.find('student')!=-1):
            os.system("mpg321 sounds/dex2.mp3")
        elif(v.find('department')!=-1):
            os.system("mpg321 sounds/dex4.mp3")
        elif(v.find('criteria')!=-1 or v.find('eligiblity')!=-1 or v.find('eligible')!=-1):
            os.system("mpg321 sounds/dex5.mp3")
        elif(v.find('fee')!=-1 or v.find('ammount')!=-1 or v.find('pay')!=-1 or v.find('Fee')!=-1):
            os.system("mpg321 sounds/dex6.mp3")
        elif(v.find('time')!=-1 or v.find('timing')!=-1):
            if(v.find('round 1')!=-1 or v.find('round one')!=-1):
                os.system("mpg321 sounds/dex15.mp3")
            if(v.find('round 2')!=-1 or v.find('round two')!=-1):
                os.system("mpg321 sounds/dex15.mp3")
            if(v.find('round 3')!=-1 or v.find('round three')!=-1):
                os.system("mpg321 sounds/dex16.mp3")
            if(v.find('round 4')!=-1 or v.find('round four')!=-1):
                os.system("mpg321 sounds/dex17.mp3")
            if(v.find('round 5')!=-1 or v.find('round five')!=-1):
                os.system("mpg321 sounds/dex19.mp3")
            else:
                os.system("mpg321 sounds/dex14.mp3")
        elif(v.find('describe')!=-1 or v.find('tell')!=-1 or v.find('what')!=-1 or v.find('about')!=-1):
            if(v.find('rule')!=-1):
                os.system("mpg321 sounds/dex20.mp3")
            elif(v.find('round 1')!=-1 or v.find('round one')!=-1):
                os.system("mpg321 sounds/dex9.mp3")
            elif(v.find('round 2')!=-1 or v.find('round two')!=-1):
                os.system("mpg321 sounds/dex10.mp3")
            elif(v.find('round 3')!=-1 or v.find('round three')!=-1):
                os.system("mpg321 sounds/dex11.mp3")
            elif(v.find('round 4')!=-1 or v.find('round four')!=-1):
                os.system("mpg321 sounds/dex12.mp3")
            elif(v.find('round 5')!=-1 or v.find('round five')!=-1):
                os.system("mpg321 sounds/dex13.mp3")
            elif(v.find('round')!=-1):
                os.system("mpg321 sounds/dex8.mp3")
            if(v.find('team')!=-1 or v.find('number')!=-1 or v.find('group')!=-1 or v.find('individual')!=-1):
                os.system("mpg321 sounds/dex7.mp3")
            else:
                os.system("mpg321 sounds/dex1.mp3")
        elif(v.find('participant')!=-1 or v.find('participate')!=-1):
            if(v.find('team')!=-1 or v.find('number')!=-1 or v.find('group')!=-1 or v.find('individual')!=-1):
                os.system("mpg321 sounds/dex7.mp3")
            else:
                os.system("mpg321 sounds/dex5.mp3")
        else:
            os.system("mpg321 sounds/excep.mp3")
# end of dexter


# science start
# Start of Elocation Competition
    elif(v.find('Elocation Competition')!=-1 or v.find('Elocation')!=-1 or v.find('elocation')!=-1 or v.find('elocation competition.')!=-1):
        if(v.find('faculty')!=-1):
            os.system("mpg321 sounds/ec2.mp3")
        elif(v.find('student')!=-1):
            os.system("mpg321 sounds/ec3.mp3")
        elif(v.find('department')!=-1):
            os.system("mpg321 sounds/ec4.mp3")
        elif(v.find('criteria')!=-1 or v.find('eligiblity')!=-1 or v.find('eligible')!=-1):
            os.system("mpg321 sounds/ec5.mp3")
        elif(v.find('fee')!=-1 or v.find('ammount')!=-1 or v.find('pay')!=-1 or v.find('Fee')!=-1):
            os.system("mpg321 sounds/ec6.mp3")
        elif(v.find('time')!=-1 or v.find('timing')!=-1):
            os.system("mpg321 sounds/ec9.mp3")
        elif(v.find('describe')!=-1 or v.find('tell')!=-1 or v.find('what')!=-1 or v.find('about')!=-1):
            if(v.find('rule')!=-1):
                os.system("mpg321 sounds/ec10.mp3")
            elif(v.find('round')!=-1):
                os.system("mpg321 sounds/ec8.mp3")
            elif(v.find('team')!=-1 or v.find('number')!=-1 or v.find('group')!=-1 or v.find('individual')!=-1):
                os.system("mpg321 sounds/ec7.mp3")
            else:
                os.system("mpg321 sounds/ec1.mp3")
        elif(v.find('participant')!=-1 or v.find('participate')!=-1):
            if(v.find('team')!=-1 or v.find('number')!=-1 or v.find('group')!=-1 or v.find('individual')!=-1):
                os.system("mpg321 sounds/ec7.mp3")
            else:
                os.system("mpg321 sounds/ec5.mp3")
        else:
            os.system("mpg321 sounds/excep.mp3")
#end of Elocation Competition

# Start of Laser Maniac
    elif(v.find('Laser Maniac')!=-1 or v.find('laser')!=-1 or v.find('mania')!=-1 or v.find('laser mania')!=-1):
        if(v.find('faculty')!=-1):
            os.system("mpg321 sounds/ls2.mp3")
        elif(v.find('student')!=-1):
            os.system("mpg321 sounds/ls3.mp3")
        elif(v.find('department')!=-1):
            os.system("mpg321 sounds/ls4.mp3")
        elif(v.find('criteria')!=-1 or v.find('eligiblity')!=-1 or v.find('eligible')!=-1):
            os.system("mpg321 sounds/ls5.mp3")
        elif(v.find('fee')!=-1 or v.find('ammount')!=-1 or v.find('pay')!=-1 or v.find('Fee')!=-1):
            os.system("mpg321 sounds/ls6.mp3")
        elif(v.find('time')!=-1 or v.find('timing')!=-1):
            os.system("mpg321 sounds/ls9.mp3")
        elif(v.find('describe')!=-1 or v.find('tell')!=-1 or v.find('what')!=-1 or v.find('about')!=-1):
            if(v.find('rule')!=-1):
                os.system("mpg321 sounds/ls10.mp3")
            elif(v.find('round')!=-1):
                os.system("mpg321 sounds/ls8.mp3")
            elif(v.find('team')!=-1 or v.find('number')!=-1 or v.find('group')!=-1 or v.find('individual')!=-1):
                os.system("mpg321 sounds/ls7.mp3")
            else:
                os.system("mpg321 sounds/ls1.mp3")
        elif(v.find('participant')!=-1 or v.find('participate')!=-1):
            if(v.find('team')!=-1 or v.find('number')!=-1 or v.find('group')!=-1 or v.find('individual')!=-1):
                os.system("mpg321 sounds/ls7.mp3")
            else:
                os.system("mpg321 sounds/ls5.mp3")
        else:
            os.system("mpg321 sounds/excep.mp3")
#end of Laser Maniac

# Start of Musing Fizik
    elif(v.find('Musing Fizik')!=-1 or v.find('music')!=-1 or v.find('physic')!=-1 or v.find('musing fizik')!=-1 or v.find('musing')!=-1 or v.find('fizik')!=-1 or v.find('fizic')!=-1):
        if(v.find('faculty')!=-1):
            os.system("mpg321 sounds/mf2.mp3")
        elif(v.find('student')!=-1):
            os.system("mpg321 sounds/mf3.mp3")
        elif(v.find('department')!=-1):
            os.system("mpg321 sounds/mf4.mp3")
        elif(v.find('criteria')!=-1 or v.find('eligiblity')!=-1 or v.find('eligible')!=-1):
            os.system("mpg321 sounds/mf5.mp3")
        elif(v.find('fee')!=-1 or v.find('ammount')!=-1 or v.find('pay')!=-1 or v.find('Fee')!=-1):
            os.system("mpg321 sounds/mf6.mp3")
        elif(v.find('time')!=-1 or v.find('timing')!=-1):
            os.system("mpg321 sounds/mf9.mp3")
        elif(v.find('describe')!=-1 or v.find('tell')!=-1 or v.find('what')!=-1 or v.find('about')!=-1):
            if(v.find('rule')!=-1):
                os.system("mpg321 sounds/mf10.mp3")
            elif(v.find('round')!=-1):
                os.system("mpg321 sounds/mf8.mp3")
            elif(v.find('team')!=-1 or v.find('number')!=-1 or v.find('group')!=-1 or v.find('individual')!=-1):
                os.system("mpg321 sounds/mf7.mp3")
            else:
                os.system("mpg321 sounds/mf1.mp3")
        elif(v.find('participant')!=-1 or v.find('participate')!=-1):
            if(v.find('team')!=-1 or v.find('number')!=-1 or v.find('group')!=-1 or v.find('individual')!=-1):
                os.system("mpg321 sounds/mf7.mp3")
            else:
                os.system("mpg321 sounds/mf5.mp3")
        else:
            os.system("mpg321 sounds/excep.mp3")
#end of Musing Fizik

# Start of Quiz Competition
    elif(v.find('Quiz Competition')!=-1 or v.find('competition')!=-1 or v.find('quiz competition')!=-1 or v.find('quiz')!=-1):
        if(v.find('faculty')!=-1):
            os.system("mpg321 sounds/qc2.mp3")
        elif(v.find('student')!=-1):
            os.system("mpg321 sounds/qc3.mp3")
        elif(v.find('department')!=-1):
            os.system("mpg321 sounds/qc4.mp3")
        elif(v.find('criteria')!=-1 or v.find('eligiblity')!=-1 or v.find('eligible')!=-1):
            os.system("mpg321 sounds/qc5.mp3")
        elif(v.find('fee')!=-1 or v.find('ammount')!=-1 or v.find('pay')!=-1 or v.find('Fee')!=-1):
            os.system("mpg321 sounds/qc6.mp3")
        elif(v.find('time')!=-1 or v.find('timing')!=-1):
            os.system("mpg321 sounds/qc9.mp3")
        elif(v.find('describe')!=-1 or v.find('tell')!=-1 or v.find('what')!=-1 or v.find('about')!=-1):
            if(v.find('rule')!=-1):
                os.system("mpg321 sounds/qc10.mp3")
            elif(v.find('round')!=-1):
                os.system("mpg321 sounds/qc8.mp3")
            elif(v.find('team')!=-1 or v.find('number')!=-1 or v.find('group')!=-1 or v.find('individual')!=-1):
                os.system("mpg321 sounds/qc7.mp3")
            else:
                os.system("mpg321 sounds/qc1.mp3")
        elif(v.find('participant')!=-1 or v.find('participate')!=-1):
            if(v.find('team')!=-1 or v.find('number')!=-1 or v.find('group')!=-1 or v.find('individual')!=-1):
                os.system("mpg321 sounds/qc7.mp3")
            else:
                os.system("mpg321 sounds/qc5.mp3")
        else:
            os.system("mpg321 sounds/excep.mp3")
#end of Quiz Competition


# general start
# start of art gallery
    elif(v.find('art gallery')!=-1 or v.find('art')!=-1 or v.find('gallery')!=-1 or v.find('Art')!=-1):
        if(v.find('faculty')!=-1):
            os.system("mpg321 sounds/art2.mp3")
        elif(v.find('student')!=-1):
            os.system("mpg321 sounds/art3.mp3")
        elif(v.find('department')!=-1):
            os.system("mpg321 sounds/art4.mp3")
        elif(v.find('criteria')!=-1 or v.find('eligiblity')!=-1 or v.find('eligible')!=-1):
            os.system("mpg321 sounds/art5.mp3")
        elif(v.find('fee')!=-1 or v.find('ammount')!=-1 or v.find('pay')!=-1 or v.find('Fee')!=-1):
            os.system("mpg321 sounds/art6.mp3")
        elif(v.find('time')!=-1 or v.find('timing')!=-1):
            os.system("mpg321 sounds/art9.mp3")
        elif(v.find('describe')!=-1 or v.find('tell')!=-1 or v.find('what')!=-1 or v.find('about')!=-1):
            if(v.find('rule')!=-1):
                os.system("mpg321 sounds/art10.mp3")
            elif(v.find('round')!=-1):
                os.system("mpg321 sounds/art8.mp3")
            elif(v.find('team')!=-1 or v.find('number')!=-1 or v.find('group')!=-1 or v.find('individual')!=-1):
                os.system("mpg321 sounds/art7.mp3")
            else:
                os.system("mpg321 sounds/art1.mp3")
        elif(v.find('participant')!=-1 or v.find('participate')!=-1):
            if(v.find('team')!=-1 or v.find('number')!=-1 or v.find('group')!=-1 or v.find('individual')!=-1):
                os.system("mpg321 sounds/art7.mp3")
            else:
                os.system("mpg321 sounds/art5.mp3")
        else:
            os.system("mpg321 sounds/excep.mp3")
# end of art gallery

# start of model presntation
    elif(v.find('model presntation')!=-1 or v.find('model')!=-1 or v.find('Model')!=-1):
        if(v.find('faculty')!=-1):
            if(v.find('civil')!=-1):
                os.system("mpg321 sounds/mop2.mp3")
            elif(v.find('chemical')!=-1):
                os.system("mpg321 sounds/mop3.mp3")
            elif(v.find('electrical')!=-1):
                os.system("mpg321 sounds/mop4.mp3")
            elif(v.find('mechanical')!=-1):
                os.system("mpg321 sounds/mop5.mp3")
        elif(v.find('student')!=-1):
            if(v.find('civil')!=-1):
                os.system("mpg321 sounds/mop6.mp3")
            elif(v.find('chemical')!=-1):
                os.system("mpg321 sounds/mop7.mp3")
            elif(v.find('electrical')!=-1):
                os.system("mpg321 sounds/mop8.mp3")
            elif(v.find('mechanical')!=-1):
                os.system("mpg321 sounds/mop9.mp3")
        elif(v.find('department')!=-1):
            os.system("mpg321 sounds/mop10.mp3")
        elif(v.find('criteria')!=-1 or v.find('eligiblity')!=-1 or v.find('eligible')!=-1):
            os.system("mpg321 sounds/mop11.mp3")
        elif(v.find('fee')!=-1 or v.find('ammount')!=-1 or v.find('pay')!=-1 or v.find('Fee')!=-1):
            os.system("mpg321 sounds/mop12.mp3")
        elif(v.find('time')!=-1 or v.find('timing')!=-1):
            os.system("mpg321 sounds/mop15.mp3")
        elif(v.find('describe')!=-1 or v.find('tell')!=-1 or v.find('what')!=-1 or v.find('about')!=-1):
            if(v.find('rule')!=-1):
                os.system("mpg321 sounds/mop16.mp3")
            elif(v.find('round')!=-1):
                os.system("mpg321 sounds/mop14.mp3")
            elif(v.find('team')!=-1 or v.find('number')!=-1 or v.find('group')!=-1 or v.find('individual')!=-1):
                os.system("mpg321 sounds/mop13.mp3")
            else:
                os.system("mpg321 sounds/mop1.mp3")
        elif(v.find('participant')!=-1 or v.find('participate')!=-1):
            if(v.find('team')!=-1 or v.find('number')!=-1 or v.find('group')!=-1 or v.find('individual')!=-1):
                os.system("mpg321 sounds/mop13.mp3")
            else:
                os.system("mpg321 sounds/mop11.mp3")
        elif(v.find('computer')!=-1):
            os.system("mpg321 sounds/mop17.mp3")
        else:
            os.system("mpg321 sounds/excep.mp3")
# end of model presntation

# start of paper presntation
    elif(v.find('paper presntation')!=-1 or v.find('paper')!=-1 or v.find('Paper')!=-1):
        if(v.find('faculty')!=-1):
            if(v.find('computer')!=-1):
                os.system("mpg321 sounds/pap2.mp3")
            elif(v.find('civil')!=-1):
                os.system("mpg321 sounds/pap3.mp3")
            elif(v.find('chemical')!=-1):
                os.system("mpg321 sounds/pap4.mp3")
            elif(v.find('electrical')!=-1):
                os.system("mpg321 sounds/pap5.mp3")
            elif(v.find('mechanical')!=-1):
                os.system("mpg321 sounds/pap6.mp3")
        elif(v.find('student')!=-1):
            if(v.find('computer')!=-1):
                os.system("mpg321 sounds/pap7.mp3")
            elif(v.find('civil')!=-1):
                os.system("mpg321 sounds/pap8.mp3")
            elif(v.find('chemical')!=-1):
                os.system("mpg321 sounds/pap9.mp3")
            elif(v.find('electrical')!=-1):
                os.system("mpg321 sounds/pap10.mp3")
            elif(v.find('mechanical')!=-1):
                os.system("mpg321 sounds/pap11.mp3")
        elif(v.find('department')!=-1):
            os.system("mpg321 sounds/pap12.mp3")
        elif(v.find('criteria')!=-1 or v.find('eligiblity')!=-1 or v.find('eligible')!=-1):
            os.system("mpg321 sounds/pap13.mp3")
        elif(v.find('fee')!=-1 or v.find('ammount')!=-1 or v.find('pay')!=-1 or v.find('Fee')!=-1):
            os.system("mpg321 sounds/pap14.mp3")
        elif(v.find('time')!=-1 or v.find('timing')!=-1):
            os.system("mpg321 sounds/pap17.mp3")
        elif(v.find('describe')!=-1 or v.find('tell')!=-1 or v.find('what')!=-1 or v.find('about')!=-1):
            if(v.find('rule')!=-1):
                os.system("mpg321 sounds/pap18.mp3")
            elif(v.find('round')!=-1):
                os.system("mpg321 sounds/pap16.mp3")
            elif(v.find('team')!=-1 or v.find('number')!=-1 or v.find('group')!=-1 or v.find('individual')!=-1):
                os.system("mpg321 sounds/pap15.mp3")
            else:
                os.system("mpg321 sounds/pap1.mp3")
        elif(v.find('participant')!=-1 or v.find('participate')!=-1):
            if(v.find('team')!=-1 or v.find('number')!=-1 or v.find('group')!=-1 or v.find('individual')!=-1):
                os.system("mpg321 sounds/pap15.mp3")
            else:
                os.system("mpg321 sounds/pap5.mp3")
        else:
            os.system("mpg321 sounds/excep.mp3")
# end of paper presntation

# start of poster presntation
    elif(v.find('poster presntation')!=-1 or v.find('poster')!=-1 or v.find('Poster')!=-1):
        if(v.find('faculty')!=-1):
            if(v.find('computer')!=-1):
                os.system("mpg321 sounds/pop2.mp3")
            elif(v.find('civil')!=-1):
                os.system("mpg321 sounds/pop3.mp3")
            elif(v.find('chemical')!=-1):
                os.system("mpg321 sounds/pop4.mp3")
            elif(v.find('electrical')!=-1):
                os.system("mpg321 sounds/pop5.mp3")
            elif(v.find('mechanical')!=-1):
                os.system("mpg321 sounds/pop6.mp3")
        elif(v.find('student')!=-1):
            if(v.find('computer')!=-1):
                os.system("mpg321 sounds/pop7.mp3")
            elif(v.find('civil')!=-1):
                os.system("mpg321 sounds/pop8.mp3")
            elif(v.find('chemical')!=-1):
                os.system("mpg321 sounds/pop9.mp3")
            elif(v.find('electrical')!=-1):
                os.system("mpg321 sounds/pop10.mp3")
            elif(v.find('mechanical')!=-1):
                os.system("mpg321 sounds/pop11.mp3")
        elif(v.find('department')!=-1):
            os.system("mpg321 sounds/pop12.mp3")
        elif(v.find('size')!=-1):
            os.system("mpg321 sounds/pop1mp3")
        elif(v.find('criteria')!=-1 or v.find('eligiblity')!=-1 or v.find('eligible')!=-1):
            os.system("mpg321 sounds/pop13.mp3")
        elif(v.find('fee')!=-1 or v.find('ammount')!=-1 or v.find('pay')!=-1 or v.find('Fee')!=-1):
            os.system("mpg321 sounds/pop14.mp3")
        elif(v.find('time')!=-1 or v.find('timing')!=-1):
            os.system("mpg321 sounds/pop17.mp3")
        elif(v.find('describe')!=-1 or v.find('tell')!=-1 or v.find('what')!=-1 or v.find('about')!=-1):
            if(v.find('rule')!=-1):
                os.system("mpg321 sounds/pop18.mp3")
            elif(v.find('round')!=-1):
                os.system("mpg321 sounds/pop16.mp3")
            elif(v.find('team')!=-1 or v.find('number')!=-1 or v.find('group')!=-1 or v.find('individual')!=-1):
                os.system("mpg321 sounds/pop15.mp3")
            else:
                os.system("mpg321 sounds/pop1.mp3")
        elif(v.find('participant')!=-1 or v.find('participate')!=-1):
            if(v.find('team')!=-1 or v.find('number')!=-1 or v.find('group')!=-1 or v.find('individual')!=-1):
                os.system("mpg321 sounds/pop15.mp3")
            else:
                os.system("mpg321 sounds/pop13.mp3")
        else:
            os.system("mpg321 sounds/excep.mp3")
# end of poster presntation


#general quries
    elif(v.find('superintendent')!=-1 or v.find('superint')!=-1 or v.find('Superintendent')!=-1):
        os.system("mpg321 sounds/in1.mp3")
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
