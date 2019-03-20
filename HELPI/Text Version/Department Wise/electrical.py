eg1=['E google is an event of visvesmruti 2k18 managed by Electrical department in which Participants have to answer the questions based on Google search.']
eg2=['Professor Milind kansara is the faculty coordinator of Robo Soccer']
eg3=[]
eg4=['Electrical department is going to manage the E google event','E google is managed by Electrical department']
eg5=['Any student from diploma and degree engineering can take part in E google','any student pursuing graduation can participate in E google']
eg6=['the participants have to pay a fee of rupees fifty','Each participant have to pay fifty rupees',]
eg7=['the participant have to take part individually','E google is an event for individuals']
eg8=['This event will comprise of three rounds.']
eg9=['In first round, 30 questions to be answered with the help of Internet (Google Search)']
eg10=['In second round, 25 questions to be answered with the help of Internet (Google Search)']
eg11=['In third round, 20 questions to be answered with the help of Internet (Google Search)']
eg12=['time of each round is 20 minutes.']
eg13=['Timing will be considered for participant in all the round.']

rc1=['Robo climber is an event of visvesmruti 2k18 managed by Electrical department in which the participants have to make a simple wiredrobot that can run, or climb on the arena consisting paths with obstacles like sand, pebbles, oil, speed breakers, tunnel, so on..']
rc2=['Professor Milind kansara is the faculty coordinator of Robo climber']
rc3=[]
rc4=['Electrical department is going to manage the Robo climber event','Robo climber is managed by Electrical department']
rc5=['Any student from diploma and degree engineering can take part in Robo climber as the team of 4.']
rc6=['the participants have to pay a fee of 600 rupees per team']
rc7=['the participant have to take part in team of 4 members.']
rc8=['tere are multiple round based on the arena.']
rc9=['There are different timing for each round based on the task.']
rc10=['Readymade toy is not allowed,  climber ball should only be pushed, not to be grabbed by the bot. Team should make sure not to damage the arena or the opponent bot.']
rc11=['Arena will consist of path with obstacles like sand, pebbles, oil, speed breakers, tunnel, so on.']
rc12=['Robo dimensions should not be more than 30 cross 30 cross 30 centimeter, Machine should not weigh more than 4 kilogram with battery']

rs1=['Robo Soccer is an event of visvesmruti 2k18 managed by Electrical department in which the participants have to make a simple wiredrobot that can play football with each other.']
rs2=['Professor Milind kansara is the faculty coordinator of Robo Soccer']
rs3=[]
rs4=['Electrical department is going to manage the Robo Soccer event','Robo Soccer is managed by Electrical department']
rs5=['Any student from diploma and degree engineering can take part in Robo Soccer as the team of 2 or 4.']
rs6=['the participants have to pay a fee of 200 rupees per team']
rs7=['the participant have to take part in team of 2 to 4 members']
rs8=['there are total 6 rounds. each round has different task with different time limit']
rs9=['in round 1, there will be 4 balls, two will be red and another two will be blue. Robo 1 has to put red ball in goal and Robo 2 has to put blue ball in goal']
rs10=['in round 2, there will be 5 balls, 1 Red having 30 points, 2 blue balls having 20 points, 2 white balls having 10 points,1 hand touch is allowed, maximum goal scorer will qualify']
rs11=['in round 3, there will be 3 balls, 1 blue balls having 20 points, 2 white balls having 10 points, 1 hand touch is allowed, maximum goal scorer will qualify']
rs12=['in round 4, there will be 4 balls, 1 blue balls having 30 points, 3 white balls having 15 points, No hand touch is allowed, If required touch than both team loss 5 point, maximum goal scorer will qualify']
rs13=['in round 5, there will be 4 balls, 1 blue balls having 30 points, 3 white balls having 15 points. No hand touch is allowed, If required touch than both team loss 5 point, maximum goal scorer will qualify']
rs14=['in round 6, there will be 5 balls,1 red balls having 35 points, 2 blue balls having 25 points, 2 white balls having 20 points. Not hand touch will allowed. If required touch than both team loss 10 point']
rs15=['There are different timing for each round based on the task']
rs16=['Time limit of round 1 is 2 minutes and 30 seconds.']
rs17=['Time limit of round 2 is 3 minutes']
rs18=['Time limit of round 3 is 3 minutes']
rs19=['Time limit of round 4 is 3 minutes and 30 seconds.']
rs20=['Time limit of round 5 is 4 minutes']
rs21=['Time limit of round 6 is 5 minutes']
rs22=['Readymade toy is not allowed,  Soccer ball should only be pushed, not to be grabbed by the bot. Team should make sure not to damage the arena or the opponent bot.']
rs23=['Arena will be football ground with dimensions 180 centimetres cross 270 centimetres.']
rs24=['Robo dimensions should not be more than 30 cross 30 cross 30 centimeter, Machine should not weigh more than 4 kilogram with battery']


while(1):
    v=input("Ask something:")
