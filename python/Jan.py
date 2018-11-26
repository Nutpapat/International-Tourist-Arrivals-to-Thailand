

import pandas as pd





df = pd.read_csv('Book2.csv')







years = df.ปี #df.คือการนำปีทั้งหมดมาเป็น list
year_all = []
for year in years: #เก็บปีทั้งหมดว่ามีกี่ปี
    if year not in year_all:
        year_all.append(year)



def kindofaccident(): #ฟังก์ชันหาประเภทอุบัติเหตุว่ามีอะไรบ้าง
    accidents = df.accident
    accident_all = []
    for accident in accidents:
        if accident not in accident_all:
            accident_all.append(accident)
    return accident_all




def injured_dicc(): #ฟังก์ชันเก็บจำนวนคนบาดเจ็บในแต่ละปี
    injured_dic = {}
    injured = df.injured
    year_b = year_all[0]
    people_injured = 0
    for i in year_all:
        injured_dic[year_b] = people_injured #ถ้าปีเปลี่ยนก็เพิ่มจำนวนคนบาดเจ็บเข้าไปใน dict
        people_injured = 0
        for people, year in zip(injured,years): #เช็คคนกับจำนวนปีว่าตรงกันไหมถ้าตรงก็บวกคนบาดเจ็บ
            if year == i:
                people_injured += people
        year_b = i
    injured_dic[year_b] = people_injured
    list_injured = [injured_dic[year] for year in year_all]
    return list_injured
            





def death_year(): #ฟังก์ชันเก็บจำนวนคนเสียชีวิตในแต่ละปี
    death = df.death
    death_dic = {} 
    people_death = 0
    year_b = year_all[0]
    for i in year_all:
        death_dic[year_b] = people_death
        people_death = 0
        for people, year in zip(death, years):
            if year == i:
                people_death += people
        year_b = i
    death_dic[year_b] = people_death
    list_death = [death_dic[year] for year in year_all]
    return list_death





def accident_year(): #เช็คจำนวนครั้งทั้งหมดของแต่ละอุบัติเหตุ
    accident_all = df.accident
    count_accident = 0
    dic_acc = {}
    accident_b = 0
    for accident in kindofaccident():
        dic_acc[accident_b] = count_accident
        count_accident = 0
        for accidents in accident_all:
            if accident == accidents:
                count_accident += 1
        accident_b = accident
        dic_acc[accident_b] = count_accident
    return dic_acc
                
                
            
         
    





accident_top4 = sorted(accident_year().values()) #หาจำนวน top4
accident_top4.sort(reverse=True)
accident_top4_list = []




for i in range(4): # หาจำนวน top4 เข้าไปใน list เป็นจำนวน ครั้งที่มากที่สุดก่อน
    accident_top4_list.append(list(accident_year().keys())[list(accident_year().values()).index(accident_top4[i])])






def accident_count_year(accident_choice): #เช็คจำนวนการเกิดอุบัติเหตุในแต่ละปี
    accident_count = {}
    year_b = year_all[0]
    count = 0
    accidents = df.accident
    for i in year_all:
        accident_count[year_b] = count
        count = 0
        for accident, year in zip(accidents, years):
            if accident == accident_choice and year == i:
                count += 1
        year_b = i
    accident_count[year_b] = count
    return accident_count

def grah_line(): #ฟังก์ชันสร้างกราฟ
    import pygal
    line_chart = pygal.Bar() #เลือก type กราฟ
    line_chart.title = 'TOP_4 accident in 2544-2556'
    line_chart.x_labels = year_all
    for i in accident_top4_list: #สร้างแค่ top 4
        accident_add = accident_count_year(i)
        list_accident_count = [accident_add[year] for year in year_all] #นำค่าในแต่ละปีมาใส่
        line_chart.add(i, list_accident_count) #เพิ่มค่า
        line_chart.render_to_file('line.svg') #แปลงไฟล์
grah_line()


