"""
Project PSIT61
Data Analysis
-ProjectAVG-
>>Barchart_Horizon: income/another province in region

by  Jakkawan Intaratchaiyakij
    61070023
"""
import pandas as pd
import pygal
#from pygal.style import BlueStyle
def main():
    """ This graph is plot about A Average of income in each region on each year """ 
    df = pd.read_csv('income.csv', index_col='Region and province')
    #Transpose it to change index from (year>>region)
    tdf = df.T
    #Send Datafrme to function each Region
    central(df, tdf)
    north(df, tdf)
    neast(df, tdf)
    south(df, tdf)

def central(df, tdf):
    """ Data for Central Region """
    region = 'Central'
    cen = df['Central Region':'Northern Region'][1:]
    cen_lst = list(cen.T)
    lst = []
    for i in cen_lst:
        avg = sum(list(cen.T[i])[1:])/len(list(cen.T[i])[1:])
        lst.append(avg)
    graph(cen_lst, lst, region)


def north(df, tdf):
    """ Data for Northen Region """
    region = 'Northern'
    north = df['Northern Region':'Northeastern Region'][1:]
    north_lst = list(north.T)
    lst = []
    for i in north_lst:
        avg = sum(list(north.T[i])[1:])/len(list(north.T[i])[1:])
        lst.append(avg)
    graph(north_lst, lst, region)

def neast(df, tdf):
    """ Data for Northeastern Region """
    region = 'Northeastern'
    neast = df['Northeastern Region':'Southern Region'][1:]
    neast_lst = list(neast.T)
    lst = []
    for i in neast_lst:
        avg = sum(list(neast.T[i])[1:])/len(list(neast.T[i])[1:])
        lst.append(avg)
    graph(neast_lst, lst, region)

def south(df, tdf):
    """ Data for Southern Region """
    region = 'Southern'
    south = df['Southern Region':][1:]
    south_lst = list(south.T)
    lst = []
    for i in south_lst:
        avg = sum(list(south.T[i])[1:])/len(list(south.T[i])[1:])
        lst.append(avg)
    graph(south_lst, lst, region)

def graph(region, data, reg):
    """ Function plot graph """
    line_chart = pygal.HorizontalBar()
    line_chart.title = '%s Region Income average in each year' % reg
    for i in range(len(region)):
        line_chart.add(region[i], data[i])
    line_chart.render_in_browser()
    line_chart.render_to_file('%s.svg' % reg)


main()
