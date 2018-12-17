""" TOURISM RECEIPTS FROM INTERNATIONAL TOURIST ARRIVALS """
import pandas as pd
import pygal
from pygal.style import DarkColorizedStyle
def main():
    """ Ranking the income of foreign tourists into Thailand. """
    lis_y = []
    lis_x = ['China', 'Russia', 'Malaysia', 'United Kingdom', 'Australia', 'USA', 'Korea', 'Japan', 'Germany', 'India']
    check = 0
    data = pd.read_csv('receipts.csv', encoding="utf-8")
    group = data.groupby(['Month'])
    dataframe = group.get_group('Total')
    total = dataframe[dataframe['Year'] == 'Total']
    lis_china = cn(total, lis_y, check)
    lis_y = []
    lis_russia = rs(total, lis_y, check)
    lis_y = []
    lis_malaysia = ml(total, lis_y, check)
    lis_y = []
    lis_united_kingdom = un(total, lis_y, check)
    lis_y = []
    lis_australia = ast(total, lis_y, check)
    lis_y = []
    lis_usa = us(total, lis_y, check)
    lis_y = []
    lis_korea = kr(total, lis_y, check)
    lis_y = []
    lis_japan = jp(total, lis_y, check)
    lis_y = []
    lis_germany = gm(total, lis_y, check)
    lis_y = []
    lis_india = id(total, lis_y, check)
    lis_y = []
    chart = pygal.HorizontalBar(style=DarkColorizedStyle)
    chart.title = 'TOP 10 TOTAL INCOME OF FOREIGN TOURISTS INTO THAILAND EACH COUNTRY (2013 to 2018)'
    chart.x_title = 'Income from tourists (Million Baht)'
    chart.y_title ='Country'
    chart.legend_at_bottom = True
    chart.legend_box_size = 20
    chart.add("China", lis_china)
    chart.add("Russia", lis_russia)
    chart.add("Malaysia", lis_malaysia)
    chart.add("United Kingdom", lis_united_kingdom)
    chart.add("Australia", lis_australia)
    chart.add("USA", lis_usa)
    chart.add("Korea", lis_korea)
    chart.add("Japan", lis_japan)
    chart.add("Germany", lis_germany)
    chart.add("India", lis_india)
    chart.render_to_file('BarRankingIncome.svg')
def cn(total, var, check):
    """return east_asia point (list)"""
    for i in total.China:
        check += int(i)
    var.append(check)
    check = 0
    return list(var)
def rs(total, var, check):
    """return east_asia point (list)"""
    for i in total.Russia:
        check += int(i)
    var.append(check)
    check = 0
    return list(var)
def ml(total, var, check):
    """return east_asia point (list)"""
    for i in total.Malaysia:
        check += int(i)
    var.append(check)
    check = 0
    return list(var)
def un(total, var, check):
    """return east_asia point (list)"""
    for i in total.UnitedKingdom:
        check += int(i)
    var.append(check)
    check = 0
    return list(var)
def ast(total, var, check):
    """return east_asia point (list)"""
    for i in total.Australia:
        check += int(i)
    var.append(check)
    check = 0
    return list(var)
def us(total, var, check):
    """return east_asia point (list)"""
    for i in total.USA:
        check += int(i)
    var.append(check)
    check = 0
    return list(var)
def kr(total, var, check):
    """return east_asia point (list)"""
    for i in total.Korea:
        check += int(i)
    var.append(check)
    check = 0
    return list(var)
def jp(total, var, check):
    """return east_asia point (list)"""
    for i in total.Japan:
        check += int(i)
    var.append(check)
    check = 0
    return list(var)
def gm(total, var, check):
    """return east_asia point (list)"""
    for i in total.Germany:
        check += int(i)
    var.append(check)
    check = 0
    return list(var)
def id(total, var, check):
    """return east_asia point (list)"""
    for i in total.India:
        check += int(i)
    var.append(check)
    check = 0
    return list(var)
main()
