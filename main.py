from parsing import *
import pandas as pd
# import openpyxl

def printer(country, region, town, settlement, district, street, building, place, index):
    if country:
        print("Cтрана:    " + country)
    if region:
        print("Регион:    " + region)
    if town:
        print("Город:     " + town)
    elif settlement:
        print("Поселение: " + settlement)
    if district:
        print("Район:     " + district)
    if street:
        print("Улица:     " + street)
    if building:
        print("Здание:    " + building)
    if place:
        print("Место:     " + place)
    if index:
        print("Индекс:    " + index)


if __name__ == '__main__':
	# df = pd.read_excel("sources/addresses.xlsx")
	# df = df.sample(n=1000, random_state=42)
	# df = df['Column1'].to_frame()
	# df['country'] = ""
	# print(type(df))
	s = "Нижний Новгород Гор. Нижний Новгород пер. Камчатский 5 "
	# def parsing(s):
	# 	s = str(s)
	# 	return address_parsing(s) #country, region, town, settlement, district, street, building, place, index, result_string =
	country, region, town, settlement, district, street, building, place, index, result_string = address_parsing(s)
	printer(country, region, town, settlement, district, street, building, place, index)
	print(result_string)
	# df['country'], df['region'], df['town'], df['settlement'], df['district'], df['street'], df['building'], df['place'], df['index'], df['result_string'] = zip(*df['Column1'].apply(parsing))
	# df.to_excel(r"/Users/a18573916/Desktop/addr_parse/Addr_parse/results/metric1000.xlsx")



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
