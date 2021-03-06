import torch
import torch.nn as nn
class QNetwork(nn.Module):
    """Actor (Policy) Model."""

    def __init__(self, state_size, action_size, seed, fc1=32, fc2=64, fc3=64):
        """Initialize parameters and build model.
        Params
        ======
            state_size (int): Dimension of each state
            action_size (int): Dimension of each action
            seed (int): Random seed
        """
        super(QNetwork, self).__init__()
        self.seed = torch.manual_seed(seed)
        
        #"*** YOUR CODE HERE ***"
        self.fc1 = nn.Linear(state_size, fc1)
        self.relu1 = nn.ReLU()
        self.fc2 = nn.Linear(fc1, fc2)
        self.relu2 = nn.ReLU()
        self.fc3 = nn.Linear(fc2, action_size)

    def forward(self, state):
        """Build a network that maps state -> action values."""
        state = self.fc1(state)
        state = self.relu1(state)
        state = self.fc2(state)
        state = self.relu2(state)
        state = self.fc3(state)

        return state
