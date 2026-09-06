"""
Lesson 27: Your First Neural Network (PyTorch)

Demonstrates building, training, and evaluating a simple feedforward
neural network - the foundational architecture behind modern deep
learning - using PyTorch, applied to the same pass/fail prediction
problem from Lesson 25's classification model.
"""

import torch
import torch.nn as nn
import torch.optim as optim


class SimpleNet(nn.Module):
    """A small feedforward neural network: 2 inputs -> 4 hidden -> 1 output."""

    def __init__(self):
        super().__init__()
        self.layer1 = nn.Linear(2, 4)
        self.layer2 = nn.Linear(4, 1)
        self.relu = nn.ReLU()
        self.sigmoid = nn.Sigmoid()

    def forward(self, x):
        x = self.relu(self.layer1(x))
        x = self.sigmoid(self.layer2(x))
        return x


# Features: [hours_studied, previous_score] (normalized roughly to 0-1 range)
X = torch.tensor([
    [0.1, 0.4], [0.2, 0.45], [0.3, 0.55], [0.4, 0.6],
    [0.5, 0.7], [0.6, 0.75], [0.7, 0.85], [0.8, 0.9]
], dtype=torch.float32)

# Labels: 0 = fail, 1 = pass
y = torch.tensor([[0], [0], [0], [1], [1], [1], [1], [1]], dtype=torch.float32)

model = SimpleNet()
criterion = nn.BCELoss()  # Binary Cross Entropy - standard loss for pass/fail problems
optimizer = optim.Adam(model.parameters(), lr=0.1)

print("Training the network...")
for epoch in range(200):
    optimizer.zero_grad()
    predictions = model(X)
    loss = criterion(predictions, y)
    loss.backward()
    optimizer.step()

    if (epoch + 1) % 50 == 0:
        print(f"Epoch {epoch + 1}, Loss: {loss.item():.4f}")

print("\nFinal predictions vs actual:")
with torch.no_grad():
    final_predictions = model(X)
    for i in range(len(X)):
        predicted_label = "Pass" if final_predictions[i].item() > 0.5 else "Fail"
        actual_label = "Pass" if y[i].item() == 1 else "Fail"
        print(f"Predicted: {predicted_label} ({final_predictions[i].item():.3f}) | Actual: {actual_label}")
