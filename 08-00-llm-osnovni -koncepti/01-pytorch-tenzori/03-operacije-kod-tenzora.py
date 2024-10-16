import torch

# kreiranje tenzora
tensor3d = torch.tensor([[[1, 2], [3, 4]],
[[5, 6], [7, 8]]])
print(tensor3d)

# ocitavanje oblika tenzora
oblik = tensor3d.shape
print(oblik)

# promena obila tenzora 2x2x2 -> 4x2
tenzor2d42 = tensor3d.reshape(4, 2)
print(tenzor2d42)

# promena obila tenzora 2x2x2 -> 2x4
tenzor2d24 = tensor3d.reshape(2, 4)
print(tenzor2d24)

# nije moguca promena obila tenzora 2x2x2 -> 2x3
#tenzor2d23 = tensor3d.reshape(2, 3)
#print(tenzor2d23)

# promena obila tenzora 2x2x2 -> 8
tenzor1d = tensor3d.reshape(8)
print(tenzor1d)