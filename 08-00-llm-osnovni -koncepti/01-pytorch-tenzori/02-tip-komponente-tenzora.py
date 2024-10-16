import torch

# ocitavanje tipa komponente tenzora 
tensor3di = torch.tensor([[[1, 2], [3, 4]],
[[5, 6], [7, 8]]])
print(tensor3di.dtype) 

# promena tipa komponente tenzora
tensor3df = tensor3di.to(torch.float32)
print(tensor3df.dtype) 
