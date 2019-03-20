pd1=['programming date is an event of visvesmruti 2k18 managed by computer department which looks for the Real Star Team that stands upto the ability of ACCURACY, SPEED, CO-OPERATION and LOGIC']
pd2=['programming date is coordinated by Professor Hemang Shah']
pd3=['PATEL DEEP and MAHANT HIMANSHU are the student co-ordinator of programming date']
pd4=['programming date is arranged by Computer department']
pd5=['Any student from diploma and degree engineering can take part in programming date']
pd6=['Each participant have to pay fifty rupees',]
pd7=['the participants have to take part individually']
pd8=['round 1 will be are simple programs of c programming , round 2 will contain simple algorithms and programs, round 3 will be the final round and described at the venue']
pd9=['round 1 will be are simple programs on c programming']
pd10=['in second round there a team will be formed containing a boy and a girl and this round will contain simple algorithms and programs.']
pd11=['round 3 will be the final round, top 10 teams will be selected for this round. this round will be descibed at venue.']
pd12=['There are different timing for each round based on the task']
pd13=['round 1 will be of 45 minutes, may be vary']
pd14=['round 2 will be of 1 hour, may  be vary']
pd15=['round 3 will be of 1 hour, may be vary']
pd16=['Judge Decision will be final. Price money of the winner will be divided equally among the 2 members of a winning team']

snl1=['Quiz with Snakes and Ladders is an event of visvesmruti 2k18 managed by computer department which two members of team will give answer to the question asked by coordinator and third member will play the game. if they give the right answer then they will get chance to role the dice else they cannot role.']
snl2=['Miss Niyant Panchal is the faculty coordinator of Quiz with Snakes and Ladders']
snl3=['Javiya Radhika and Darji Karan are the student co-ordinator of Quiz with Snakes and Ladders']
snl4=['Computer department is going to manage the Quiz with Snakes and Ladders event']
snl5=['any student pursuing diploma engineering can participate']
snl6=['the participants have to pay a fee of 150 rupees for a team means 50 rupees per head','Each participant have to pay fifty rupees per head means 150 rupees for a team',]
snl7=['the participant have to take part as the team of 3.']
snl8=['rounds will be decalred at the venue on the event day.']
snl9=['There are different timing for each round based on the task.']
snl10=['quiz with Snakes and ladders is a game. in which two teams will compete in a round. Multiple rounds will be played. team which lead will selected for next round.']

vp1=['Virtual Placement is an event of visvesmruti 2k18 managed by computer department which .']
vp2=['Miss Henita RANA and Miss Bhagyshri Patel are the faculty coordinators of Virtual Placement']
vp3=['Saurabh Jha and Nirmal Patel are the student co-ordinators of Virtual Placement']
vp4=['Virtual Placement is managed by Computer department']
vp5=['Any student from diploma or degree engineering can take part in Virtual Placement']
vp6=['the participants have to pay a fee of 50 rupees']
vp7=['the participant have to take part individually']
vp8=['round one will be aptitude test. round two will be Group Discussion. final round will be Personal Interview.']
vp9=['round 1 is aptitude test. there will be multiple choice questions each carrying 1 mark.']
vp10=['round 2 will be group discussion. the topics will be given on spot. each group will have maximum 12 minutes to represent their views.']
vp11=['round 3 will be personal interview. this round includes technical and human resource interview Questions']
vp12=['There are different timing for each round based on the task']
vp13=['Round 1 will be of 30 minutes.']
vp14=['each group will get maximum 12 minutes to represent their views.']
vp15=['we cannot specify the time for personal interview, it depends on interviewer.']
vp16=['There is not on spot entry for this event. All the participants have to submit their Resume before to appear in virtual placement and for more visit techfest website.']

