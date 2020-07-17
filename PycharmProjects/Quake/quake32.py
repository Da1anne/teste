import json

# the file to be converted
filename = 'Quake2.txt'

# resultant dictionary
conj1 = {}
novo_conjunto = []
# fields in the sample file
dados_players = {'id', 'nome', 'kills', 'old_names'}
players = [dados_players]
status = ['total_kills', 'players']
old_names = []
games = {}

with open(filename) as fh:
    # count variable for employee id creation
    l = 1

    for line in fh:

        # reading line by line from the text file
        description = list(line.split(None, 4))
        if '------------------------------------------------------------' in description:
            description.pop()
        else:
            # for output see below
            print(description)
            novo_conjunto.append(description)

lista_games = []
with open(filename) as fh:
    # count variable for employee id creation
    l = 1
    for [] in novo_conjunto:
        # reading line by line from the text file
        if 'InitGame:' in description:
            # for output see below
            # for automatic creation of id for each employee
            sno1 = 'game' + str(l)

            # loop variable
            i = 0
            # intermediate dictionary
            while i < len:
                # creating dictionary for each employee
                conj1[fields[i]] = description[i]
                i = i + 1

                # appending the record of each employee to
                # the main dictionary
                l = l + 1

# creating json file
out_file = open("test2.json", "w")
json.dump(conj1, out_file, indent=4)
print(conj1)
print(novo_conjunto)
print(lista_games)
#final = games.union(status)

out_file.close()