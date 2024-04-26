class Fuvar:
    def __init__(self, azonosito, indulas, idotartam, tavolsag, viteldij, borravalo, fizetes):
        self.azonosito = azonosito
        self.indulas = indulas
        self.idotartam = idotartam
        self.tavolsag = tavolsag
        self.viteldij = viteldij
        self.borravalo = borravalo
        self.fizetes = fizetes

fajl = open('fuvar.csv', 'rt', encoding='utf-8')
fajl.readline()

fuvarok = []

for sor in fajl:
    sor = sor.strip().split(';')
    fuvarok.append(Fuvar(sor[0], sor[1], sor[2], sor[3], sor[4], sor[5], sor[6]))

