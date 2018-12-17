""" TOURISM RECEIPTS FROM INTERNATIONAL TOURIST ARRIVALS """
import pandas as pd
import pygal
from pygal.style import NeonStyle
def main():
    """ Receipts from 7 foreign tourists coming to Thailand between 2013 to 2018 """
    lis_y = []
    lis_x = ['EastAsia', 'Europe', 'America', 'SouthAsia', 'Oceania', 'MiddleEast', 'Africa']
    check = 0
    data = pd.read_csv('receipts.csv', encoding="utf-8")
    group = data.groupby(['Month'])
    dataframe = group.get_group('Total')
    total = dataframe[dataframe['Year'] == 'Total']
    lis_eastasia = ea(total, lis_y, check)
    lis_y = []
    lis_europe = er(total, lis_y, check)
    lis_y = []
    lis_america = am(total, lis_y, check)
    lis_y = []
    lis_southasia = sa(total, lis_y, check)
    lis_y = []
    lis_oceania = oc(total, lis_y, check)
    lis_y = []
    lis_middleeast = me(total, lis_y, check)
    lis_y = []
    lis_africa = af(total, lis_y, check)
    lis_y = []
    chart = pygal.HorizontalBar(inner_radius=.45, style=NeonStyle)
    chart.title = 'TOTAL RECEIPTS ALL OF EACH LANDMASS (2013 to 2018)'
    chart.x_title = 'Income from tourists (Million Baht)'
    chart.y_title ='Landmass'
    chart.legend_at_bottom = True
    chart.legend_box_size = 20
    chart.add("Eastasia", lis_eastasia)
    chart.add("Europe", lis_europe)
    chart.add("America", lis_america)
    chart.add("Southasia", lis_southasia)
    chart.add("Oceania", lis_oceania)
    chart.add("Middleeast", lis_middleeast)
    chart.add("Africa", lis_africa)
    chart.render_to_file('BarTotalReceips.svg')
def ea(total, var, check):
    """return east_asia point (list)"""
    for i in total.EastAsia:
        check += int(i)
    var.append(check)
    check = 0
    return list(var)
def er(total, var, check):
    """return europe point (list)"""
    for i in total.Europe:
        check += int(i)
    var.append(check)
    check = 0
    return list(var)
def am(total, var, check):
    """return america point (list)"""
    for i in total.America:
        check += int(i)
    var.append(check)
    check = 0
    return list(var)
def sa(total, var, check):
    """return south_asia point (list)"""
    for i in total.SouthAsia:
        check += int(i)
    var.append(check)
    check = 0
    return list(var)
def oc(total, var, check):
    """return oceania point (list)"""
    for i in total.Oceania:
        check += int(i)
    var.append(check)
    check = 0
    return list(var)
def me(total, var, check):
    """return middle_east point (list)"""
    for i in total.MiddleEast:
        check += int(i)
    var.append(check)
    check = 0
    return list(var)
def af(total, var, check):
    """return africa point (list)"""
    for i in total.Africa:
        check += int(i)
    var.append(check)
    check = 0
    return list(var)
main()
