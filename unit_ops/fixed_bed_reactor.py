import numpy as np
import numpy.typing as npt

class FixedBedReactor:
    def __init__(self , bed_data: npt.NDArray[np.float64]):
        self.bed_data = bed_data

    @property
    def bed_data(self):
        return self._bed_data

    @bed_data.setter
    def bed_data(self, value: npt.NDArray[np.float64]) -> None:
        C = np.asanyarray(value, np.float64)
        if C.ndim != 2 or C.shape[1] != 4:
            raise ValueError(f"Expected (N, 4), got {C.shape}.")
        self._bed_data = np.ascontiguousarray(C)

    def max_temperature(self) -> float:
        T = self._bed_data[:, 1]
        return float(np.max(T))

    def get_depleted_zones(self, concentration_threshold: float) -> npt.NDArray[np.float64]:
        C_A = self._bed_data[:, 2]
        mask = concentration_threshold > C_A
        return self._bed_data[mask][:, [0, 1]]
