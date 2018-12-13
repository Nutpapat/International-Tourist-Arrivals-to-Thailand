""" TOURISM RECEIPTS FROM INTERNATIONAL TOURIST ARRIVALS """
import pandas as pd
import pygal
from pygal.style import DarkStyle
def main():
    """ Receipts from 7 foreign tourists coming to Thailand between 2013 to 2018 """
    lis_y = []
    lis_x = [2013, 2014, 2015, 2016, 2017, 2018]
    check = 0
    data = pd.read_csv('receipts.csv')
    group = data.groupby(['Month'])
    dataframe1 = group.get_group('January-December')
    dataframe2 = group.get_group('January-October')
    year2013 = dataframe1[dataframe1['Year'] == 2013]
    year2014 = dataframe1[dataframe1['Year'] == 2014]
    year2015 = dataframe1[dataframe1['Year'] == 2015]
    year2016 = dataframe1[dataframe1['Year'] == 2016]
    year2017 = dataframe1[dataframe1['Year'] == 2017]
    year2018 = dataframe2[dataframe2['Year'] == 2018]
    lis_eastasia = ea(year2013, year2014, year2015, year2016, year2017, year2018, lis_y, check)
    lis_y = []
    lis_europe = er(year2013, year2014, year2015, year2016, year2017, year2018, lis_y, check)
    lis_y = []
    lis_america = am(year2013, year2014, year2015, year2016, year2017, year2018, lis_y, check)
    lis_y = []
    lis_southasia = sa(year2013, year2014, year2015, year2016, year2017, year2018, lis_y, check)
    lis_y = []
    lis_oceania = oc(year2013, year2014, year2015, year2016, year2017, year2018, lis_y, check)
    lis_y = []
    lis_middleeast = me(year2013, year2014, year2015, year2016, year2017, year2018, lis_y, check)
    lis_y = []
    lis_africa = af(year2013, year2014, year2015, year2016, year2017, year2018, lis_y, check)
    lis_y = []
    chart = pygal.StackedBar(fill=True, stack_from_top=True, style=DarkStyle,\
     x_title='Year', y_title='Tourism Receipts(Million Baht)')
    chart.title = 'TOURISM RECEIPTS FROM INTERNATIONAL TOURIST ARRIVALS (2013 to 2018)'
    chart.x_labels = ['2013', '2014', '2015', '2016', '2017', '2018(Jan-Oct)*']
    chart.y_labels = [0, 50000 , 100000, 150000, 200000, 250000, 300000, 350000, 400000, 450000, \
    500000, 550000, 600000, 650000, 700000, 750000, 800000, 850000, 900000, 950000, 1000000, \
    1050000 , 1100000, 1150000, 1200000, 1250000, 1300000, 1350000, 1400000, 1450000, 1500000, \
    1550000, 1600000, 1650000, 1700000, 1750000, 1800000, 1850000, 1900000]
    chart.value_formatter = lambda x: '%.dM' % x
    chart.add("Eastasia", lis_eastasia)
    chart.add("Europe", lis_europe)
    chart.add("America", lis_america)
    chart.add("Southasia", lis_southasia)
    chart.add("Oceania", lis_oceania)
    chart.add("Middleeast", lis_middleeast)
    chart.add("Africa", lis_africa)
    chart.render_to_file('GraphReceips.svg')
def af(year2013, year2014, year2015, year2016, year2017, year2018, var, check):
    """return africa point (list)"""
    for i in year2013.Africa:
        check += int(i)
    var.append(check)
    check = 0
    for i in year2014.Africa:
        check += int(i)
    var.append(check)
    check = 0
    for i in year2015.Africa:
        check += int(i)
    var.append(check)
    check = 0
    for i in year2016.Africa:
        check += int(i)
    var.append(check)
    check = 0
    for i in year2017.Africa:
        check += int(i)
    var.append(check)
    check = 0
    for i in year2018.Africa:
        check += int(i)
    var.append(check)
    check = 0
    return list(var)
