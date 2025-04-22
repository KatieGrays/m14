
def main():
    winner = ''
    pakurispecies = set()
    highest = 0
    with open('contest.txt', 'r') as file:
        filelines = file.readlines()

    for line in filelines:
        fileline = line.strip().split(',')
        trainername = fileline[0]
        pakurilist = fileline[1:]


        for pakuri in pakurilist:
            species, level = pakuri.split('-')
            level = int(level)
            pakurispecies.add(species)

            if level > highest:
                highest = level
                winner = trainername

    with open('winner.txt', 'w') as file:
        file.write(winner)

    with open('pakuri.txt', 'w') as file:
        for species in sorted(pakurispecies):
            file.write(species + '\n')





if __name__ == "__main__":
    main()
