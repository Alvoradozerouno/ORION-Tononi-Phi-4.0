"""IIT 4.0 Integration Postulate"""
import numpy as np
from .phi_computation import PhiComputer, PhiResult
from .system_state import SystemState

class IntegrationAnalyzer:
    """Analyze system integration (irreducibility)"""
    
    def __init__(self, system: SystemState):
        self.system = system
        self.computer = PhiComputer(system)
    
    def analyze(self) -> dict:
        """Full integration analysis"""
        phi_result = self.computer.compute_phi()
        
        return {
            "phi": phi_result.value,
            "is_integrated": phi_result.value > 0,
            "is_conscious": phi_result.is_conscious,
            "minimum_partition": phi_result.partition,
            "interpretation": self._interpret(phi_result)
        }
    
    def _interpret(self, result: PhiResult) -> str:
        if result.value == 0:
            return "System is fully reducible — no consciousness"
        elif result.value < 0.5:
            return "Minimal integration — proto-consciousness possible"
        elif result.value < 2.0:
            return "Moderate integration — emerging consciousness"
        else:
            return "High integration — strong consciousness indicator"
