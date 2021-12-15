#Habit Tracker
import schedule
import time
schedule.Set
from bokeh.plotting import figure, show


def daily_affirmation ():
    with open('affirmations.csv','r') as file:
        contents = file.read()
        line = contents.split('\n')
    for j in line:
        j=1
        if j < 31:
             time.sleep(4)
             print(line[j])
             j += 1

def counter(global met_goals ):
    global met_goals = 0
    return global met_goals    

def goal1(message='drink water'):
    print(message)
    global met_goals 
    accomplished= input("Task complete? (y/n) ")
    if accomplished == "y":
        print("Yay-one step closer!")
        global met_goals +=1
    if accomplished == "n":
        print("keep trying!")

def goal2(message='work out'):
    print("time to", message)
    global met_goals 
    accomplished= input("Task complete? (y/n) ")
    if accomplished == "y":
        print("Yay-one step closer!")
        global met_goals  +=1
    if accomplished == "n":
        print("keep trying!")

def goal3(message='sleep 8 hours'):
    print("time to", message)
    global met_goals 
    accomplished= input("Task complete? (y/n) ")
    if accomplished == "y":
        print("Yay-one step closer!")
        global met_goals  +=1
    if accomplished == "n":
        print("keep trying!")

def goal4(message='wake up!Drink a glass of water- Cheers!'):
    print("time to", message)
    global met_goals 
    accomplished= input("Task complete? (y/n) ")
    if accomplished == "y":
        print("Yay-one step closer!")
        global met_goals  +=1
    if accomplished == "n":
        print("keep trying!")

def goal5(message='get steps in'):
    print("time to", message)
    global met_goals 
    accomplished= input("Task complete? (y/n) ")
    if accomplished == "y":
        print("Yay-one step closer!")
        global met_goals  +=1
    if accomplished == "n":
        print("keep trying!")

def congrats (message='Congratulations! Keep up the great work!'):
    print(message)

schedule.__spec__
schedule.__annotations__

schedule.every(15).minutes.do(goal1)
schedule.every(15).to(30).minutes.do(goal5)
# schedule.every(5).to(10).days.do(goal1)
schedule.every(1).hour.do(goal2, )
schedule.every().day.at("11:33").do(goal2)
schedule.every().day.at("09:30").do(goal3)
schedule.every().day.at("06:00").do(goal4)
schedule.every().day.at("14:58").do(daily_affirmation)
schedule.every().day.at("16:00").do(congrats)

# daily= int(global met_goals )
# weeklytally = []
# weeklytally.append(daily)
# print(weeklytally)

x= 1,2,3,4,5,6,7
y= 5,7,9,12,13,16,30
w= figure(title="Goal Tracker", x_axis_label = "days", y_axis_label= "goals met")
w.line(x, y, legend_label="consistency.", line_width=2)
progress= input("do you want to see your progress? (y/n)")
if progress == "y":
    show(w)



while True:
    schedule.run_pending()
    time.sleep(1)
    counter(global met_goals = 0)
   


#ideally a print out of total day tasks would be nice ie ("look ahead:" + list)
#adding a affirmations/daily quote generator like joke generator would be great
#input for initial goals at beginning would be great. 
#user input for realist time frames (i.e. not 930am to 1230pm and not 1:30pm-430pm)
# Ideally!- exceptions taken into account (i.e. study session at 430-6pm latest or dentist appointment at 8am) .... recalculate schedule<3 <3 <3 
#input for supporting actions ie (laundry)
#input for what are doing prompt? input for goal compatibility? 
#mini capstone project title = "1% gains every day"---upDATED
#ideally, days would be listed as mon-sun
#user enters times workout out/duration 
#want to differentiate between strength training and cardio (should be 3x3)
#also need multiple graphs/input between strength training exercises including reps/weight 
#graphs are great to show improvement overtime but statements stating percentage in improvements are better ie (" Bicep curl gain in total volume: 10%!") etc.
#Project Status= Build Habit Tracker
#'Earn goal (in this case Health) stars!'