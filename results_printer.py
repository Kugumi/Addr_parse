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
