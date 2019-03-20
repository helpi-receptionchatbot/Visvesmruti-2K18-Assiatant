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
