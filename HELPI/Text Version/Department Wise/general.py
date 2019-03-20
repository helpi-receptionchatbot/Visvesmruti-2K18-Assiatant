art1=['art gallery is an event of visvesmruti 2k18. in which participants can present their handmade pictures and portraits.']
art2=['Professor H. T. Shah is the faculty coordinator of art gallery']
art3=['Shreyas Parekh is the student co-ordinator of art gallery']
art4=['the art gallery event is managed by all deparments centraly.']
art5=['any student pursuing diploma or degree engineering can participate']
art6=['the participants have to pay a fee50 rupees per head']
art7=['the participant have to take part as the team of 3.']
art8=['this event does not have any round.']
art9=['timming will be given you at the venue of event.']
art10=['Your picture should be unique and handmade.']

mop1=['model presntation is an event of visvesmruti 2k18 managed by each department of our college. in which focuses on how you turn your technical skills into actual practice. The event is all about building working models.']
mop2=['Professor K. D. Patel is the faculty co-ordinator of model presntation for civil department.']
mop3=['Professor Dhaval Patel is the faculty co-ordinator of model presntation for chemical department.']
mop4=['Professor Milind Kansara is the faculty co-ordinator of model presntation for electrical department.']
mop5=['Professor Hardik Nayak is the faculty co-ordinator of model presntation for mechanical department.']
mop6=['Contact Professor K. D. Patel for student co-ordinators.']
mop7=['Anat Patel and Karan Modi are the student co-ordinators of model presntation for chemical department.']
mop8=['Contact Professor Milind Kansara for student co-ordinators.']
mop9=['Ganesh Kavar and Parth Ladani are the student co-ordinators of model presntation for mechanical department.']
mop10=['all departments are managing the model presntation event at department level exept computer department']
mop11=['any student pursuing diploma or degree engineering can participate.']
mop12=['the participants have to pay a fee of 200 rupees for a team means 50 rupees per head']
mop13=['the participant have to take part as the team of 4.']
mop14=['There are rounds like presentation and questioning-answering']
mop15=['You have to represent whole model in 15 to 20 minutes. and A 2 to 5 minute question and answer period will follow the presentation of the model.']
mop16=['Model should be related to technical topic.']
mop17=['Computer doesnot organize model presentation.']

pap1=['paper presntation is an event of visvesmruti 2k18 managed by each department of our college. in which the participant have to make a paper and than have to present that']
pap2=['Professor Dhaval rana is the faculty co-ordinator of paper presntation for computer department.']
pap3=['Professor S. M. Marfani is the faculty co-ordinator of paper presntation for civil department.']
pap4=['Professor Kimshuk Desai is the faculty co-ordinator of paper presntation for chemical department.']
pap5=['Professor Milind Kansara is the faculty co-ordinator of paper presntation for electrical department.']
pap6=['Professor Hardik Nayak is the faculty co-ordinator of paper presntation for mechanical department.']
pap7=['Hemraj Desai and Riya Shah are the student co-ordinators of paper presntation for computer department.']
pap8=['Dipesh Sosa and Heni Bhajiwala are the student co-ordinators of paper presntation for civil department.']
pap9=['Dhrumil Prajapati and Milind Patel are the student co-ordinators of paper presntation for chemical department.']
pap10=['Contact Professor Milind Kansara for student co-ordinators.']
pap11=['Amit Savaliya and Subham Patel are the student co-ordinators of paper presntation for mechanical department.']
pap12=['all departments are managing the paper presntation event at department level.']
pap13=['any student pursuing diploma or degree engineering can participate']
pap14=['the participants have to pay a fee of 100 rupees for a team means 50 rupees per head']
pap15=['the participant have to take part as the team of 2.']
pap16=['There are rounds like presentation and questioning-answering']
pap17=['The presentation time will be of 5 to 7 minutes. and A 2 to 5 minute question and answer period will follow the presentation of the paper.']
pap18=['Your work should be original and the papers should be in standard, I triple E format. No of pages should not be more than 10.']

