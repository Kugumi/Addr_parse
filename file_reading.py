def file_reader():
    with open('sources/towns.txt', 'r') as f:
        towns = f.read()

    towns = towns.split(",")

    with open('sources/regions.txt', 'r') as f:
        regions = f.read()

    regions = regions.split(",")

    with open('sources/settlements.txt', 'r') as f:
        settlements = f.read()  # это как-то надо вынести, чтобы каждый раз не выполнялось чтение файлов

    settlements = settlements.split(",")

    return towns, regions, settlements
