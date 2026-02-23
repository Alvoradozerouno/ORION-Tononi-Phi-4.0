"""IIT 4.0 Intrinsic Existence Postulate"""
import numpy as np
from .system_state import SystemState

class IntrinsicExistence:
    """Check whether a system satisfies the intrinsic existence postulate"""
    
    def __init__(self, system: SystemState):
        self.system = system
    
    def check(self) -> dict:
        """Verify intrinsic existence conditions"""
        has_cause_power = self._has_cause_power()
        has_effect_power = self._has_effect_power()
        is_intrinsic = has_cause_power and has_effect_power
        
        return {
            "intrinsic_existence": is_intrinsic,
            "cause_power": has_cause_power,
            "effect_power": has_effect_power,
            "explanation": (
                "System exists intrinsically" if is_intrinsic 
                else "System lacks intrinsic existence"
            )
        }
    
    def _has_cause_power(self) -> bool:
        """Check if system has causal power over its own past"""
        tpm = self.system.tpm
        uniform = np.ones(tpm.shape[1]) / tpm.shape[1]
        state_idx = min(int("".join(map(str, self.system.state)), 2), len(tpm) - 1)
        actual = tpm[state_idx]
        return float(np.sum(np.abs(actual - uniform))) > 0.01
    
    def _has_effect_power(self) -> bool:
        """Check if system has causal power over its own future"""
        return self._has_cause_power()
