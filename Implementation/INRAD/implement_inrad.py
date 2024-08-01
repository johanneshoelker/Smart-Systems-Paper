import torch
import torch.nn as nn

# model design
class INRADModel(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super(INRADModel, self).__init__()
        self.fc1 = nn.Linear(input_size, hidden_size)
        self.relu = nn.ReLU()
        self.fc2 = nn.Linear(hidden_size, output_size)

    def forward(self, x):
        out = self.fc1(x)
        out = self.relu(out)
        out = self.fc2(out)
        return out

model = INRADModel(input_size=1, hidden_size=50, output_size=1)

# Training
criterion = nn.MSELoss()
optimizer = torch.optim.Adam(model.parameters(), lr=0.001)

for epoch in range(num_epochs):
    for time, value in train_loader:
        time = time.view(-1, 1).float()
        value = value.view(-1, 1).float()

        # Forward pass
        output = model(time)
        loss = criterion(output, value)

        # Backward pass and optimization
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

# Anomaly detection
anomaly_scores = []
with torch.no_grad():
    for time, value in test_loader:
        time = time.view(-1, 1).float()
        value = value.view(-1, 1).float()
        output = model(time)
        error = criterion(output, value)
        anomaly_scores.append(error.item())
