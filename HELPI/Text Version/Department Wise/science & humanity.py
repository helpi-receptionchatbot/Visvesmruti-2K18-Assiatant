ec1=['Elocation Competition is an event of visvesmruti 2k18 managed by Science And Humanity department in which Paricipants have to showcase the skill of clear and expressive speech, especially of distinct pronunciation and articulation']
ec2=['Elocation Competition will be coordinated by Professor Tripti Desai.']
ec3=[]
ec4=['Science And Humanity department is going to manage the Elocation Competition event.']
ec5=['Any student from first year of degree engineering can take part in Elocation Competition']
ec6=['the participants have to pay a fee of rupees fifty per head.']
ec7=['the participant have to take part individually']
ec8=['this event consist 1 round only in which you have to show the skill of clear and expressive speech, especially of distinct pronunciation and articulation']
ec9=['you will get maximum 7 minutes to complete the speech.']
ec10=['Contestant can give his/her speech in Gujarati, Hindi, or English. Contestant cannot carry paper of content at the time of Competition']

ls1=['Laser Maniac is an event of visvesmruti 2k18 managed by Science And Humanity department in which Participants have to perform task using laser with limited time']
ls2=['Laser Maniac will be coordinated by Doctor Mehul Mangrola']
ls3=[]
ls4=['Science And Humanity department is going to manage the Laser Maniac event']
ls5=['Any student from first year of degree engineering can take part in Laser Maniac']
ls6=['the participants have to pay a fee of rupees fifty per head.']
ls7=['the participant have to take part as a team of 4']
ls8=['this event consist 1 round only in which Guide laser light starting to ending point using mirror.']
ls9=['you will get maximum 3 minutes to complete the task.']
ls10=['Guided laser light starting to ending point using mirror. Task should be completed within 3 minute.']

mf1=['Musing Fizik is an event of visvesmruti 2k18 managed by Science And Humanity department in which Participants have to prepare a Working model on the base of fundamental law of science and technology.']
mf2=['Musing Fizik will be coordinated by Doctor Mehul Mangrola']
mf3=[]
mf4=['Science And Humanity department is going to manage the Musing Fizik event']
mf5=['Any student from first year of degree engineering can take part in Musing Fizik.']
mf6=['the participants have to pay a fee of rupees fifty per person.']
mf7=['the participant have to take part as a team of maximum 6.']
mf8=['this event consist 1 round only in which participants have to represent their models.']
mf9=['this event will run for 2 days all the time.']
mf10=['Readymade models are not allowed.']

qc1=['Quiz Competition is an event of visvesmruti 2k18 managed by Science And Humanity department in which Participants have to solve Quiz Competition based on General Knowledge , Maths, Physics, English, Computer']
qc2=['Laser Maniac will be coordinated by Professor Harsh Naik']
qc3=[]
qc4=['Science And Humanity department is going to manage the Quiz Competition event']
qc5=['Any student from first year of degree engineering can take part in Quiz Competition']
qc6=['the participants have to pay a fee of rupees fifty per person.']
qc7=['the participant have to take part as a team of 4.']
qc8=['this event consist 1 round only named written test']
qc9=['time will be given at the venue of event.']
qc10=['Participants shall not be allowed to use mobile or any electronic gadgets. The questions shall be in the form of multiple choices. 1 team from each department will be selected and they will represent their departments.']


while(1):
    v=input("Ask something:")
# Start of Elocation Competition
    if(v.find('Elocation Competition')!=-1 or v.find('Elocation')!=-1 or v.find('elocation')!=-1 or v.find('elocation competition.')!=-1):
        if(v.find('faculty')!=-1):
            print(ec2)
        elif(v.find('student')!=-1):
            print(ec2)
        elif(v.find('department')!=-1):
            print(ec4)
        elif(v.find('criteria')!=-1 or v.find('eligiblity')!=-1 or v.find('eligible')!=-1):
            print(ec5)
        elif(v.find('fee')!=-1 or v.find('ammount')!=-1 or v.find('pay')!=-1 or v.find('Fee')!=-1):
            print(ec6)
        elif(v.find('time')!=-1 or v.find('timing')!=-1):
            print(ec9)
        elif(v.find('describe')!=-1 or v.find('tell')!=-1 or v.find('what')!=-1 or v.find('about')!=-1):
            if(v.find('rule')!=-1):
                print(ec10)
            elif(v.find('round')!=-1):
                print(ec8)
            elif(v.find('team')!=-1 or v.find('number')!=-1 or v.find('group')!=-1 or v.find('individual')!=-1):
                print(ec7)
            else:
                print(ec1)
        elif(v.find('participant')!=-1 or v.find('participate')!=-1):
            if(v.find('team')!=-1 or v.find('number')!=-1 or v.find('group')!=-1 or v.find('individual')!=-1):
                print(ec7)
            else:
                print(ec5)
        else:
            print('I don\'t get it.')