# start of  e google
    if(v.find(' e google')!=-1 or v.find('E google')!=-1 or v.find('Google')!=-1 or v.find('google')!=-1):
        if(v.find('faculty')!=-1):
            print(eg2)
        elif(v.find('student')!=-1):
            print(eg2)
        elif(v.find('department')!=-1):
            print(eg4)
        elif(v.find('criteria')!=-1 or v.find('eligiblity')!=-1 or v.find('eligible')!=-1):
            print(eg5)
        elif(v.find('fee')!=-1 or v.find('ammount')!=-1 or v.find('pay')!=-1 or v.find('Fee')!=-1):
            print(eg6)
        elif(v.find('time')!=-1 or v.find('timing')!=-1):
            print(eg12)
        elif(v.find('describe')!=-1 or v.find('tell')!=-1 or v.find('what')!=-1 or v.find('about')!=-1):
            if(v.find('rule')!=-1):
                print(eg13)
            elif(v.find('round 1')!=-1 or v.find('round one')!=-1):
                print(rs9)
            elif(v.find('round 2')!=-1 or v.find('round two')!=-1):
                print(rs10)
            elif(v.find('round 3')!=-1 or v.find('round three')!=-1):
                print(rs11)
            elif(v.find('round')!=-1):
                print(eg8)
            elif(v.find('team')!=-1 or v.find('number')!=-1 or v.find('group')!=-1 or v.find('individual')!=-1):
                print(eg7)
            else:
                print(eg1)
        elif(v.find('participant')!=-1 or v.find('participate')!=-1):
            if(v.find('team')!=-1 or v.find('number')!=-1 or v.find('group')!=-1 or v.find('individual')!=-1):
                print(eg7)
            else:
                print(eg5)
        else:
            print('I dont get it.')
# end of  e google

# start of robo climber
    if(v.find('robo climber')!=-1 or v.find('Robo Climber')!=-1 or v.find('climber')!=-1 or v.find('Climber')!=-1):
        if(v.find('faculty')!=-1):
            print(rc2)
        elif(v.find('student')!=-1):
            print(rc2)
        elif(v.find('department')!=-1):
            print(rc4)
        elif(v.find('criteria')!=-1 or v.find('eligiblity')!=-1 or v.find('eligible')!=-1):
            print(rc5)
        elif(v.find('fee')!=-1 or v.find('ammount')!=-1 or v.find('pay')!=-1 or v.find('Fee')!=-1):
            print(rc6)
        elif(v.find('time')!=-1 or v.find('timing')!=-1):
            print(rc9)
        elif(v.find('describe')!=-1 or v.find('tell')!=-1 or v.find('what')!=-1 or v.find('about')!=-1):
            if(v.find('rule')!=-1):
                print(rc10)
            elif(v.find('arena')!=-1):
                print(rc11)
            elif(v.find('specification')!=-1):
                print(rc12)
            elif(v.find('round')!=-1):
                print(rc8)
            elif(v.find('team')!=-1 or v.find('number')!=-1 or v.find('group')!=-1 or v.find('individual')!=-1):
                print(rc7)
            else:
                print(rc1)
        elif(v.find('participant')!=-1 or v.find('participate')!=-1):
            if(v.find('team')!=-1 or v.find('number')!=-1 or v.find('group')!=-1 or v.find('individual')!=-1):
                print(rc7)
            else:
                print(rc5)
        else:
            print('I dont get it.')
# end of robo climber

# start of robo soccer
    if(v.find('robo soccer')!=-1 or v.find('Robo Soccer')!=-1 or v.find('Soccer')!=-1 or v.find('soccer')!=-1):
        if(v.find('faculty')!=-1):
            print(rs2)
        elif(v.find('student')!=-1):
            print(rs2)
        elif(v.find('department')!=-1):
            print(rs4)
        elif(v.find('criteria')!=-1 or v.find('eligiblity')!=-1 or v.find('eligible')!=-1):
            print(rs5)
        elif(v.find('fee')!=-1 or v.find('ammount')!=-1 or v.find('pay')!=-1 or v.find('Fee')!=-1):
            print(rs6)
        elif(v.find('time')!=-1 or v.find('timing')!=-1):
            if(v.find('round 1')!=-1 or v.find('round one')!=-1):
                print(rs16)
            elif(v.find('round 2')!=-1 or v.find('round two')!=-1):
                print(rs17)
            elif(v.find('round 3')!=-1 or v.find('round three')!=-1):
                print(rs18)
            elif(v.find('round 4')!=-1 or v.find('round four')!=-1):
                print(rs19)
            elif(v.find('round 5')!=-1 or v.find('round five')!=-1):
                print(rs20)
            elif(v.find('round 6')!=-1 or v.find('round six')!=-1):
                print(rs21)
            else:
                print(rs15)
        elif(v.find('describe')!=-1 or v.find('tell')!=-1 or v.find('what')!=-1 or v.find('about')!=-1):
            if(v.find('rule')!=-1):
                print(rs22)
            elif(v.find('arena')!=-1):
                print(rs23)
            elif(v.find('specification')!=-1):
                print(rs24)
            elif(v.find('round 1')!=-1 or v.find('round one')!=-1):
                print(rs9)
            elif(v.find('round 2')!=-1 or v.find('round two')!=-1):
                print(rs10)
            elif(v.find('round 3')!=-1 or v.find('round three')!=-1):
                print(rs11)
            elif(v.find('round 4')!=-1 or v.find('round four')!=-1):
                print(rs12)
            elif(v.find('round 5')!=-1 or v.find('round five')!=-1):
                print(rs13)
            elif(v.find('round 6')!=-1 or v.find('round six')!=-1):
                print(rs14)
            elif(v.find('round')!=-1):
                print(rs8)
            elif(v.find('team')!=-1 or v.find('number')!=-1 or v.find('group')!=-1 or v.find('individual')!=-1):
                print(rs7)
            else:
                print(rs1)
        elif(v.find('participant')!=-1 or v.find('participate')!=-1):
            if(v.find('team')!=-1 or v.find('number')!=-1 or v.find('group')!=-1 or v.find('individual')!=-1):
                print(rs7)
            else:
                print(rs5)
        else:
            print('I dont get it.')
# end of robo soccer