def me(year2013, year2014, year2015, year2016, year2017, year2018, var, check):
    """return middle_east point (list)"""
    for i in year2013.MiddleEast:
        check += int(i)
    var.append(check)
    check = 0
    for i in year2014.MiddleEast:
        check += int(i)
    var.append(check)
    check = 0
    for i in year2015.MiddleEast:
        check += int(i)
    var.append(check)
    check = 0
    for i in year2016.MiddleEast:
        check += int(i)
    var.append(check)
    check = 0
    for i in year2017.MiddleEast:
        check += int(i)
    var.append(check)
    check = 0
    for i in year2018.MiddleEast:
        check += int(i)
    var.append(check)
    check = 0
    return list(var)
def oc(year2013, year2014, year2015, year2016, year2017, year2018, var, check):
    """return oceania point (list)"""
    for i in year2013.Oceania:
        check += int(i)
    var.append(check)
    check = 0
    for i in year2014.Oceania:
        check += int(i)
    var.append(check)
    check = 0
    for i in year2015.Oceania:
        check += int(i)
    var.append(check)
    check = 0
    for i in year2016.Oceania:
        check += int(i)
    var.append(check)
    check = 0
    for i in year2017.Oceania:
        check += int(i)
    var.append(check)
    check = 0
    for i in year2018.Oceania:
        check += int(i)
    var.append(check)
    check = 0
    return list(var)
def sa(year2013, year2014, year2015, year2016, year2017, year2018, var, check):
    """return south_asia point (list)"""
    for i in year2013.SouthAsia:
        check += int(i)
    var.append(check)
    check = 0
    for i in year2014.SouthAsia:
        check += int(i)
    var.append(check)
    check = 0
    for i in year2015.SouthAsia:
        check += int(i)
    var.append(check)
    check = 0
    for i in year2016.SouthAsia:
        check += int(i)
    var.append(check)
    check = 0
    for i in year2017.SouthAsia:
        check += int(i)
    var.append(check)
    check = 0
    for i in year2018.SouthAsia:
        check += int(i)
    var.append(check)
    check = 0
    return list(var)
def am(year2013, year2014, year2015, year2016, year2017, year2018, var, check):
    """return america point (list)"""
    for i in year2013.America:
        check += int(i)
    var.append(check)
    check = 0
    for i in year2014.America:
        check += int(i)
    var.append(check)
    check = 0
    for i in year2015.America:
        check += int(i)
    var.append(check)
    check = 0
    for i in year2016.America:
        check += int(i)
    var.append(check)
    check = 0
    for i in year2017.America:
        check += int(i)
    var.append(check)
    check = 0
    for i in year2018.America:
        check += int(i)
    var.append(check)
    check = 0
    return list(var)
def er(year2013, year2014, year2015, year2016, year2017, year2018, var, check):
    """return europe point (list)"""
    for i in year2013.Europe:
        check += int(i)
    var.append(check)
    check = 0
    for i in year2014.Europe:
        check += int(i)
    var.append(check)
    check = 0
    for i in year2015.Europe:
        check += int(i)
    var.append(check)
    check = 0
    for i in year2016.Europe:
        check += int(i)
    var.append(check)
    check = 0
    for i in year2017.Europe:
        check += int(i)
    var.append(check)
    check = 0
    for i in year2018.Europe:
        check += int(i)
    var.append(check)
    check = 0
    return list(var)
def ea(year2013, year2014, year2015, year2016, year2017, year2018, var, check):
    """return east_asia point (list)"""
    for i in year2013.EastAsia:
        check += int(i)
    var.append(check)
    check = 0
    for i in year2014.EastAsia:
        check += int(i)
    var.append(check)
    check = 0
    for i in year2015.EastAsia:
        check += int(i)
    var.append(check)
    check = 0
    for i in year2016.EastAsia:
        check += int(i)
    var.append(check)
    check = 0
    for i in year2017.EastAsia:
        check += int(i)
    var.append(check)
    check = 0
    for i in year2018.EastAsia:
        check += int(i)
    var.append(check)
    check = 0
    return list(var)
main()
