def file_reader():
    with open('sources/towns.txt', 'r') as f:
        towns = f.read()

    towns = towns.split(",")[0]

    with open('sources/regions.txt', 'r') as f:
        regions = f.read()

    regions = regions.split(",")[0]

    with open('sources/settlements.txt', 'r') as f:
        settlements = f.read()  # это как-то надо вынести, чтобы каждый раз не выполнялось чтение файлов

    settlements = settlements.split(",")[0]

    return towns, regions, settlements
