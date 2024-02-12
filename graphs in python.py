#importing the relevant modules
import matplotlib.pyplot as plt

#plotting graphs in python
#very basic plot, we want something better
x= [1,3,5,10] #this is what we are plotting
plt.plot(x)
plt.show() #this will show the plot we are plotting

#plotting x and y against each other
y=[7,12,21,22]
plt.plot(x,y)
plt.show()

#lets plot a lovely looking plot

#line 1 - points
x= [3,9,14]
y= [2,7,11]
#plotting x and y
plt.plot(x,y,c="red", linewidth= 2, label="line 1")

#line 2 points
x2= [1,15,18]
y2= [0,3,12]
#plotting x2 and y2
plt.plot(x2,y2, c="green", linewidth=2, label="line 2", linestyle="dashed", marker='o', markerfacecolor="orange", markersize=10)
#limits of the axis
#plt.ylim
#plt.xlim

#label the axis and give the plot a title
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.title("Two lines!")

#show the legend on the plot
plt.legend()
#get python to show the plot
plt.show()