wd1=['web design is an event of visvesmruti 2k18 managed by computer department which design an attractive Web Page based on the given the using HTML, JavaScript, CSS, extra.']
wd2=['web design is coordinated by Professor Ankit Prajapati.']
wd3=['RITVA VAGHASIYA and HARSH DALAL are the student co-ordinator of web design.']
wd4=['Computer department is going to manage the web design event.']
wd5=['Any student from diploma and degree engineering can take part in web design in a team of 2.']
wd6=['the participants have to pay a fee of 50 rupees per head.']
wd7=['the participant have to take part as the team of 2.']
wd8=['In round 1 there are 5 different types of questions will be given to the participants and they need to complete the task. and In the second round participants need to design website, or webpages based on topic provided by the coordinators using permitted development tools.']
wd9=['In round 1 there are 5 different types of questions will be given to the participants and they need to complete the task.']
wd10=['In the second round participants need to design website. or webpages based on topic provided by the coordinators using permitted development tools.']
wd11=['Each round has been allocated different times','There are different timing for each round based on the task']
wd12=['round 1 will be of around 45 minutes.']
wd13=['round 2 will be of around 75 minutes.']
wd14=['Use of USB drive and Internet is strictly prohibited.']


while(1):
    v=input("Ask something:")
# start of programming date
    if(v.find('programming date')!=-1 or v.find('programming')!=-1 or v.find('Programming')!=-1 or v.find('programming data')!=-1):
        if(v.find('faculty')!=-1):
            print(pd2)
        elif(v.find('student')!=-1):
            print(pd3)
        elif(v.find('department')!=-1):
            print(pd4)
        elif(v.find('criteria')!=-1 or v.find('eligiblity')!=-1 or v.find('eligible')!=-1):
            print(pd5)
        elif(v.find('fee')!=-1 or v.find('ammount')!=-1 or v.find('pay')!=-1 or v.find('Fee')!=-1):
            print(pd6)
        elif(v.find('time')!=-1 or v.find('timing')!=-1):
            if(v.find('round 1')!=-1 or v.find('round one')!=-1):
                print(pd13)
            elif(v.find('round 2')!=-1 or v.find('round two')!=-1):
                print(pd14)
            elif(v.find('round 3')!=-1 or v.find('round three')!=-1):
                print(pd15)
            else:
                print(pd12)
        elif(v.find('describe')!=-1 or v.find('tell')!=-1 or v.find('what')!=-1 or v.find('about')!=-1):
            if(v.find('rule')!=-1):
                print(pd16)
            elif(v.find('round 1')!=-1 or v.find('round one')!=-1):
                print(pd9)
            elif(v.find('round 2')!=-1 or v.find('round two')!=-1):
                print(pd10)
            elif(v.find('round 3')!=-1 or v.find('round three')!=-1):
                print(pd11)
            elif(v.find('round')!=-1):
                print(pd8)
            elif(v.find('team')!=-1 or v.find('number')!=-1 or v.find('group')!=-1 or v.find('individual')!=-1):
                print(pd7)
            else:
                print(pd1)
        elif(v.find('participant')!=-1 or v.find('participate')!=-1):
            if(v.find('team')!=-1 or v.find('number')!=-1 or v.find('group')!=-1 or v.find('individual')!=-1):
                print(pd7)
            else:
                print(pd5)
        else:
            print('I dont get it.')
# end of programming date

# start of quiz with snakes and ladders
    if(v.find('quiz with snakes and ladders')!=-1 or v.find('snakes and ladders')!=-1 or v.find('snake')!=-1 or v.find('ladder')!=-1):
        if(v.find('faculty')!=-1):
            print(snl2)
        elif(v.find('student')!=-1):
            print(snl3)
        elif(v.find('department')!=-1):
            print(snl4)
        elif(v.find('criteria')!=-1 or v.find('eligiblity')!=-1 or v.find('eligible')!=-1):
            print(snl5)
        elif(v.find('fee')!=-1 or v.find('ammount')!=-1 or v.find('pay')!=-1 or v.find('Fee')!=-1):
            print(snl6)
        elif(v.find('time')!=-1 or v.find('timing')!=-1):
            print(snl9)
        elif(v.find('describe')!=-1 or v.find('tell')!=-1 or v.find('what')!=-1 or v.find('about')!=-1):
            if(v.find('rule')!=-1):
                print(snl10)
            elif(v.find('round')!=-1):
                print(snl8)
            elif(v.find('team')!=-1 or v.find('number')!=-1 or v.find('group')!=-1 or v.find('individual')!=-1):
                print(snl7)
            else:
                print(snl1)
        elif(v.find('participant')!=-1 or v.find('participate')!=-1):
            if(v.find('team')!=-1 or v.find('number')!=-1 or v.find('group')!=-1 or v.find('individual')!=-1):
                print(snl7)
            else:
                print(snl5)
        else:
            print('I dont get it.')
