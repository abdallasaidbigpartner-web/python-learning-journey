"""
Professionalization pass: automated test for Lesson 27's PyTorch
neural network.

Verifies the network actually learns the pass/fail pattern (loss
decreases, final predictions match expected labels) rather than just
"the script ran." Runs via GitHub Actions cloud CI since PyTorch
cannot build on Termux/Android.
"""

import torch
import torch.nn as nn
import torch.optim as optim
from lesson27_neural_network import SimpleNet


def test_network_learns_and_predicts_correctly():
    X = torch.tensor([
        [0.1, 0.4], [0.2, 0.45], [0.3, 0.55], [0.4, 0.6],
        [0.5, 0.7], [0.6, 0.75], [0.7, 0.85], [0.8, 0.9]
    ], dtype=torch.float32)
    y = torch.tensor([[0], [0], [0], [1], [1], [1], [1], [1]], dtype=torch.float32)

    model = SimpleNet()
    criterion = nn.BCELoss()
    optimizer = optim.Adam(model.parameters(), lr=0.1)

    initial_loss = None
    final_loss = None

    for epoch in range(200):
        optimizer.zero_grad()
        predictions = model(X)
        loss = criterion(predictions, y)
        loss.backward()
        optimizer.step()

        if epoch == 0:
            initial_loss = loss.item()
        final_loss = loss.item()

    assert final_loss < initial_loss, "Loss should decrease after training"

    with torch.no_grad():
        final_predictions = model(X)
        predicted_labels = (final_predictions > 0.5).float()
        accuracy = (predicted_labels == y).float().mean().item()

    assert accuracy >= 0.75, f"Expected at least 75% accuracy, got {accuracy}"