pop1=['poster presntation is an event of visvesmruti 2k18 managed by each department of our college. in which the participant have to represent their ideas by a poster.']
pop2=['Professor Nikunj Kansara is the faculty co-ordinator of poster presntation for computer department.']
pop3=['Professor G. P. Barot is the faculty co-ordinator of poster presntation for civil department.']
pop4=['Professor Taruna Patel is the faculty co-ordinator of poster presntation for chemical department.']
pop5=['Professor Milind Kansara is the faculty co-ordinator of poster presntation for electrical department.']
pop6=['Professor Hardik Nayak is the faculty co-ordinator of poster presntation for mechanical department.']
pop7=['Ankita Tank and Chandera Dayna are the student co-ordinators of poster presntation for computer department.']
pop8=['Masum Patel and Raj Desai are the student co-ordinators of poster presntation for civil department.']
pop9=['Rushit Chawda and Kinjal Prajapati are the student co-ordinators of poster presntation for chemical department.']
pop10=['Contact Professor Milind Kansara for student co-ordinators.']
pop11=['Bhavya Pandya and Naman Shah are the student co-ordinators of poster presntation for mechanical department.']
pop12=['all departments are managing the poster presntation event at department level.']
pop13=['any student pursuing diploma or degree engineering can participate']
pop14=['the participants have to pay a fee of 50 rupees per head']
pop15=['the participant have to take part as the team of 3.']
pop16=['There are rounds like presentation and questioning-answering']
pop17=['The presentation time will be of 7 to 10 minutes. and A 2 to 5 minute question and answer period will follow the presentation of the poster.']
pop18=['Your work should be original and the posters should be in standard, I triple E format. Abstract should not exceed 300 words.']
pop19=['participants have to present their idea on a standard poster of dimensions 3 feet (height) and 2 feet (width) or 3 feet (height) and 4 feet (width).']


while(1):
    v=input("Ask something:")
# start of art gallery
    if(v.find('art gallery')!=-1 or v.find('art')!=-1 or v.find('gallery')!=-1 or v.find('Art')!=-1):
        if(v.find('faculty')!=-1):
            print(art2)
        elif(v.find('student')!=-1):
            print(art3)
        elif(v.find('department')!=-1):
            print(art4)
        elif(v.find('criteria')!=-1 or v.find('eligiblity')!=-1 or v.find('eligible')!=-1):
            print(art5)
        elif(v.find('fee')!=-1 or v.find('ammount')!=-1 or v.find('pay')!=-1 or v.find('Fee')!=-1):
            print(art6)
        elif(v.find('time')!=-1 or v.find('timing')!=-1):
            print(art9)
        elif(v.find('describe')!=-1 or v.find('tell')!=-1 or v.find('what')!=-1 or v.find('about')!=-1):
            if(v.find('rule')!=-1):
                print(art10)
            elif(v.find('round')!=-1):
                print(art8)
            elif(v.find('team')!=-1 or v.find('number')!=-1 or v.find('group')!=-1 or v.find('individual')!=-1):
                print(art7)
            else:
                print(art1)
        elif(v.find('participant')!=-1 or v.find('participate')!=-1):
            if(v.find('team')!=-1 or v.find('number')!=-1 or v.find('group')!=-1 or v.find('individual')!=-1):
                print(art7)
            else:
                print(art5)
        else:
            print('I dont get it.')
# end of art gallery

# start of model presntation
    if(v.find('model presntation')!=-1 or v.find('model')!=-1 or v.find('Model')!=-1):
        if(v.find('faculty')!=-1):
            if(v.find('civil')!=-1):
                print(mop2)
            elif(v.find('chemical')!=-1):
                print(mop3)
            elif(v.find('electrical')!=-1):
                print(mop4)
            elif(v.find('mechanical')!=-1):
                print(mop5)
        elif(v.find('student')!=-1):
            if(v.find('civil')!=-1):
                print(mop6)
            elif(v.find('chemical')!=-1):
                print(mop7)
            elif(v.find('electrical')!=-1):
                print(mop8)
            elif(v.find('mechanical')!=-1):
                print(mop9)
        elif(v.find('department')!=-1):
            print(mop10)
        elif(v.find('criteria')!=-1 or v.find('eligiblity')!=-1 or v.find('eligible')!=-1):
            print(mop11)
        elif(v.find('fee')!=-1 or v.find('ammount')!=-1 or v.find('pay')!=-1 or v.find('Fee')!=-1):
            print(mop12)
        elif(v.find('time')!=-1 or v.find('timing')!=-1):
            print(mop15)
        elif(v.find('describe')!=-1 or v.find('tell')!=-1 or v.find('what')!=-1 or v.find('about')!=-1):
            if(v.find('rule')!=-1):
                print(mop16)
            elif(v.find('round')!=-1):
                print(mop14)
            elif(v.find('team')!=-1 or v.find('number')!=-1 or v.find('group')!=-1 or v.find('individual')!=-1):
                print(mop13)
            else:
                print(mop1)
        elif(v.find('participant')!=-1 or v.find('participate')!=-1):
            if(v.find('team')!=-1 or v.find('number')!=-1 or v.find('group')!=-1 or v.find('individual')!=-1):
                print(mop13)
            else:
                print(mop11)
        elif(v.find('computer')!=-1):
            print(mop17)
        else:
            print('I dont get it.')
