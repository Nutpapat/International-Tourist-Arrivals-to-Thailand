"""Number_of_foreigner_travel_to_thailand_in_rains_season"""
import pandas as pd
import matplotlib.pyplot as plt
def main():
    """7 land mass foreigner travel to thailand between 2013 to 2018 in rains_season"""
    lis_y = []
    lis_x = [2013, 2014, 2015, 2016, 2017, 2018]
    check = 0
    data = pd.read_csv('data.csv')
    group = data.groupby(['Season'])
    dataframe = group.get_group('rains')
    year2013 = dataframe[dataframe['Year'] == 2013]
    year2014 = dataframe[dataframe['Year'] == 2014]
    year2015 = dataframe[dataframe['Year'] == 2015]
    year2016 = dataframe[dataframe['Year'] == 2016]
    year2017 = dataframe[dataframe['Year'] == 2017]
    year2018 = dataframe[dataframe['Year'] == 2018]
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
    ax = plt.gca()
    ax.set_title('ปริมาณชาวต่างชาติที่เข้าประเทศไทยตอนฤดูฝนช่วง 6 ปี',fontname='JasmineUPC',fontsize='20')
    ax.set_xlabel('ปี',fontname='JasmineUPC',fontsize='20')
    ax.set_ylabel('จำนวนชาวต่างชาติ (หน่วย10ล้าน)',fontname='JasmineUPC',fontsize='20')
    ax.set_ylim([0, 10000000])
    plt.text(2013,9400000,'eastasia', color="mediumblue")
    plt.text(2013,9000000,'europe', color="magenta")
    plt.text(2013,8600000,'america', color="forestgreen")
    plt.text(2013,8200000,'oceania', color="crimson")
    plt.text(2013,7800000,'middleeast', color="chocolate")
    plt.text(2013,7400000,'africa', color="black")
    plt.text(2013,7000000,'southasia', color="darkviolet")
    plt.stackplot(lis_x, lis_eastasia, color="mediumblue")#สีน้ำเงิน
    plt.stackplot(lis_x, lis_europe, color="magenta")#สีม่วง
    plt.stackplot(lis_x, lis_america, color="forestgreen")#สีเขียว
    plt.stackplot(lis_x, lis_southasia, color="darkviolet")#ม่วงเข้ม
    plt.stackplot(lis_x, lis_oceania, color="crimson")#สีแดง
    plt.stackplot(lis_x, lis_middleeast, color="chocolate")#สีน้ำตาล
    plt.stackplot(lis_x, lis_africa, color="black")#สีดำ
    plt.show()
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
