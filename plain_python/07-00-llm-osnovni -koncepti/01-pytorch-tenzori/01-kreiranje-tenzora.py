import torch

# Scalar (0D tensor)
tensor0d = torch.tensor(1)
print(tensor0d)

# Vector (1D tensor)
tensor1d = torch.tensor([1, 2, 3])
print(tensor1d)

# Matrix (2D tensor)
tensor2d = torch.tensor([[1, 2],
[3, 4]])
print(tensor2d)

# 3D Tensor
tensor3d = torch.tensor([[[1, 2], [3, 4]],
[[5, 6], [7, 8]]])
print(tensor3d)
