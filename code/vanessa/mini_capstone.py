#Habit Tracker
import schedule
import time
schedule.Set
from bokeh.plotting import figure, show

w= figure(plot_width=400, plot_height=400, title="Goal Tracker", x_axis_label = "days", y_axis_label= "goals met")
w.star([1,2,3,4,5,6,7,], [6, 7, 10, 4, 5,10,7], size=15, line_color="navy", fill_color="orange", fill_alpha=0.5)
progress= input("do you want to see your progress? (y/n)")
if progress == "y":
    show(w)
else:
    print("Ok!")

# def daily_affirmation ():
#     with open('affirmations.csv','r') as file:
#         contents = file.read()
#         line = contents.split('\n')
#     for j in line:
#         j=1
#         if j < 31:
#              time.sleep(4)
#              print(line[j])
#              j += 1

# def counter(global met_goals ):
#     global met_goals0
#     return global met_goals    

def goal1(message='drink water'):
    print(message)
    accomplished= input("Task complete? (y/n) ")
    if accomplished == "y":
        print("Yay-one step closer!")
    if accomplished == "n":
        print("keep trying!")

def goal2(message='work out'):
    print("time to", message)
    accomplished= input("Task complete? (y/n) ")
    if accomplished == "y":
        print("Yay-one step closer!")   
    if accomplished == "n":
        print("keep trying!")

def goal3(message='sleep 8 hours'):
    print("time to", message)
    accomplished= input("Task complete? (y/n) ")
    if accomplished == "y":
        print("Yay-one step closer!")    
    if accomplished == "n":
        print("keep trying!")

def goal4(message='wake up!Drink a glass of water- Cheers!'):
    print("time to", message)
    accomplished= input("Task complete? (y/n) ")
    if accomplished == "y":
        print("Yay-one step closer!")   
    if accomplished == "n":
        print("keep trying!")

def goal5(message='get steps in'):
    print("time to", message)
    accomplished= input("Task complete? (y/n) ")
    if accomplished == "y":
        print("Yay-one step closer!")
    if accomplished == "n":
        print("keep trying!")

def congrats (message='Congratulations! Keep up the great work!'):
    print(message)


schedule.every(15).minutes.do(goal1)
schedule.every(15).to(30).minutes.do(goal5)
schedule.every(5).to(10).days.do(goal1)
schedule.every(1).hour.do(goal2, )
schedule.every().day.at("03:05").do(goal2)
schedule.every().day.at("03:05:30").do(goal3)
schedule.every().day.at("03:04").do(goal4)
# schedule.every().day.at("14:58").do(daily_affirmation)
schedule.every().day.at("03:05").do(congrats)

while True:
    schedule.run_pending()
    time.sleep(1)


