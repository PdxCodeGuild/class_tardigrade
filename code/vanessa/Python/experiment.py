import schedule
import time
schedule.Set
from bokeh.plotting import figure, show

w= figure(plot_width=400, plot_height=400, title="Goal Tracker", x_axis_label = "days", y_axis_label= "goals met")
w.star([1,2,3,4,5,6,7,], [6, 7, 10, 4, 5,10,7], size=15, line_color="navy", fill_color="orange", fill_alpha=0.5)
# w= figure(title="Goal Tracker", x_axis_label = "days", y_axis_label= "goals met")
# w.line(x, y, legend_label="consistency.", line_width=2)
progress= input("do you want to see your progress? (y/n)")
if progress == "y":
    show(w)
show(w) # show the resultsyy