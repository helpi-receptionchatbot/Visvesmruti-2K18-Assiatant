arc1=['Arcania is an event of visvesmruti 2k18 managed by mechanical department in which the participants will be given a set of technical and non-technical questions as well as games to check their knowledge around the world.']
arc2=['Arcania will be co-ordinated by Professor Hardik Nayak']
arc3=['students coordinators are Akash Yadav and Divyesh Patil']
arc4=['mechanical department is going to manage the Arcania event']
arc5=['Any student from diploma and degree engineering can take part in Arcania']
arc6=['the participants have to pay a fee of rupees 200 per team']
arc7=['the participant have to take part in team of 4 persons']
arc8=['Teaser round, Technical & Non-Technical Questions and Bonus Round, Surprise Round are the rounds of Arcania event. and for more you may visit our techfest website.']
arc9=['timming and the tasks will be given at the venue']

jyw1=['Junkyard War is an event of our techfest managed by mechanical department in which Participants have to build a working model from the junk provided to their team.']
jyw2=['Junkyard War will be co-ordinated by Professor Hardik Nayak']
jyw3=['Student Coordinators of junkyard war are PANCHAL JENISH and MISTRY ROHAN']
jyw4=['mechanical department is going manage the Junkyard War event']
jyw5=['Any student from diploma and degree engineering can take part in Junkyard War']
jyw6=['the participants have to pay a fee of rupees 200 per team']
jyw7=['the participant have to take part as the team of 4']
jyw8=['rounds will be described at the venue. or you can visit our techfest website.']
jyw9=['timing and the tasks will be given at the venue. or you can visit our techfest website.']
jyw10=['Teams are expected to have a basic knowledge how over working principles of design and fabrication works, Teams must have 1 project leader, 1 design expert and 2 members as the fabrication unit. for more visit techfest website.']

lw1=['Lathe War is an event of visvesmruti 2k18 managed by mechanical department in which Participants have to prepare a vehicle propellants system which may run by merely any mechanical reaction.']
lw2=['Lathe War will be co-ordinated by Professor Hardik Nayak']
lw3=['Student Coordinators are PATEL JAY and PATEL Viral']
lw4=['Lathe War is managed by mechanical department']
lw5=['any student pursuing diploma engineering can participate in Lathe War']
lw6=['the participants have to pay a fee of rupees fifty per person']
lw7=['the participant have to take part as a team of 2']
lw8=['rounds will be described at the venue']
lw9=['timming and the tasks will be given at the venue']
lw10=['Only Diploma Student can participate with 2 members in a team. All candidate have must their own Apron, Carbide tool and work piece material will be provided by the college, and you may visit our techfest website.']


while(1):
    v=input("Ask something:")
# start of arcania
    if(v.find('arcania')!=-1 or v.find('Arcania')!=-1 or v.find('arc')!=-1 or v.find('Arc')!=-1):
        if(v.find('faculty')!=-1):
            print(arc2)
        elif(v.find('student')!=-1):
            print(arc3)
        elif(v.find('department')!=-1):
            print(arc4)
        elif(v.find('criteria')!=-1 or v.find('eligiblity')!=-1 or v.find('eligible')!=-1):
            print(arc5)
        elif(v.find('fee')!=-1 or v.find('ammount')!=-1 or v.find('pay')!=-1 or v.find('Fee')!=-1):
            print(arc6)
        elif(v.find('time')!=-1 or v.find('timing')!=-1):
            print(arc9)
        elif(v.find('describe')!=-1 or v.find('tell')!=-1 or v.find('what')!=-1 or v.find('about')!=-1):
            if(v.find('rule')!=-1):
                print(arc10)
            elif(v.find('round')!=-1):
                print(arc8)
            elif(v.find('team')!=-1 or v.find('number')!=-1 or v.find('group')!=-1 or v.find('individual')!=-1):
                print(arc7)
            else:
                print(arc1)
        elif(v.find('participant')!=-1 or v.find('participate')!=-1):
            if(v.find('team')!=-1 or v.find('group')!=-1 or v.find('number')!=-1 or v.find('individual')!=-1):
                print(arc7)
            else:
                print(arc5)
        else:
            print('I dont get it.')
# end of arcania

# start of junkyard war
    if(v.find('junkyard war')!=-1 or v.find('junkyard')!=-1 or v.find('junk')!=-1 or v.find('junk yard')!=-1):
        if(v.find('faculty')!=-1):
            print(jyw2)
        elif(v.find('student')!=-1):
            print(jyw3)
        elif(v.find('department')!=-1):
            print(jyw4)
        elif(v.find('criteria')!=-1 or v.find('eligiblity')!=-1 or v.find('eligible')!=-1):
            print(jyw5)
        elif(v.find('fee')!=-1 or v.find('ammount')!=-1 or v.find('pay')!=-1 or v.find('Fee')!=-1):
            print(jyw6)
        elif(v.find('time')!=-1 or v.find('timing')!=-1):
            print(jyw9)
        elif(v.find('describe')!=-1 or v.find('tell')!=-1 or v.find('what')!=-1 or v.find('about')!=-1):
            if(v.find('rule')!=-1):
                print(jyw10)
            elif(v.find('round')!=-1):
                print(jyw8)
            elif(v.find('team')!=-1 or v.find('number')!=-1 or v.find('group')!=-1 or v.find('individual')!=-1):
                print(jyw7)
            else:
                print(jyw1)
        elif(v.find('participant')!=-1 or v.find('participate')!=-1):
            if(v.find('team')!=-1 or v.find('group')!=-1 or v.find('number')!=-1 or v.find('individual')!=-1):
                print(jyw7)
            else:
                print(jyw5)
        else:
            print('I dont get it.')
# end of junkyard war

# start of lathe war
    if(v.find('lathe war')!=-1 or v.find('lathe')!=-1 or v.find('Lathe')!=-1 or v.find('Lathe war')!=-1):
        if(v.find('faculty')!=-1):
            print(lw2)
        elif(v.find('student')!=-1):
            print(lw3)
        elif(v.find('department')!=-1):
            print(lw4)
        elif(v.find('criteria')!=-1 or v.find('eligiblity')!=-1 or v.find('eligible')!=-1):
            print(lw5)
        elif(v.find('fee')!=-1 or v.find('ammount')!=-1 or v.find('pay')!=-1 or v.find('Fee')!=-1):
            print(lw6)
        elif(v.find('time')!=-1 or v.find('timing')!=-1):
            print(lw9)
        elif(v.find('describe')!=-1 or v.find('tell')!=-1 or v.find('what')!=-1 or v.find('about')!=-1):
            if(v.find('rule')!=-1):
                print(lw10)
            elif(v.find('round')!=-1):
                print(lw8)
            elif(v.find('team')!=-1 or v.find('number')!=-1 or v.find('group')!=-1 or v.find('individual')!=-1):
                print(lw7)
            else:
                print(lw1)
        elif(v.find('participant')!=-1 or v.find('participate')!=-1):
            if(v.find('team')!=-1 or v.find('group')!=-1 or v.find('number')!=-1 or v.find('individual')!=-1):
                print(lw7)
            else:
                print(lw5)
        else:
            print('I dont get it.')
# end of lathe war
