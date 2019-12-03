
legends = {('Poe', 'author'): (1809, 1849, 1976), 
    ('Gaudi', 'architect'): (1852, 1906, 1987),
    ('Freud', 'psychoanalyst'): (1856, 1939,1990)}

for eachLegend in legends:
    print("Name: %s\tOccupation: %s" % eachLegend)
    print("Birth: %s\tDeath: %s\tAlbum: %s\n" % legends[eachLegend])
