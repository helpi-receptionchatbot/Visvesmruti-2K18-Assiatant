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
