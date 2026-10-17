# Vectorized Unit Operations Suite (Python / NumPy OOP)

An engineering-grade, high-performance Python package modeling chemical process unit operations using **Vectorized Object-Oriented Programming (OOP)** and raw memory management via **NumPy**.

## 🚀 Key Architectural Highlights
- **Zero-Loop Computation:** Strict avoidance of Python `for` loops in numerical pipelines using vectorized masking and NumPy broadcasting.
- **Memory Contiguity Assurance:** Automated normalization to contiguous C-order memory layout (`np.ascontiguousarray`) for SIMD and cache locality.
- **Strict Data Integrity:** Fully enforced type annotations (`numpy.typing`), runtime shape assertions, and protective getter/setter properties.

## 📦 Implemented Process Units
1. **`FixedBedReactor`**: Axial multi-sensor catalytic reactor monitoring Hot Spots and finding concentration-depleted zones.
2. **`DistillationColumn`**: Tray-by-tray data vector processing for light component fraction and thermal profile indexing.
3. **`HeatExchangerTubes`**: Multi-tube hydraulic and thermal network analyzer identifying fouled tube coordinates.
4. **`ReactorMesh2D`**: 2D discrete cell mesh evaluation for spatial temperature field gradients.

## 🛠️ Quickstart
```bash
git clone https://github.com/<YOUR_USERNAME>/chemeng-vectorized-unit-ops.git
cd chemeng-vectorized-unit-ops
pip install -r requirements.txt
```
## Example Usage:
```
import numpy as np
from unit_ops import FixedBedReactor

# Data columns: [z (m), T (K), C_A (kmol/m^3), velocity (m/s)]
data = np.array([
[2.0, 120.0, 12.0, 34.0],
[2.5, 298.9, 22.0, 129.8],
[4.0, 187.89, 10.8, 46.98],
], dtype=np.float64)

reactor = FixedBedReactor(data)

print("Peak Hot-Spot Temp (K):", reactor.max_temperature())
print("Depleted Zones (z, T):", reactor.get_depleted_zones(conc_threshold=11.5))

