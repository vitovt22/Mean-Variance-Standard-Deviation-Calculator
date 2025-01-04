
# Calculation of Statistics for a 3x3 Matrix 

This script computes statistical measures for a given list of 9 numerical values, reshaped into a 3x3 matrix using NumPy. The calculated statistics include mean, variance, standard deviation, maximum, minimum, and sum for each row, column, and the entire matrix.
## Installation

Install the required package using pip:

```bash
  pip install numpy
```
    
## Usage/Examples
The input must be a list of exactly 9 numerical values.
If the list contains more or fewer values, an error is raised.

Call the ```calculate(lst)``` function, passing the list of 9 numbers as an argument.
Example:



```python
from your_script_name import calculate

lst = [0, 1, 2, 3, 4, 5, 6, 7, 8]
result = calculate(lst)
print(result)
```


## Output

The function returns a dictionary containing the following statistical measures for the 3x3 matrix:

- Mean: Averages of each column, each row, and the entire matrix.
- Variance: Variance of each column, each row, and the entire matrix.
- Standard Deviation: Standard deviation of each column, each row, and the entire matrix.
- Max: Maximum values in each column, each row, and the entire matrix.
- Min: Minimum values in each column, each row, and the entire matrix.
- Sum: Sums of each column, each row, and the entire matrix.


# Example Output:
For the input list ```[0, 1, 2, 3, 4, 5, 6, 7, 8]```, the output will be:

```
{
    'mean': [[3.0, 4.0, 5.0], [1.0, 4.0, 7.0], 4.0],
    'variance': [[6.0, 6.0, 6.0], [0.6666666666666666, 0.6666666666666666, 0.6666666666666666], 6.666666666666667],
    'standard deviation': [[2.449489742783178, 2.449489742783178, 2.449489742783178], [0.816496580927726, 0.816496580927726, 0.816496580927726], 2.581988897471611],
    'max': [[6, 7, 8], [2, 5, 8], 8],
    'min': [[0, 1, 2], [0, 3, 6], 0],
    'sum': [[9, 12, 15], [3, 12, 21], 36]
}
```
## License

[MIT](https://choosealicense.com/licenses/mit/)

