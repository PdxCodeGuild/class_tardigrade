#Habit Tracker
from typing import Counter
import schedule
import time
schedule.Set
from bokeh.plotting import figure, show
# from datetime import datetime
# d = datetime.now()
# print(d)


counter=[0]

def goal1(message='drink water'):
    print(message)
    counts = 0
    accomplished= input("Task complete? (y/n) ")
    if accomplished == "y":
        print("Yay-one step closer!")    
        counts= counts + 1
        counter.append(counts)
        print(counter)
    if accomplished == "n":
        print("keep trying!")

def goal2(message='work out'):
    print("time to", message)
    accomplished= input("Task complete? (y/n) ")
    counts=0
    if accomplished == "y":
        print("Yay-one step closer!")    
        counts= counts + 1
        counter.append(counts)
        print(counter)
    if accomplished == "n":
        print("keep trying!")

def goal3(message='sleep 8 hours'):
    print("time to", message)
    accomplished= input("Task complete? (y/n) ")
    counts=0
    if accomplished == "y":
        counts= counts + 1
        counter.append(counts)
        print(counter)
        print("Yay-one step closer!")    
    if accomplished == "n":
        print("keep trying!")

def goal4(message='wake up!Drink a glass of water- Cheers!'):
    print("time to", message)
    accomplished= input("Task complete? (y/n) ")
    counts=0
    if accomplished == "y":
        print("Yay-one step closer!")    
        counts= counts + 1
        counter.append(counts)
        print(counter)
    if accomplished == "n":
        print("keep trying!")

def goal5(message='sleep 8 hours'):
    print("time to", message)
    accomplished= input("Task complete? (y/n) ")
    counts=0
    if accomplished == "y":
        print("Yay-one step closer!")    
        counts= counts + 1
        counter.append(counts)
        print(counter)
    if accomplished == "n":
        print("keep trying!")


def congrats (message='Congratulations! Keep up the great work!'):
    print(message)
    total=(len(counter))
    return total


schedule.every(1).minutes.do(goal1)
schedule.every(5).to(10).minutes.do(goal5)
schedule.every(5).to(10).days.do(goal1)
schedule.every(1).hour.do(goal2, )
schedule.every().day.at("13:45").do(goal2)
schedule.every().day.at("13:46:30").do(goal3)
schedule.every().day.at("13:47").do(goal4)
# schedule.every().day.at("14:78").do(daily_affirmation)
schedule.every().day.at("13:48:30").do(congrats)


# for i in range(120,0,-1):
#      time.sleep(1)
#      schedule.run_pending()  

final= (len(counter))-1
print(final)

progress= input("do you want to see your progress? (y/n)")
number_of_days= [0,1,2,3,4,5,6,7]
final_counts=[4,5,6,5,5,10]
final_counts.append(final)

def success():
    w= figure(plot_width=400, plot_height=400, title="Goal Tracker", x_axis_label = "days", y_axis_label= "goals met")
    w.star(number_of_days, final_counts, size=15, line_color="navy", fill_color="orange", fill_alpha=0.5)
    show(w)


if progress == "y":
   (success())



#end of day, add to input list, each number = each day. use input list in graph for 10 days/30 days
#maybe put final graph in seperate function or build graph day by day? 

