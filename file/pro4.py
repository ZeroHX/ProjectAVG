"""
Project PSIT61
Data Analysis
-ProjectAVG-
>>Barchart: Top10 highest AVG

by  Suphitsara Cheevanantaporn
    61070230
"""
import pandas as pd
import pygal
from pygal.style import BlueStyle
def main():
    data = {}
    df = pd.read_csv('csv/income.csv', index_col='Region and province')
    tdf = df.T
    region = list(tdf)[1:]
    for i in region:
        #Calculate average and add to dict<data>
        data[i] = float("%.2f" % (sum(list(tdf[i])[1:])/len(list(tdf[i]))))

    #Change from dict to tuple and sort it from value
    data = sorted(data.items(), key=lambda x: x[1], reverse=1)[:10]

    #Create graph
    line_chart = pygal.HorizontalBar(fill=True, interpolate='cubic', style=BlueStyle)
    line_chart.title = 'Top10 highest AVG income'
    #Add bar(Top10 region)
    for j in range(10):
        line_chart.add(data[j][0], data[j][1])
    line_chart.render_in_browser()
    line_chart.render_to_file('graph/top10_avg.svg')
main()

