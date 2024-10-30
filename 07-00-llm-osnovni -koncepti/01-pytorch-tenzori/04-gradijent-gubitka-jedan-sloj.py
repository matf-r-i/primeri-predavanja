import torch
import torch.nn.functional as F

# Define input and target
x = torch.tensor([1.1])
y = torch.tensor([1.0])

# Initialize weights with requires_grad=True to track computations
w = torch.tensor([2.2], requires_grad=True)
b = torch.tensor([0.0], requires_grad=True)

# Forward pass
z = x * w + b
a = torch.sigmoid(z)
loss = F.binary_cross_entropy(a, y)

# Backward pass
loss.backward()

# Gradients
print("Gradient w.r.t w:", w.grad)
print("Gradient w.r.t b:", b.grad)