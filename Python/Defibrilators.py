import math

# location formula
def distance (long1, long2, lat1, lat2):
    x = (long2-long1)*math.cos((lat1+lat2)/2)
    y = lat2-lat1
    return math.sqrt(x*x+y*y)*6371


# Real inputs
lon = input()
lat = input()
n = int(input())
defib = [None]*n
for i in range(n):
    defib[i] = input()


# # Mock inputs
# lon = "3,879483"
# lat = "43,608177"
# n = int("3")
# defib = [None]*n
# loc = [
#     "1;Maison de la Prevention Sante;6 rue Maguelone 340000 Montpellier;;3,87952263361082;43,6071285339217",
#     "2;Hotel de Ville;1 place Georges Freche 34267 Montpellier;;3,89652239197876;43,5987299452849",
#     "3;Zoo de Lunaret;50 avenue Agropolis 34090 Mtp;;3,87388031141133;43,6395872778854"]
# for i in range(n):
#     defib[i] = loc[i]

# parse long and lati

lon = float(lon.replace(',','.'))
lat = float(lat.replace(',','.'))

# parse defib loactions into a dict of dicts
defibs = dict()
for x in defib:
    x_parse = x.split(';')
    defibs[x_parse[0]]=dict()
    defibs[x_parse[0]]['Name'] = x_parse[1]
    defibs[x_parse[0]]['Address'] = x_parse[2]
    defibs[x_parse[0]]['Phone'] = x_parse[3]
    defibs[x_parse[0]]['Long'] = float(x_parse[4].replace(',','.'))
    defibs[x_parse[0]]['Lat'] = float(x_parse[5].replace(',','.'))

# evaluate location against all of the locations and print the name of the winner

winner=None
winDist=None
for defi in defibs.values():
    dist = distance(lon, defi['Long'],lat, defi['Lat'])
    if winDist == None or dist < winDist:
        winner = defi['Name']
        winDist=dist

print(winner)