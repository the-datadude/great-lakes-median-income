import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np

style.use('seaborn-whitegrid')
#Show the different styles.
#fivethirtyeight
#seaborn-pastel
#seaborn-whitegrid
#ggplot
#grayscale


# Make sure to explain that you can load more than one type of file. (For example: txt and csv)
mn_x,mn_y = np.loadtxt('mndata.txt',
                 unpack=True,
                 delimiter=',')


us_x,us_y = np.loadtxt('usincome.txt',
                 unpack=True,
                 delimiter=',')

oh_x,oh_y = np.loadtxt('ohiodatatest.csv',
                 unpack=True,
                 delimiter=',',
                       skiprows=1)

wi_x,wi_y = np.loadtxt('wisconsindata.csv',
                 unpack=True,
                 delimiter=',',
                       skiprows=1)

mi_x,mi_y = np.loadtxt('michigandata.csv',
                 unpack=True,
                 delimiter=',',
                       skiprows=1)

il_x,il_y = np.loadtxt('illinoisdata.csv',
                 unpack=True,
                 delimiter=',',
                       skiprows=1)

in_x,in_y = np.loadtxt('indianadata.csv',
                 unpack=True,
                 delimiter=',',
                       skiprows=1)



# This is the portion of the data study that determines the average growth rate.

StateList = [us_y, mn_y, wi_y,il_y,in_y,mi_y,oh_y]   #Add State as required
StateNames = ["The United States", "Minnesota","Wisconsin", "Illinois", "Indiana", "Michigan", "Ohio"] #Add States as required

#creating an empty list that will contain the average growth rates
growthRateList = []


for i in range(len(StateList)):
    State = StateList[i]
    NextState =StateNames[i]
    count = 0
    CountOfValues = len(State) - 1
    GrowthRateTotal = 0
    for i in State:#Circle through every value in the State
            count = count + 1
            if count == CountOfValues+1:
                break
            else:
                nextnumberinset = State[count] #Find the next value the set
                AnnualGR = float(((nextnumberinset - i) / i))
                GrowthRateTotal = GrowthRateTotal + AnnualGR
    print("The Average Income Growth for {} per year is {:.3f}%".format(NextState,(GrowthRateTotal/CountOfValues*100)))
    growthRateList.append(GrowthRateTotal / CountOfValues * 100)


maxrate = max(growthRateList)
MaxGR=growthRateList. index(maxrate)
maxstate = StateNames[MaxGR]
growthRateList.append(GrowthRateTotal/CountOfValues*100)




# This is how you associate each states information with the plot.
plt.plot(us_x,us_y, label='United States')
plt.plot(oh_x,oh_y, label='Ohio')
plt.plot(wi_x,wi_y, label='Wisconsin')

# Notice how a marker can also be added to the plot.  I chose to have it appear as dots.
plt.plot(mn_x,mn_y, label='Minnesota', marker= '.')
plt.plot(mi_x,mi_y, label='Michigan')
plt.plot(il_x,il_y, label='Illinois')
plt.plot(in_x,in_y, label='Indiana')
plt.title('Historical Great-Lake State Incomes')
plt.ylabel('Income in USD')
plt.xlabel('Year')
plt.legend(title = 'Legend')



# How you add text to a plot.
x_pos = 1995
y_pos = 20000
plt.text(x_pos, y_pos, "The State with the highest \n average income growth is: \n" + maxstate + " : " + str(maxrate), color = 'red', fontsize = 15)

plt.show()