#end of Elocation Competition

# Start of Laser Maniac
    if(v.find('Laser Maniac')!=-1 or v.find('laser')!=-1 or v.find('mania')!=-1 or v.find('laser mania')!=-1):
        if(v.find('faculty')!=-1):
            print(ls2)
        elif(v.find('student')!=-1):
            print(ls2)
        elif(v.find('department')!=-1):
            print(ls4)
        elif(v.find('criteria')!=-1 or v.find('eligiblity')!=-1 or v.find('eligible')!=-1):
            print(ls5)
        elif(v.find('fee')!=-1 or v.find('ammount')!=-1 or v.find('pay')!=-1 or v.find('Fee')!=-1):
            print(ls6)
        elif(v.find('time')!=-1 or v.find('timing')!=-1):
            print(ls9)
        elif(v.find('describe')!=-1 or v.find('tell')!=-1 or v.find('what')!=-1 or v.find('about')!=-1):
            if(v.find('rule')!=-1):
                print(ls10)
            elif(v.find('round')!=-1):
                print(ls8)
            elif(v.find('team')!=-1 or v.find('number')!=-1 or v.find('group')!=-1 or v.find('individual')!=-1):
                print(ls7)
            else:
                print(ls1)
        elif(v.find('participant')!=-1 or v.find('participate')!=-1):
            if(v.find('team')!=-1 or v.find('number')!=-1 or v.find('group')!=-1 or v.find('individual')!=-1):
                print(ls7)
            else:
                print(ls5)
        else:
            print('I don\'t get it.')
#end of Laser Maniac

# Start of Musing Fizik
    if(v.find('Musing Fizik')!=-1 or v.find('music')!=-1 or v.find('physic')!=-1 or v.find('musing fizik')!=-1 or v.find('musing')!=-1 or v.find('fizik')!=-1 or v.find('fizic')!=-1):
        if(v.find('faculty')!=-1):
            print(mf2)
        elif(v.find('student')!=-1):
            print(mf2)
        elif(v.find('department')!=-1):
            print(mf4)
        elif(v.find('criteria')!=-1 or v.find('eligiblity')!=-1 or v.find('eligible')!=-1):
            print(mf5)
        elif(v.find('fee')!=-1 or v.find('ammount')!=-1 or v.find('pay')!=-1 or v.find('Fee')!=-1):
            print(mf6)
        elif(v.find('time')!=-1 or v.find('timing')!=-1):
            print(mf9)
        elif(v.find('describe')!=-1 or v.find('tell')!=-1 or v.find('what')!=-1 or v.find('about')!=-1):
            if(v.find('rule')!=-1):
                print(mf10)
            elif(v.find('round')!=-1):
                print(mf8)
            elif(v.find('team')!=-1 or v.find('number')!=-1 or v.find('group')!=-1 or v.find('individual')!=-1):
                print(mf7)
            else:
                print(mf1)
        elif(v.find('participant')!=-1 or v.find('participate')!=-1):
            if(v.find('team')!=-1 or v.find('number')!=-1 or v.find('group')!=-1 or v.find('individual')!=-1):
                print(mf7)
            else:
                print(mf5)
        else:
            print('I don\'t get it.')
#end of Musing Fizik

# Start of Quiz Competition
    if(v.find('Quiz Competition')!=-1 or v.find('competition')!=-1 or v.find('quiz competition')!=-1 or v.find('quiz')!=-1):
        if(v.find('faculty')!=-1):
            print(qc2)
        elif(v.find('student')!=-1):
            print(qc2)
        elif(v.find('department')!=-1):
            print(qc4)
        elif(v.find('criteria')!=-1 or v.find('eligiblity')!=-1 or v.find('eligible')!=-1):
            print(qc5)
        elif(v.find('fee')!=-1 or v.find('ammount')!=-1 or v.find('pay')!=-1 or v.find('Fee')!=-1):
            print(qc6)
        elif(v.find('time')!=-1 or v.find('timing')!=-1):
            print(qc9)
        elif(v.find('describe')!=-1 or v.find('tell')!=-1 or v.find('what')!=-1 or v.find('about')!=-1):
            if(v.find('rule')!=-1):
                print(qc10)
            elif(v.find('round')!=-1):
                print(qc8)
            elif(v.find('team')!=-1 or v.find('number')!=-1 or v.find('group')!=-1 or v.find('individual')!=-1):
                print(qc7)
            else:
                print(qc1)
        elif(v.find('participant')!=-1 or v.find('participate')!=-1):
            if(v.find('team')!=-1 or v.find('number')!=-1 or v.find('group')!=-1 or v.find('individual')!=-1):
                print(qc7)
            else:
                print(qc5)
        else:
            print('I don\'t get it.')
#end of Quiz Competition
