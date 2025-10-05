"""
Comprehensive test suite for the package sorting system.

Test Coverage:
- Standard packages (normal cases)
- Bulky packages (volume-based and dimension-based)
- Heavy packages
- Rejected packages (both bulky and heavy)
- Boundary conditions (exact threshold values)
- Edge cases (minimum valid values, large values)
- Input validation (negative, zero, non-numeric inputs)

"""

import pytest
from package_sorter import sort


class TestStandardPackages:
    """Test cases for packages that should be classified as STANDARD."""

    def test_small_light_package(self):
        """Small package well below all thresholds."""
        assert sort(10, 10, 10, 5) == "STANDARD"

    def test_just_below_all_thresholds(self):
        """Package just below both bulky and heavy thresholds."""
        assert sort(100, 100, 99, 19.99) == "STANDARD"

    def test_minimum_valid_dimensions(self):
        """Smallest possible valid package."""
        assert sort(0.1, 0.1, 0.1, 0.1) == "STANDARD"


class TestBulkyPackages:
    """Test cases for bulky packages (SPECIAL category)."""

    def test_bulky_by_volume_exactly_at_threshold(self):
        """Package with volume exactly at 1,000,000 cm³."""
        assert sort(100, 100, 100, 10) == "SPECIAL"

    def test_bulky_by_volume_above_threshold(self):
        """Package with volume above 1,000,000 cm³."""
        assert sort(101, 100, 100, 10) == "SPECIAL"

    def test_bulky_by_width_exactly_at_threshold(self):
        """Package with width exactly at 150 cm."""
        assert sort(150, 50, 50, 10) == "SPECIAL"

    def test_bulky_by_height_exactly_at_threshold(self):
        """Package with height exactly at 150 cm."""
        assert sort(50, 150, 50, 10) == "SPECIAL"

    def test_bulky_by_length_exactly_at_threshold(self):
        """Package with length exactly at 150 cm."""
        assert sort(50, 50, 150, 10) == "SPECIAL"

    def test_bulky_by_dimension_above_threshold(self):
        """Package with one dimension significantly above 150 cm."""
        assert sort(200, 50, 50, 10) == "SPECIAL"

    def test_just_below_bulky_thresholds(self):
        """Package just below bulky thresholds should be STANDARD."""
        assert sort(149, 50, 50, 10) == "STANDARD"

    def test_volume_just_below_threshold(self):
        """Package with volume just below 1,000,000 cm³."""
        assert sort(99, 100, 100, 10) == "STANDARD"


class TestHeavyPackages:
    """Test cases for heavy packages (SPECIAL category)."""

    def test_heavy_exactly_at_threshold(self):
        """Package with mass exactly at 20 kg."""
        assert sort(50, 50, 50, 20) == "SPECIAL"

    def test_heavy_above_threshold(self):
        """Package with mass above 20 kg."""
        assert sort(50, 50, 50, 25) == "SPECIAL"

    def test_very_heavy(self):
        """Extremely heavy package."""
        assert sort(10, 10, 10, 100) == "SPECIAL"

    def test_just_below_heavy_threshold(self):
        """Package just below heavy threshold should be STANDARD."""
        assert sort(50, 50, 50, 19.99) == "STANDARD"


class TestRejectedPackages:
    """Test cases for packages that are both bulky and heavy (REJECTED)."""

    def test_bulky_by_volume_and_heavy(self):
        """Package that is bulky by volume and heavy."""
        assert sort(100, 100, 100, 20) == "REJECTED"

    def test_bulky_by_dimension_and_heavy(self):
        """Package that is bulky by dimension and heavy."""
        assert sort(150, 50, 50, 25) == "REJECTED"

    def test_extremely_bulky_and_heavy(self):
        """Package that exceeds both thresholds significantly."""
        assert sort(200, 200, 200, 50) == "REJECTED"

    def test_all_dimensions_at_threshold_and_heavy(self):
        """Package with all dimensions at threshold and heavy."""
        assert sort(150, 150, 150, 20) == "REJECTED"


