"""
Project PSIT61
Data Analysis
-ProjectAVG-
>>Barchart: income/year(Whole Region)

by Jakkawan Intaratchaiyakij
    61070023
"""
import pandas as pd
import pygal
def main():
    chart = []
    df = pd.read_csv('income.csv', index_col='Region and province')
    year = list(df)[1:]
    tdf = df.T

    line_chart = pygal.Line()
    line_chart.title = 'Income for each year'
    line_chart.x_labels = year
    for i in year:
        avg1 = tdf['Whole Kingdom'][i]
        #avg = (sum(list(df[i])[1:])-(tdf['Central Region'][i]+tdf['Northern Region'][i]+tdf['Northeastern Region'][i]+\
        #tdf['Southern Region'][i]+tdf['Whole Kingdom'][i]))/len(list(df[i])[1:])
        chart.append(float('%.2f' % avg1))
    line_chart.add("Year", chart)
    line_chart.render_to_file('year_whole_chart.svg')
    line_chart.render_in_browser()

main()
