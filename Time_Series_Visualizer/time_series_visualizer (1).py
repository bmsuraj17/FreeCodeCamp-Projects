import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv',index_col='date')
df.index=pd.to_datetime(df.index)

# Clean data
df = df[(df.value>=df.value.quantile(0.025)) & (df.value<=df.value.quantile(0.975))]



def draw_line_plot():

    # Draw line plot
    fig,ax=plt.subplots(figsize=(15,5))
    plt.plot(df.index,df.value,color='firebrick')
    plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    plt.xlabel('Date')
    plt.ylabel('Page Views')


    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar=df.copy()
    df_bar['month']=df_bar.index.month_name()
    df_bar['year']=df_bar.index.year
    month_list=["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    df_bar['month']=df_bar.month.astype('category').cat.set_categories(month_list,ordered=True)

    df_bar = df_bar.groupby(['year','month']).value.mean().unstack()

    # Draw bar plot

    fig = df_bar.plot.bar(figsize=(12,6),legend=True,xlabel='Years', ylabel='Average Page Views').figure
    ax=plt.gca()
    ax.legend(title='Months')
    # plt.show()

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]
    months_list= ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    df['month']=df_box.month.astype('category').cat.set_categories(months_list,ordered=True)

    # Draw box plots (using Seaborn)
    fig,ax=plt.subplots(1,2,figsize=(15,5))
    ax[0]=sns.boxplot(x=df_box['year'],y=df_box['value'],ax=ax[0])
    ax[0].set_title('Year-wise Box Plot (Trend)')
    ax[0].set_xlabel('Year')
    ax[0].set_ylabel('Page Views')
    ax[0].set_yticks(range(0, 220000, 20000))

    ax[1]=sns.boxplot(x=df_box['month'],y=df_box['value'],ax=ax[1],order=months_list)
    ax[1].set_title('Month-wise Box Plot (Seasonality)')
    ax[1].set_xlabel('Month')
    ax[1].set_ylabel('Page Views')
    ax[1].set_yticks(range(0, 220000, 20000))






    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
