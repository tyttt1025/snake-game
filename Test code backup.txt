import random 
productivity = 50 
happiness = 50 
stress = 50 
energy = 70 
friendship = 50 
Sfriendship = 50
Pfriendship = 50
day = 0
bestfriend_unlocked = False
exammark = 0
pythonskill = 0
germanskill = 0
readtimes = 0
geography = 50
science = 50
history = 50
sejarah = 50
print ("Task Simulator") 
while True: 
    day += 1
    print ("Day: ", day)
    if day == 10:
        print ("Exam Incoming!")
        examsubject = random.randint (1,4)
        if examsubject == 1:
            print ("Geography exam!")
            examchoice = input ("Study or relax?").lower()
            if examchoice == "study":
                print ("You studied!")
                print ("Productvity +15")
                print ("Stress -5")
                productivity += 15
                stress -= 5
                if geography >= 70:
                    print ("You got a good grade!")
                else:
                    print ("You got an 80. Kind of dissapointing.")
            else:
                print ("You chose to relax.")
                print ("Try your luck on the exam!")
                print ("Happiness +10")
                happiness += 10
                if exammark >= 5:
                    print ("You still somehow got a good grade.")
                else:
                    print ("You got a 70. Dissapointing.")
        elif examsubject == 2:
            print ("Science exam!")
            examchoice = input ("Study or relax?").lower()
            if examchoice == "study":
                print ("You studied!")
                print ("Productvity +15")
                print ("Stress -5")
                productivity += 15
                stress -= 5
                if science >= 70:
                    print ("You got a good grade!")
                else:
                    print ("You got an 80. Kind of dissapointing.")
            else:
                print ("You chose to relax.")
                print ("Try your luck on the exam!")
                print ("Happiness +10")
                happiness += 10
                if exammark >= 5:
                    print ("You still somehow got a good grade.")
                else:
                    print ("You got a 70. Dissapointing.")
        elif examsubject == 3:
            print ("History exam!")
            examchoice = input ("Study or relax?").lower()
            if examchoice == "study":
                print ("You studied!")
                print ("Productvity +15")
                print ("Stress -5")
                productivity += 15
                stress -= 5
                if history >= 70:
                    print ("You got a good grade!")
                else:
                    print ("You got an 80. Kind of dissapointing.")
            else:
                print ("You chose to relax.")
                print ("Try your luck on the exam!")
                print ("Happiness +10")
                happiness += 10
                if exammark >= 5:
                    print ("You still somehow got a good grade.")
                else:
                    print ("You got a 70. Dissapointing.")
        else:
            print ("Sejarah exam!")
            examchoice = input ("Study or relax?").lower()
            if examchoice == "study":
                print ("You studied!")
                print ("Productvity +15")
                print ("Stress -5")
                productivity += 15
                stress -= 5
                if sejarah >= 70:
                    print ("You got a good grade!")
                else:
                    print ("You got an 80. Kind of dissapointing.")
            else:
                print ("You chose to relax.")
                print ("Try your luck on the exam!")
                print ("Happiness +10")
                happiness += 10
                if exammark >= 5:
                    print ("You still somehow got a good grade.")
                else:
                    print ("You got a 70. Dissapointing.")
    else:
        event = random.randint (1,7) 
        if event == 1: 
            print ("Random event:") 
            print ("You got a message from S!") 
            print ("Happiness +5")
            print ("Friendship + 10") 
            happiness += 5 
            friendship += 10 
            Sfriendship += 5
        elif event == 2: 
            print ("Random event:") 
            print ("You have a lot of homework!") 
            print ("Productivity +5") 
            print ("Energy -5") 
            productivity += 5 
            energy -= 5 
        elif event == 3:
            print ("Random event:")
            print ("You got a message from P!")
            print ("Happiness + 5")
            print ("Friendship +10")
            happiness += 5
            friendship += 10
            Pfriendship += 5
        elif event == 4:
            print ("Random event:")
            print ("You forgot to bring your textbook!")
            print ("Stress +10")
            stress += 10
        elif event == 5:
            print ("Random event:")
            print ("Sudden pop quiz!")
            print ("Stress +20")
            stress += 20
        elif event == 6:
            print ("Random event:")
            print ("S asked the group chat to call.")
            call = input ("Accept or decline call? ")
            if call == "accept":
                print ("Productivity -7")
                print ("Happiness +7")
                print ("Friendship +5")
                productivity -= 7
                happiness += 7
                friendship += 5
            else:
                print ("Productivity +8")
                print ("Happiness -4")
                print ("Friendship -4")
                productivity += 8
                happiness -= 4
                friendship -= 4
        else: 
            print ("Random event:") 
            print ("You eat a snack!") 
            print ("Energy +3")
            energy += 3 
        task = input ("Study, read, chat, sleep or quit? ").lower() 
        if task == "study": 
            topic = input ("Science, history, sejarah, maths, geography, python or german? ").lower()
            if topic == "science":
                if stress <= 80:
                    print ("Productivity +10") 
                    print ("Happiness -5") 
                    print ("Stress -5") 
                    print ("Energy -10") 
                    print ("Exam chance +10")
                    productivity += 10 
                    happiness -= 5 
                    stress -= 5 
                    energy -= 10 
                    science += 10
                else:
                    print ("Burnout!")
                    print ("Productivity +4")
                    print ("Happiness -7")
                    print ("Energy -13")
                    print ("Exam chance +5")
                    productivity += 4
                    happiness -= 7
                    energy -= 13
                    science += 5
            elif topic == "geography":
                if stress <= 80:
                    print ("Productivity +10") 
                    print ("Happiness -5") 
                    print ("Stress -5") 
                    print ("Energy -10") 
                    print ("Exam chance +10")
                    productivity += 10 
                    happiness -= 5 
                    stress -= 5 
                    energy -= 10 
                    geography += 10
                else:
                    print ("Burnout!")
                    print ("Productivity +4")
                    print ("Happiness -7")
                    print ("Energy -13")
                    print ("Exam chance +5")
                    productivity += 4
                    happiness -= 7
                    energy -= 13
                    geography += 5
            elif topic == "history":
                if stress <= 80:
                    print ("Productivity +10") 
                    print ("Happiness -5") 
                    print ("Stress -5") 
                    print ("Energy -10") 
                    print ("Exam chance +10")
                    productivity += 10 
                    happiness -= 5 
                    stress -= 5 
                    energy -= 10 
                    history += 10
                else:
                    print ("Burnout!")
                    print ("Productivity +4")
                    print ("Happiness -7")
                    print ("Energy -13")
                    print ("Exam chance +5")
                    productivity += 4
                    happiness -= 7
                    energy -= 13
                    history += 5
            elif topic == "sejarah":
                if stress <= 80:
                    print ("Productivity +10") 
                    print ("Happiness -5") 
                    print ("Stress -5") 
                    print ("Energy -10") 
                    print ("Exam chance +10")
                    productivity += 10 
                    happiness -= 5 
                    stress -= 5 
                    energy -= 10 
                    sejarah += 10
                else:
                    print ("Burnout!")
                    print ("Productivity +4")
                    print ("Happiness -7")
                    print ("Energy -13")
                    print ("Exam chance +5")
                    productivity += 4
                    happiness -= 7
                    energy -= 13
                    sejarah += 5
            elif topic == "python":
                print ("Productivity +7")
                print ("Happiness +5")
                print ("Stress -3")
                print ("Python skill +5")
                productivity += 7
                happiness += 5
                stress -= 3
                pythonskill += 5
            else:
                print ("Productivity +4")
                print ("Happiness +3")
                print ("Stress -3")
                print ("German skill +3")
                productivity += 4
                happiness += 3
                stress -= 3
                germanskill += 3
        elif task == "read": 
            print ("Productivity -5") 
            print ("Happiness +10") 
            print ("Stress -10") 
            print ("Energy +10") 
            happiness += 10 
            productivity -= 5 
            stress -= 10 
            energy += 10 
            readtimes += 1
        elif task == "chat": 
            chatoption = input ("Chat or ignore messages? ").lower() 
            if chatoption == "chat": 
                chatperson = input ("Text S, P or group chat?").lower()
                if chatperson == "s":
                    print ("Friendship with S +10")    
                    print ("Productivity -10") 
                    print ("Happiness +7") 
                    print ("Stress -10") 
                    print ("Energy +5") 
                    print ("Friendship +10") 
                    stress -= 10 
                    productivity -= 10 
                    happiness += 7 
                    energy += 5 
                    friendship += 10 
                    Sfriendship += 10
                elif chatperson == "p":
                    print ("Friendship with P +10")    
                    print ("Productivity -10") 
                    print ("Happiness +7") 
                    print ("Stress -10") 
                    print ("Energy +5") 
                    print ("Friendship +10") 
                    stress -= 10 
                    productivity -= 10 
                    happiness += 7 
                    energy += 5 
                    friendship += 10 
                    Pfriendship += 10
                else:
                    print ("Productivity -10") 
                    print ("Happiness +7") 
                    print ("Stress -10") 
                    print ("Energy +5") 
                    print ("Friendship +10") 
                    stress -= 10 
                    productivity -= 10 
                    happiness += 7 
                    energy += 5 
                    friendship += 10 
            else: 
                print ("Productivity +5") 
                print ("Happiness -5") 
                print ("Stress +3") 
                print ("Friendship -8") 
                happiness -= 5 
                productivity += 5 
                stress += 3 
                friendship -= 8 
        elif task == "quit": 
            break 
        elif task == "sleep":
            print ("Energy +20")
            print ("Stress -5")
            energy += 20
            stress -= 5
        else: print ("Invalid task. Try again.") 
        print ("Result:") 
        print ("Productivity: ", productivity) 
        print ("Happiness: ", happiness) 
        print ("Stress: ", stress) 
        print ("Energy: ", energy) 
        print ("Friendship: ", friendship)
        print ("S friendship: ", Sfriendship)
        print ("P friendship: ", Pfriendship)
        print ("Python skill: ", pythonskill)
        print ("German skill: ", germanskill)
        if energy < 20: 
            print ("You are too tired!") 
            print ("Game over.") 
            break 
        elif productivity > 100:
            print ("You have completed all your tasks!") 
            print ("You win!") 
            break
        elif friendship >= 100 and bestfriend_unlocked == False:
            print ("Acheivement unlocked!")
            print ("Best Friends")
            bestfriend_unlocked = True
            print ("______________________")
        elif readtimes == 20:
            print ("Acheivement unlocked!")
            print ("Bookworm")
        elif germanskill == 30:
            print ("Achievement unlocked!")
            print ("German learner")
        elif pythonskill == 30:
            print ("Achievement unlocked!")
            print ("Python Programmer")
        else: print ("______________________")