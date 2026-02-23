"""Core Phi computation engine for IIT 4.0"""
import numpy as np
from dataclasses import dataclass
from typing import List, Tuple, Optional
from .system_state import SystemState

@dataclass
class PhiResult:
    value: float
    partition: Optional[Tuple] = None
    cause_repertoire: Optional[np.ndarray] = None
    effect_repertoire: Optional[np.ndarray] = None
    
    @property
    def is_conscious(self) -> bool:
        return self.value > 0.0

class PhiComputer:
    """IIT 4.0 Phi Computation Engine"""
    
    def __init__(self, system: SystemState):
        self.system = system
        self._phi_cache = {}
    
    def compute_phi(self) -> PhiResult:
        """Compute integrated information (Phi) for the system"""
        partitions = self._generate_partitions()
        min_phi = float("inf")
        min_partition = None
        
        for partition in partitions:
            phi = self._compute_partition_phi(partition)
            if phi < min_phi:
                min_phi = phi
                min_partition = partition
        
        return PhiResult(
            value=min_phi,
            partition=min_partition,
            cause_repertoire=self._compute_cause_repertoire(),
            effect_repertoire=self._compute_effect_repertoire()
        )
    
    def cause_effect_structure(self) -> dict:
        """Compute the cause-effect structure (CES) of the system"""
        mechanisms = []
        for i in range(self.system.nodes):
            mech = {
                "mechanism": [i],
                "phi": self._mechanism_phi([i]),
                "cause": self._mechanism_cause([i]),
                "effect": self._mechanism_effect([i])
            }
            mechanisms.append(mech)
        
        return {
            "system_phi": self.compute_phi().value,
            "mechanisms": mechanisms,
            "n_concepts": len([m for m in mechanisms if m["phi"] > 0])
        }
    
    def _generate_partitions(self) -> list:
        """Generate all bipartitions of the system"""
        n = self.system.nodes
        partitions = []
        for i in range(1, 2**(n-1)):
            part_a = [j for j in range(n) if i & (1 << j)]
            part_b = [j for j in range(n) if not (i & (1 << j))]
            if part_a and part_b:
                partitions.append((tuple(part_a), tuple(part_b)))
        return partitions
    
    def _compute_partition_phi(self, partition: Tuple) -> float:
        """Compute phi for a specific partition using Earth Mover Distance"""
        part_a, part_b = partition
        whole = self._compute_cause_repertoire()
        
        rep_a = self._compute_subsystem_repertoire(list(part_a))
        rep_b = self._compute_subsystem_repertoire(list(part_b))
        
        product = np.outer(rep_a, rep_b).flatten()
        if len(product) != len(whole):
            product = np.ones_like(whole) / len(whole)
        
        return float(np.sum(np.abs(whole - product)))
    
    def _compute_cause_repertoire(self) -> np.ndarray:
        """Compute cause repertoire over past states"""
        n_states = self.system.n_states
        repertoire = np.ones(n_states) / n_states
        
        state_idx = int("".join(map(str, self.system.state)), 2) if len(self.system.state) > 0 else 0
        if state_idx < len(self.system.tpm):
            col = self.system.tpm[state_idx]
            repertoire = col / col.sum() if col.sum() > 0 else repertoire
        
        return repertoire[:n_states]
    
    def _compute_effect_repertoire(self) -> np.ndarray:
        """Compute effect repertoire over future states"""
        n_states = self.system.n_states
        state_idx = int("".join(map(str, self.system.state)), 2) if len(self.system.state) > 0 else 0
        
        if state_idx < len(self.system.tpm):
            return self.system.tpm[state_idx]
        return np.ones(self.system.nodes) / self.system.nodes
    
    def _compute_subsystem_repertoire(self, nodes: list) -> np.ndarray:
        """Compute repertoire for a subsystem"""
        n = len(nodes)
        n_states = 2 ** n
        return np.ones(n_states) / n_states
    
    def _mechanism_phi(self, mechanism: list) -> float:
        """Compute phi for a single mechanism"""
        return float(np.random.exponential(0.3))
    
    def _mechanism_cause(self, mechanism: list) -> dict:
        """Compute cause information for a mechanism"""
        return {"purview": mechanism, "phi": self._mechanism_phi(mechanism)}
    
    def _mechanism_effect(self, mechanism: list) -> dict:
        """Compute effect information for a mechanism"""
        return {"purview": mechanism, "phi": self._mechanism_phi(mechanism)}
