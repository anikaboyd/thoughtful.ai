# Package Sorting System

A Python-based package classification system for Thoughtful AI's robotic automation factory. This system automatically sorts packages into appropriate handling categories based on their physical dimensions and mass.

## Quick Start

### Prerequisites
- Python 3.7 or higher
- pytest (for running tests)

### Installation

```bash
# Clone or download this repository
cd thoughtful.ai

# Install pytest if not already installed
pip install pytest
```

### Running the Code

**Basic Usage:**

```python
from package_sorter import sort

# Standard package
result = sort(50, 50, 50, 10)
print(result)  # Output: STANDARD

# Bulky package (dimension >= 150 cm)
result = sort(150, 50, 50, 15)
print(result)  # Output: SPECIAL

# Heavy package (mass >= 20 kg)
result = sort(50, 50, 50, 25)
print(result)  # Output: SPECIAL

# Rejected package (both bulky and heavy)
result = sort(150, 100, 100, 25)
print(result)  # Output: REJECTED
```

**Running Tests:**

```bash
# Run all tests with verbose output
pytest test_package_sorter.py -v

# Run with coverage report
pytest test_package_sorter.py -v --cov=package_sorter --cov-report=term-missing

# Run specific test class
pytest test_package_sorter.py::TestBoundaryConditions -v
```

## Classification Rules

### Package Categories

1. **STANDARD**: Normal packages that can be handled automatically
   - Not bulky AND not heavy

2. **SPECIAL**: Packages requiring special handling
   - Either bulky OR heavy (but not both)

3. **REJECTED**: Packages that cannot be processed
   - Both bulky AND heavy

### Bulky Criteria

A package is considered **bulky** if it meets ANY of these conditions:
- Volume (Width × Height × Length) ≥ 1,000,000 cm³
- Any single dimension ≥ 150 cm

### Heavy Criteria

A package is considered **heavy** if:
- Mass ≥ 20 kg

## Design Decisions

### 1. Input Validation
**Decision**: Validate all inputs before processing.

**Rationale**:
- Prevents invalid data from causing issues
- Provides clear error messages
- Makes debugging easier

### 2. Helper Functions
**Decision**: Split logic into `_validate_inputs`, `_is_bulky`, and `_is_heavy` functions.

**Rationale**:
- Each function has one clear job
- Makes code easier to read and test
- Separates concerns properly

### 3. Simple Control Flow
**Decision**: Use straightforward if-elif-else statements throughout.

**Rationale**:
- Clear and easy to follow
- No complex nested logic
- Easy to maintain

### 4. Comprehensive Test Coverage
**Decision**: Create 40+ test cases covering multiple scenarios.

**Test Categories**:
- **Standard packages**: Normal cases and boundary conditions
- **Bulky packages**: Both volume-based and dimension-based
- **Heavy packages**: Exact thresholds and above
- **Rejected packages**: All combinations of bulky + heavy
- **Boundary conditions**: Testing >= operators with exact threshold values
- **Input validation**: Negative, zero, and non-numeric inputs
- **Real-world scenarios**: Practical package types
- **Floating-point precision**: Fractional values and scientific notation

**Rationale**:
- Ensures correctness at boundary values (critical for >= comparisons)
- Catches edge cases that could cause production issues
- Provides regression testing for future changes
- Demonstrates thorough understanding of requirements

## Test Results

The test suite includes 40+ test cases covering:
- All classification categories (STANDARD, SPECIAL, REJECTED)
- Exact threshold boundaries (149.99 vs 150, 19.99 vs 20, etc.)
- Volume and dimension-based bulky detection
- Input validation and error handling
- Real-world package scenarios
- Floating-point precision handling

## Code Quality Features

1. **Input Validation**: Proper error handling for invalid inputs
2. **Clean Code**: Follows PEP 8 style guidelines
3. **DRY Principle**: No code duplication
4. **Testability**: All functions are easily testable
5. **Clear Comments**: Key logic is documented

## Function Signature

```python
def sort(width: float, height: float, length: float, mass: float) -> str
```

**Parameters**:
- `width` (float): Package width in centimeters
- `height` (float): Package height in centimeters
- `length` (float): Package length in centimeters
- `mass` (float): Package mass in kilograms

**Returns**:
- `str`: One of "STANDARD", "SPECIAL", or "REJECTED"

**Raises**:
- `TypeError`: If any input is not a number
- `ValueError`: If any input is zero or negative

## Example Scenarios

### Real-World Package Types

```python
# Small electronics package (30cm × 20cm × 40cm, 2kg)
sort(30, 20, 40, 2)  # STANDARD

# Laptop shipping box (45cm × 35cm × 8cm, 3.5kg)
sort(45, 35, 8, 3.5)  # STANDARD

# Large TV (160cm × 90cm × 15cm, 18kg) - bulky by dimension
sort(160, 90, 15, 18)  # SPECIAL

# Industrial machinery part (40cm × 30cm × 30cm, 45kg) - heavy
sort(40, 30, 30, 45)  # SPECIAL

# Furniture shipment (180cm × 120cm × 90cm, 35kg) - both
sort(180, 120, 90, 35)  # REJECTED
```

## Time Complexity

All operations run in O(1) constant time, suitable for high-throughput robotic systems.

## Future Enhancements

Potential improvements for production use:
1. Add logging for audit trails
2. Implement metrics collection for package statistics
3. Add configuration file for threshold values
4. Create API endpoint for integration with robotic systems
5. Add support for different unit systems (inches, pounds)
6. Implement batch processing for multiple packages



**Made with love by Anika Boyd**