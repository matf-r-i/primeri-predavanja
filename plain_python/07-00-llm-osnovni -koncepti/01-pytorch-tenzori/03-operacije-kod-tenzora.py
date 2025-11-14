import torch

# kreiranje tenzora
tenzor3d = torch.tensor([[[1, 2], [3, 4]],
[[5, 6], [7, 8]]])
print(tenzor3d)

# ocitavanje oblika tenzora
oblik = tenzor3d.shape
print(oblik)

# promena obila tenzora 2x2x2 -> 4x2
tenzor2d42 = tenzor3d.reshape(4, 2)
print(tenzor2d42)

# promena obila tenzora 2x2x2 -> 2x4
tenzor2d24 = tenzor3d.reshape(2, 4)
print(tenzor2d24)

# nije moguca promena obila tenzora 2x2x2 -> 2x3
#tenzor2d23 = tensor3d.reshape(2, 3)
#print(tenzor2d23)

# promena obila tenzora 2x2x2 -> 8
tenzor1d = tenzor3d.reshape(8)
print(tenzor1d)

# transponovanje 1d tenzora
tenzor1dt = tenzor1d.T
print(tenzor1dt)

# transponovanje 2d tenzora
tenzor2d24t = tenzor2d24.T
print(tenzor2d24t)

# transponovanje 3d tenzora
tenzor3dt = tenzor3d.T
print(tenzor3dt)

# mnozenje dva 2d tenzora
rezultat = tenzor2d24 @ tenzor2d42
print(rezultat)

# mnozenje dva 2d tenzora
rezultat = tenzor2d42 @ tenzor2d24
print(rezultat)

# mnozenje dva 3d tenzora
rezultat = tenzor3d @ tenzor3dt
print(rezultat)

# mnozenje 2d i 1d tenzora
tenzor1d2 = torch.tensor([5, 5])
rezultat = tenzor2d42 @ tenzor1d2
print(rezultat)

# mnozenje 1d i 2d tenzora
rezultat =  tenzor1d2 @ tenzor2d24
print(rezultat)

# mnozenje 3d i 1d tenzora
rezultat = tenzor3d @ tenzor1d2
print(rezultat)

# mnozenje 1d i 3d tenzora
rezultat = tenzor1d2 @ tenzor3d
print(rezultat)
