"""Unicode utilities and optional NLP adapter for the proposed Hebrew kernel."""

from .hebrew_core import HebrewKernel
from .hebrew_nlp_adapter import HebrewNLPAdapter

__all__ = ["HebrewKernel", "HebrewNLPAdapter"]
