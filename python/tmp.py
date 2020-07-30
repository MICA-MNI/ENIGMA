
# List of genes from ILAE on Complex Epilepsies, 2018, Nat Comms
allepilepsy = ['FANCL', 'BCL11A', 'SCN3A', 'SCN2A', 'TTC21B', 'SCN1A', 'HEATR3', 'BRD7']
focalepilepsy = ['SCN3A', 'SCN2A', 'TTC21B', 'SCN1A']
generalizedepilepsy = ['FANCL', 'BCL11A', 'SCN3A', 'SCN2A', 'TTC21B', 'SCN1A', 'STAT4', 'PCDH7', 'GABRA2', 'KCNN2', 'ATXN1', 'PNPO', 'GRIK1']
jme = ['STX1B']
cae = ['FANCL', 'BCL11A', 'ZEB2']
focalhs = ['C3orf33', 'SLC33A1', 'KCNAB1', 'GJA1']

epigx = {'allepilepsy': allepilepsy, 'focalepilepsy': focalepilepsy,
         'generalizedepilepsy': generalizedepilepsy, 'jme': jme,
         'cae': cae, 'focalhs': focalhs}

# Combine and remove duplicates
allg = epigx['allepilepsy'] + epigx['focalepilepsy'] + epigx['generalizedepilepsy']\
       + epigx['jme'] + epigx['cae'] + epigx['focalhs']
allg = list(dict.fromkeys(allg))