# end of model presntation

# start of paper presntation
    if(v.find('paper presntation')!=-1 or v.find('paper')!=-1 or v.find('Paper')!=-1):
        if(v.find('faculty')!=-1):
            if(v.find('computer')!=-1):
                print(pap2)
            elif(v.find('civil')!=-1):
                print(pap3)
            elif(v.find('chemical')!=-1):
                print(pap4)
            elif(v.find('electrical')!=-1):
                print(pap5)
            elif(v.find('mechanical')!=-1):
                print(pap6)
        elif(v.find('student')!=-1):
            if(v.find('computer')!=-1):
                print(pap7)
            elif(v.find('civil')!=-1):
                print(pap8)
            elif(v.find('chemical')!=-1):
                print(pap9)
            elif(v.find('electrical')!=-1):
                print(pap10)
            elif(v.find('mechanical')!=-1):
                print(pap11)
        elif(v.find('department')!=-1):
            print(pap12)
        elif(v.find('criteria')!=-1 or v.find('eligiblity')!=-1 or v.find('eligible')!=-1):
            print(pap13)
        elif(v.find('fee')!=-1 or v.find('ammount')!=-1 or v.find('pay')!=-1 or v.find('Fee')!=-1):
            print(pap14)
        elif(v.find('time')!=-1 or v.find('timing')!=-1):
            print(pap17)
        elif(v.find('describe')!=-1 or v.find('tell')!=-1 or v.find('what')!=-1 or v.find('about')!=-1):
            if(v.find('rule')!=-1):
                print(pap18)
            elif(v.find('round')!=-1):
                print(pap16)
            elif(v.find('team')!=-1 or v.find('number')!=-1 or v.find('group')!=-1 or v.find('individual')!=-1):
                print(pap15)
            else:
                print(pap1)
        elif(v.find('participant')!=-1 or v.find('participate')!=-1):
            if(v.find('team')!=-1 or v.find('number')!=-1 or v.find('group')!=-1 or v.find('individual')!=-1):
                print(pap15)
            else:
                print(pap5)
        else:
            print('I dont get it.')
# end of paper presntation

# start of poster presntation
    if(v.find('poster presntation')!=-1 or v.find('poster')!=-1 or v.find('Poster')!=-1):
        if(v.find('faculty')!=-1):
            if(v.find('computer')!=-1):
                print(pop2)
            elif(v.find('civil')!=-1):
                print(pop3)
            elif(v.find('chemical')!=-1):
                print(pop4)
            elif(v.find('electrical')!=-1):
                print(pop5)
            elif(v.find('mechanical')!=-1):
                print(pop6)
        elif(v.find('student')!=-1):
            if(v.find('computer')!=-1):
                print(pop7)
            elif(v.find('civil')!=-1):
                print(pop8)
            elif(v.find('chemical')!=-1):
                print(pop9)
            elif(v.find('electrical')!=-1):
                print(pop10)
            elif(v.find('mechanical')!=-1):
                print(pop11)
        elif(v.find('department')!=-1):
            print(pop12)
        elif(v.find('size')!=-1):
            print(pop19)
        elif(v.find('criteria')!=-1 or v.find('eligiblity')!=-1 or v.find('eligible')!=-1):
            print(pop13)
        elif(v.find('fee')!=-1 or v.find('ammount')!=-1 or v.find('pay')!=-1 or v.find('Fee')!=-1):
            print(pop14)
        elif(v.find('time')!=-1 or v.find('timing')!=-1):
            print(pop17)
        elif(v.find('describe')!=-1 or v.find('tell')!=-1 or v.find('what')!=-1 or v.find('about')!=-1):
            if(v.find('rule')!=-1):
                print(pop18)
            elif(v.find('round')!=-1):
                print(pop16)
            elif(v.find('team')!=-1 or v.find('number')!=-1 or v.find('group')!=-1 or v.find('individual')!=-1):
                print(pop15)
            else:
                print(pop1)
        elif(v.find('participant')!=-1 or v.find('participate')!=-1):
            if(v.find('team')!=-1 or v.find('number')!=-1 or v.find('group')!=-1 or v.find('individual')!=-1):
                print(pop15)
            else:
                print(pop13)
        else:
            print('I dont get it.')
# end of poster presntation
