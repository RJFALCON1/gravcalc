import pandas as pd
import math
df = pd.read_csv('Class 131/main.csv')
starname = df['Star_name'].tolist()
mass = df['Mass'].tolist()
radius = df['Radius'].tolist()
distance = df['Distance'].tolist()
newstarname = []
newmass = []
newradius = []
newdistance = []
newgravity = []
for i in range(1,50,2):
    r = float(radius[i])*6.957e+8
    newradius.append(r)
    m = float(mass[i])*1.989e+30
    newmass.append(m)
    newdistance.append(distance[i])
    g = 6.67 * pow(10,-11) * m/(r*r)
    newgravity.append(g)
    newstarname.append(starname[i])
newdf = pd.DataFrame({'starname':newstarname,'mass':newmass,'radius':newradius,'distance':newdistance,'gravity':newgravity})
newdf.to_csv('Class 131/calculated.csv')