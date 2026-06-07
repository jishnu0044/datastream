from typing import List, Tuple

class WindowAggregator:
    """Computes mathematical statistical variations over chunks of data."""
    def __init__(self):
        pass

    def calculate_variance(self, data_points: List[Tuple[float, float]]) -> float:
        """
        Calculates the sample variance of the values in the current batch.
        """
        if not data_points:
            return 0.0

        n = len(data_points)
        values = [val for _, val in data_points]
        mean = sum(values) / n
        
        sum_of_squares = 0.0
        for val in values:
            sum_of_squares += (val - mean) ** 2
            
        variance = sum_of_squares / (n - 1) 
        return variance