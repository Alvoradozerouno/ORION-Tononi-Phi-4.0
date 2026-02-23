"""System state representation for IIT 4.0"""
import numpy as np
from dataclasses import dataclass, field
from typing import Optional

@dataclass
class SystemState:
    nodes: int
    connections: str = "fully_connected"
    state: Optional[np.ndarray] = None
    tpm: Optional[np.ndarray] = None
    
    def __post_init__(self):
        if self.state is None:
            self.state = np.zeros(self.nodes, dtype=int)
        if self.tpm is None:
            self.tpm = self._generate_tpm()
    
    def _generate_tpm(self) -> np.ndarray:
        n_states = 2 ** self.nodes
        tpm = np.random.rand(n_states, self.nodes)
        tpm = tpm / tpm.sum(axis=1, keepdims=True)
        return tpm
    
    def set_state(self, state: list):
        self.state = np.array(state, dtype=int)
        return self
    
    @property
    def n_states(self) -> int:
        return 2 ** self.nodes
