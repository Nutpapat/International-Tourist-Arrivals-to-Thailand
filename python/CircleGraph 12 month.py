"""Percentages_of_foreigner_travel_to_thailand_in_years_2017"""
import pandas as pd
import matplotlib.pyplot as plt
def main():
    """foreigner travel to thailand between january to december in 2017"""
    data = pd.read_csv('data.csv')
    group = data.groupby(['Year'])
    dataframe = group.get_group(2017)
    january = dataframe[dataframe['Month'] == 'January']
    february = dataframe[dataframe['Month'] == 'February']
    march = dataframe[dataframe['Month'] == 'March']
    april = dataframe[dataframe['Month'] == 'April']
    may = dataframe[dataframe['Month'] == 'May']
    june = dataframe[dataframe['Month'] == 'June']
    july = dataframe[dataframe['Month'] == 'July']
    august = dataframe[dataframe['Month'] == 'August']
    september = dataframe[dataframe['Month'] == 'September']
    october = dataframe[dataframe['Month'] == 'October']
    november = dataframe[dataframe['Month'] == 'November']
    december = dataframe[dataframe['Month'] == 'December']
    ax = plt.gca()
    ax.set_title('เปอร์เซ็นต์ของชาวต่างชาติที่เข้าไทยในแต่ละเดือน',fontname='JasmineUPC',fontsize='20')
    ax.set_xlabel('ปี 2017',fontname='JasmineUPC',fontsize='20')
    lis_colors = ['#FFFF00', '#FF0000', '#FFD700', '#FFE4E1', '#DA70D6', '#7FFF00', '#FFFFFF', '#D2691E', '#7B68EE', '#FF00FF', '#F08080', '#228B22']
    lis_name = ['January','february','march','april','may','june','july','august','september','october','november','december']
    plt.pie([int(january.Total),int(february.Total),int(march.Total),int(april.Total),int(may.Total)\
            ,int(june.Total),int(july.Total),int(august.Total),int(september.Total),int(october.Total)\
            ,int(november.Total),int(december.Total)], labels=lis_name, autopct='%.2f%%', shadow=1, colors=lis_colors)
    plt.show()
main()
