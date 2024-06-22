from .google_translator import GoogleTranslator
from .parameters import Parameters
from .resolution_solver import ResolutionSolver



NODE_CLASS_MAPPINGS = {
    "GoogleTranslator": GoogleTranslator,
    "Parameters": Parameters,
    "ResolutionSolver": ResolutionSolver
}

__all__ = ['NODE_CLASS_MAPPINGS']

