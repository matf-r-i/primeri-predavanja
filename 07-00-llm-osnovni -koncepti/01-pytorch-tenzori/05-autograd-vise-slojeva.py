import torch
import torch.nn as nn
import torch.optim as optim

# Define a simple neural network
class SimpleNet(nn.Module):
    def __init__(self):
        super(SimpleNet, self).__init__()
        self.fc1 = nn.Linear(10, 5)  # Input layer to hidden layer
        self.relu = nn.ReLU()
        self.fc2 = nn.Linear(5, 1)   # Hidden layer to output layer
        self.sigmoid = nn.Sigmoid()

    def forward(self, x):
        h = self.relu(self.fc1(x))
        y_hat = self.sigmoid(self.fc2(h))
        return y_hat

# Instantiate the network
net = SimpleNet()

# Define loss function and optimizer
criterion = nn.BCELoss()
optimizer = optim.SGD(net.parameters(), lr=0.01)

# Sample data
inputs = torch.randn(1, 10)
labels = torch.tensor([1.0]).unsqueeze(1)

# Training loop
optimizer.zero_grad()          # Clear gradients
outputs = net(inputs)          # Forward pass
loss = criterion(outputs, labels)  # Compute loss
loss.backward()                # Backward pass (compute gradients)
optimizer.step()               # Update parameters

# Accessing gradients
for name, param in net.named_parameters():
    if param.requires_grad:
        print(f"Gradient of {name}: {param.grad}")