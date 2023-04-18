# In Python muss für Enums ein spezielles Module geladen werden
from enum import Enum

class Cupsize(Enum):
    # Alle Aufzählungen in Enums sind Konstante - Werte sind Unique
    SMALL = 0.33
    MEDIUM = 0.50
    LARGE = 0.75
    GIANT = 1.00