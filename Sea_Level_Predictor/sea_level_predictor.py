import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
    # Read data from file
        df=pd.read_csv('epa-sea-level.csv')
        y=df['CSIRO Adjusted Sea Level']
        x=df['Year']

    # Create scatter plot
        plt.scatter(x,y)        


    # Create first line of best fit
        slope1,intercept1,r_value1,p_value1,std_err1=linregress(x,y)
        x_pred=np.arange(1880,2051)
        # y_pred=mx+b
        y_pred=slope1*x_pred+intercept1    

        plt.plot(x_pred,y_pred,color='red',linestyle='--')
        plt.title('Rise in Sea Level')
        plt.ylabel('Sea Level (inches)')
        plt.xlabel('Year')


    # Create second line of best fit
        df2=df[df.Year>=2000]
        x2=df2['Year']
        y2=df2['CSIRO Adjusted Sea Level']
        slope2,intercept2,r_value2,p_value2,std_err2=linregress(x2,y2)

        x_pred2=pd.Series([i for i in range(2000,2051)])
        y_pred2= slope2* x_pred2+ intercept2


    # Add labels and title
        plt.plot(x_pred2,y_pred2,color='green')
        plt.title('Rise in Sea Level')
        plt.ylabel('Sea Level (inches)')
        plt.xlabel('Year')

    # Save plot and return data for testing (DO NOT MODIFY)
        plt.savefig('sea_level_plot.png')
        return plt.gca()