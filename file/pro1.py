"""
Project PSIT61
Data Analysis
-ProjectAVG-
>>Barchart: income/year(each region)

by Jakkawan Intaratchaiyakij
    61070023
"""
import pandas as pd
import pygal
def main():
    df = pd.read_csv('ProjectAVG/income.csv', index_col='Region and province')
    year = list(df)[1:]
    tdf = df.T
    north = list(tdf['Northern Region'])[1:]
    central = list(tdf['Central Region'])[1:]
    neast = list(tdf['Northeastern Region'])[1:]
    south = list(tdf['Southern Region'])[1:]

    line_chart = pygal.Bar()
    line_chart.title = 'Income AVG(Region)'
    line_chart.x_labels = year
    line_chart.add('Central', central)
    line_chart.add('North', north)
    line_chart.add('NorthEast', neast)
    line_chart.add('South', south)
    line_chart.render_to_file('year_region_chart.svg')
    line_chart.render_in_browser()
main()
