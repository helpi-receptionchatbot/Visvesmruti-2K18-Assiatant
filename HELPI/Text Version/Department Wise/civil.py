bs1=['Bridge Structure is an event of visvesmruti 2k18 managed by civil department in which Participants have to produce a bridge which is able to bear the maximum load will be the winner.']
bs2=['Bridge Structure will be coordinated by Professor B G PATEL and Professor M A QURESHI']
bs3=[]
bs4=['civil department is going to manage the Bridge Structure event']
bs5=['Any student from diploma and degree engineering can take part in Bridge Structure']
bs6=['the participants have to pay a fee of rupees fifty per person']
bs7=['the participant have to take part in team of 3 persons']
bs8=['rounds will be described at the venue or you may visit our techfest website.']
bs9=['timming and the tasks will be given at the venue']
bs10=['All required materials and dimensions will be provided, Pinning and clamping are not allowed to be used for connections. And for more visit our techfest website']

pm1=['photomania is an event of visvesmruti 2k18 managed by civil department in which Participants have to reveal the signs, logo and image shown to them in various technical rounds.']
pm2=['Reveal Me will be coordinated by Professor Ajay Patel and Professor Vivek Dungrani']
pm3=['Student Coordinators are Jitendra Prajapati and Saumil Savaliya']
pm4=['photomania is managed by civil department']
pm5=['any student pursuing diploma or degree engineering can participate in photomania']
pm6=['the participants have to pay a fee of rupees fifty per person']
pm7=['the participant have to take part as individuals']
pm8=['rounds will be described at the venue']
pm9=['timming and the tasks will be given at the venue']
pm10=['Technical Instruments, Laboratories, etc Institutes Building, Parking, Departments, Canteen, Event etc are themes. and Participants are permitted to submit a maximum of five photographs']

rm1=['Reveal Me is an event of visvesmruti 2k18 managed by civil department in which Participants have to produce a bridge which is able to bear the maximum load will be the winner.']
rm2=['Reveal Me will be coordinated by Professor Vivek Dungrani and Professor Ajay Patel']
rm3=['Student coordinators are Jitendra Prajapati and Saumil Savaliya']
rm4=['civil department is going to manage the Reveal Me event']
rm5=['Any student from diploma engineering can take part in Reveal Me']
rm6=['the participants have to pay a fee of rupees fifty per head']
rm7=['the participant have to take part individually']
rm8=['Number of rounds will be decide on the basis on the entries by the Faculty Coordinators and there will be special prize for diploma students.']
rm9=['timming and the tasks will be given at the venue']
rm10=['Content of the event basically Covers Traffic signs and symbol, Technical Figures, Abbreviation used in civil, Various Company Logo and Images of some beautiful Creation and Structure by civil Engineers.']

while(1):
    v=input("Ask something:")
# Start of Bridge Structure
    if(v.find('bridge structure')!=-1 or v.find('bs')!=-1 or v.find('b s')!=-1 or v.find('Bridge structure')!=-1):
        if(v.find('faculty')!=-1):
            print(bs2)
        elif(v.find('student')!=-1):
            print(bs3)
        elif(v.find('department')!=-1):
            print(bs4)
        elif(v.find('criteria')!=-1 or v.find('eligiblity')!=-1 or v.find('eligible')!=-1):
            print(bs5)
        elif(v.find('fee')!=-1 or v.find('ammount')!=-1 or v.find('pay')!=-1 or v.find('Fee')!=-1):
            print(bs6)
        elif(v.find('time')!=-1 or v.find('timing')!=-1):
            print(bs9)
        elif(v.find('describe')!=-1 or v.find('tell')!=-1 or v.find('what')!=-1 or v.find('about')!=-1):
            if(v.find('rule')!=-1):
                print(bs10)
            elif(v.find('round')!=-1):
                print(bs8)
            elif(v.find('team')!=-1 or v.find('number')!=-1 or v.find('group')!=-1 or v.find('individual')!=-1):
                print(bs7)
            else:
                print(bs1)
        elif(v.find('participant')!=-1 or v.find('participate')!=-1):
            if(v.find('team')!=-1 or v.find('number')!=-1 or v.find('group')!=-1 or v.find('individual')!=-1):
                print(bs7)
            else:
                print(bs5)
        else:
            print('I dont get it.')
#end of Bridge Structure

# Start of photomania
    if(v.find('photomania')!=-1 or v.find('PhotoMania')!=-1 or v.find('photo')!=-1 or v.find('poto')!=-1):
        if(v.find('faculty')!=-1):
            print(pm2)
        elif(v.find('student')!=-1):
            print(pm3)
        elif(v.find('department')!=-1):
            print(pm4)
        elif(v.find('criteria')!=-1 or v.find('eligiblity')!=-1 or v.find('eligible')!=-1):
            print(pm5)
        elif(v.find('fee')!=-1 or v.find('ammount')!=-1 or v.find('pay')!=-1 or v.find('Fee')!=-1):
            print(pm6)
        elif(v.find('time')!=-1 or v.find('timing')!=-1):
            print(pm9)
        elif(v.find('describe')!=-1 or v.find('tell')!=-1 or v.find('what')!=-1 or v.find('about')!=-1):
            if(v.find('rule')!=-1):
                print(pm10)
            elif(v.find('round')!=-1):
                print(pm8)
            elif(v.find('team')!=-1 or v.find('number')!=-1 or v.find('group')!=-1 or v.find('individual')!=-1):
                print(pm7)
            else:
                print(pm1)
        elif(v.find('participant')!=-1 or v.find('participate')!=-1):
            if(v.find('team')!=-1 or v.find('number')!=-1 or v.find('group')!=-1 or v.find('individual')!=-1):
                print(pm7)
            else:
                print(pm5)
        else:
            print('I dont get it.')
#end of photomania

# Start of Reveal Me
    if(v.find('Reveal Me')!=-1 or v.find('Reveal')!=-1 or v.find('reveal')!=-1 or v.find('real me')!=-1 or v.find('Reveal me')!=-1 or v.find('reveal me')!=-1 or v.find('realme')!=-1):
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
#end of Reveal Me