class TestBoundaryConditions:
    """Test exact boundary values to ensure >= comparisons work correctly."""

    def test_volume_boundary_999999(self):
        """Volume of 999,999 cm³ should not be bulky."""
        # 99.9 * 100 * 100.01 ≈ 999,999
        assert sort(99.9, 100, 100.01, 15) == "STANDARD"

    def test_volume_boundary_1000000(self):
        """Volume of exactly 1,000,000 cm³ should be bulky."""
        assert sort(100, 100, 100, 15) == "SPECIAL"

    def test_dimension_boundary_149_99(self):
        """Dimension of 149.99 cm should not be bulky."""
        assert sort(149.99, 10, 10, 15) == "STANDARD"

    def test_dimension_boundary_150(self):
        """Dimension of exactly 150 cm should be bulky."""
        assert sort(150, 10, 10, 15) == "SPECIAL"

    def test_mass_boundary_19_99(self):
        """Mass of 19.99 kg should not be heavy."""
        assert sort(10, 10, 10, 19.99) == "STANDARD"

    def test_mass_boundary_20(self):
        """Mass of exactly 20 kg should be heavy."""
        assert sort(10, 10, 10, 20) == "SPECIAL"


class TestInputValidation:
    """Test input validation and error handling."""

    def test_negative_width(self):
        """Negative width should raise ValueError."""
        with pytest.raises(ValueError, match="width must be positive"):
            sort(-10, 50, 50, 10)

    def test_negative_height(self):
        """Negative height should raise ValueError."""
        with pytest.raises(ValueError, match="height must be positive"):
            sort(50, -10, 50, 10)

    def test_negative_length(self):
        """Negative length should raise ValueError."""
        with pytest.raises(ValueError, match="length must be positive"):
            sort(50, 50, -10, 10)

    def test_negative_mass(self):
        """Negative mass should raise ValueError."""
        with pytest.raises(ValueError, match="mass must be positive"):
            sort(50, 50, 50, -10)

    def test_zero_width(self):
        """Zero width should raise ValueError."""
        with pytest.raises(ValueError, match="width must be positive"):
            sort(0, 50, 50, 10)

    def test_zero_mass(self):
        """Zero mass should raise ValueError."""
        with pytest.raises(ValueError, match="mass must be positive"):
            sort(50, 50, 50, 0)

    def test_non_numeric_width(self):
        """Non-numeric width should raise TypeError."""
        with pytest.raises(TypeError, match="width must be a number"):
            sort("100", 50, 50, 10)

    def test_non_numeric_mass(self):
        """Non-numeric mass should raise TypeError."""
        with pytest.raises(TypeError, match="mass must be a number"):
            sort(50, 50, 50, "20")

    def test_none_input(self):
        """None input should raise TypeError."""
        with pytest.raises(TypeError, match="must be a number"):
            sort(None, 50, 50, 10)


class TestRealWorldScenarios:
    """Test realistic package scenarios."""

    def test_small_electronics_package(self):
        """Typical small electronics package."""
        assert sort(30, 20, 40, 2) == "STANDARD"

    def test_laptop_box(self):
        """Standard laptop shipping box."""
        assert sort(45, 35, 8, 3.5) == "STANDARD"

    def test_large_tv_light(self):
        """Large TV (bulky by dimension but light)."""
        assert sort(160, 90, 15, 18) == "SPECIAL"

    def test_industrial_machinery_part(self):
        """Heavy industrial part (heavy but not bulky)."""
        assert sort(40, 30, 30, 45) == "SPECIAL"

    def test_furniture_shipment(self):
        """Large furniture item (both bulky and heavy)."""
        assert sort(180, 120, 90, 35) == "REJECTED"

    def test_pallet_of_books(self):
        """Pallet of books (bulky by volume and heavy)."""
        assert sort(120, 100, 85, 250) == "REJECTED"


class TestFloatingPointPrecision:
    """Test handling of floating point numbers."""

    def test_fractional_dimensions(self):
        """Package with fractional dimensions."""
        assert sort(50.5, 50.5, 50.5, 15.5) == "STANDARD"

    def test_very_small_fractions(self):
        """Package with very small fractional values."""
        assert sort(149.9999, 10, 10, 19.9999) == "STANDARD"

    def test_scientific_notation(self):
        """Package dimensions using scientific notation."""
        assert sort(1.5e2, 50, 50, 2e1) == "REJECTED"


if __name__ == "__main__":
    # Run tests with verbose output
    pytest.main([__file__, "-v", "--tb=short"])
