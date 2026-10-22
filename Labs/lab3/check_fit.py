"""The two examples in fit_zipf's docstring: run after every change."""
import numpy as np
from Lab3_StarterCode import fit_zipf

m, C = fit_zipf(np.array([600, 300, 200, 150]), 1, 4)
print("example 1:", round(m, 6), round(C, 6), "   want: -1.0 600.0")
m, C = fit_zipf(np.array([5000, 900, 400, 1]), 2, 3)
print("example 2:", round(m, 6), round(C, 6), "   want: -2.0 3600.0")
