"""
Project PSIT61
Data Analysis
-ProjectAVG-
"""
import pandas as pd
import pygal
def main():
    df = pd.read_csv('region.csv', index_col='Region')
    tdf = df.T
    north = list(tdf['Northern Region'])[1:]
    central = list(tdf['Central Region'])[1:]
    neast = list(tdf['Northeastern Region'])[1:]
    south = list(tdf['Southern Region'])[1:]

    line_chart = pygal.Bar()
    line_chart.title = 'Income AVG(Region)'
    line_chart.x_labels = ('2541', '2543', '2545', '2547', '2549', '2550', '2552', '2554', '2556', '2558')
    line_chart.add('Central', central)
    line_chart.add('North', north)
    line_chart.add('NorthEast', neast)
    line_chart.add('South', south)
    line_chart.render_in_browser()
main()