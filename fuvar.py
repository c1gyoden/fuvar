class Fuvar:
    def __init__(self, azonosito, indulas, idotartam, tavolsag, viteldij, borravalo, fizetes):
        self.azonosito = azonosito
        self.indulas = indulas
        self.idotartam = idotartam
        self.tavolsag = tavolsag
        self.viteldij = viteldij
        self.borravalo = borravalo
        self.fizetes = fizetes

def tizedes(szam):
    if ',' in szam:
        szam = szam.replace(',', '.')
    elif '.' in szam:
        szam = szam.replace('.', ',')
    return szam

fajl = open('fuvar.csv', 'rt', encoding='utf-8')
fajl.readline()

fuvarok = []

for sor in fajl:
    sor = sor.strip().split(';')
    fuvarok.append(Fuvar(sor[0], sor[1], sor[2], sor[3], sor[4], sor[5], sor[6]))

print('3. feladat:', len(fuvarok), 'fuvar')

hanyfuvar = 0
bevetel = 0
for f in fuvarok:
    if f.azonosito == "6185":
        hanyfuvar += 1
        bevetel += float(tizedes(f.viteldij))

print(f'4. feladat: {hanyfuvar} fuvar alatt: {tizedes(str(bevetel))}$')


stat = {}
for f in fuvarok:
    if f.fizetes in stat.keys():
        stat[f.fizetes] += 1
    else:
        stat[f.fizetes] = 1

print('5. feladat:')
for k,v in stat.items():
    print(f'\t{k}: {v} fuvar')