# end of quiz with snakes and ladders

# start of virtual placement
    if(v.find('virtual placement')!=-1 or v.find('Virtual Placement')!=-1 or v.find('Virtual placement')!=-1 or v.find('virtual')!=-1 or v.find('placement')!=-1):
        if(v.find('faculty')!=-1):
            print(vp2)
        elif(v.find('student')!=-1):
            print(vp3)
        elif(v.find('department')!=-1):
            print(vp4)
        elif(v.find('criteria')!=-1 or v.find('eligiblity')!=-1 or v.find('eligible')!=-1):
            print(vp5)
        elif(v.find('fee')!=-1 or v.find('ammount')!=-1 or v.find('pay')!=-1 or v.find('Fee')!=-1):
            print(vp6)
        elif(v.find('time')!=-1 or v.find('timing')!=-1):
            if(v.find('round 1')!=-1 or v.find('round one')!=-1 or v.find('aptitude')!=-1):
                print(vp12)
            elif(v.find('round 2')!=-1 or v.find('round two')!=-1 or v.find('discussion')!=-1):
                print(vp14)
            elif(v.find('round 3')!=-1 or v.find('round three')!=-1 or v.find('interview')!=-1):
                print(vp15)
            else:
                print(vp12)
        elif(v.find('describe')!=-1 or v.find('tell')!=-1 or v.find('what')!=-1 or v.find('about')!=-1):
            if(v.find('rule')!=-1):
                print(vp16)
            elif(v.find('round 1')!=-1 or v.find('round one')!=-1 or v.find('aptitute')!=-1):
                print(vp9)
            elif(v.find('round 2')!=-1 or v.find('round two')!=-1 or v.find('discussion')!=-1):
                print(vp10)
            elif(v.find('round 3')!=-1 or v.find('round three')!=-1 or v.find('interview')!=-1):
                print(vp11)
            elif(v.find('round')!=-1):
                print(vp8)
            elif(v.find('team')!=-1 or v.find('number')!=-1 or v.find('group')!=-1 or v.find('individual')!=-1):
                print(vp7)
            else:
                print(vp1)
        elif(v.find('participant')!=-1 or v.find('participate')!=-1):
            if(v.find('team')!=-1 or v.find('number')!=-1 or v.find('group')!=-1 or v.find('individual')!=-1):
                print(vp7)
            else:
                print(vp5)
        else:
            print('I dont get it.')
# end of virtual placement

# start of web design
    if(v.find('web design')!=-1 or v.find('web designing')!=-1 or v.find('design')!=-1 or v.find('web')!=-1):
        if(v.find('faculty')!=-1):
            print(wd2)
        elif(v.find('student')!=-1):
            print(wd3)
        elif(v.find('department')!=-1):
            print(wd4)
        elif(v.find('criteria')!=-1 or v.find('eligiblity')!=-1 or v.find('eligible')!=-1):
            print(wd5)
        elif(v.find('fee')!=-1 or v.find('ammount')!=-1 or v.find('pay')!=-1 or v.find('Fee')!=-1):
            print(wd6)
        elif(v.find('time')!=-1 or v.find('timing')!=-1):
            if(v.find('round 1')!=-1 or v.find('round one')!=-1):
                print(wd12)
            elif(v.find('round 2')!=-1 or v.find('round two')!=-1):
                print(wd13)
            else:
                print(wd11)
        elif(v.find('describe')!=-1 or v.find('tell')!=-1 or v.find('what')!=-1 or v.find('about')!=-1):
            if(v.find('rule')!=-1):
                print(wd14)
            elif(v.find('round 1')!=-1 or v.find('round one')!=-1):
                print(wd9)
            elif(v.find('round 2')!=-1 or v.find('round two')!=-1):
                print(wd10)
            elif(v.find('round')!=-1):
                print(wd8)
            elif(v.find('team')!=-1 or v.find('number')!=-1 or v.find('group')!=-1 or v.find('individual')!=-1):
                print(wd7)
            else:
                print(wd1)
        elif(v.find('participant')!=-1 or v.find('participate')!=-1):
            if(v.find('team')!=-1 or v.find('number')!=-1 or v.find('group')!=-1 or v.find('individual')!=-1):
                print(wd7)
            else:
                print(wd5)
        else:
            print('I dont get it.')
# end of web design
