#!/usr/bin/env python3
"""

The script below demonstrates example usage of the sorting function for one of thoughtful.ai's robotic arms.

"""

from package_sorter import sort


def print_classification(width, height, length, mass, description=""):
    """Print package classification with formatted output."""
    result = sort(width, height, length, mass)
    volume = width * height * length

    print(f"\n{'='*70}")
    if description:
        print(f"Scenario: {description}")
    print(f"Dimensions: {width} × {height} × {length} cm")
    print(f"Volume: {volume:,.0f} cm³")
    print(f"Mass: {mass} kg")
    print(f"Classification: {result}")
    print(f"{'='*70}")


def main():
    """Run example classifications."""

    print("\n" + "="*70)
    print("PACKAGE SORTING SYSTEM - EXAMPLE USAGE")
    print("="*70)

    # STANDARD packages
    print("\n\n### STANDARD PACKAGES ###")

    print_classification(
        30, 20, 40, 2,
        "Small electronics package"
    )

    print_classification(
        45, 35, 8, 3.5,
        "Laptop shipping box"
    )

    print_classification(
        100, 100, 99, 19.99,
        "Just below all thresholds"
    )

    # SPECIAL packages (bulky)
    print("\n\n### SPECIAL PACKAGES (BULKY) ###")

    print_classification(
        100, 100, 100, 15,
        "Bulky by volume (exactly 1,000,000 cm³)"
    )

    print_classification(
        150, 50, 50, 15,
        "Bulky by width (150 cm dimension)"
    )

    print_classification(
        160, 90, 15, 18,
        "Large TV - bulky by dimension"
    )

    print_classification(
        120, 100, 85, 15,
        "Large box - bulky by volume"
    )

    # SPECIAL packages (heavy)
    print("\n\n### SPECIAL PACKAGES (HEAVY) ###")

    print_classification(
        50, 50, 50, 20,
        "Heavy at exact threshold (20 kg)"
    )

    print_classification(
        40, 30, 30, 45,
        "Industrial machinery part"
    )

    print_classification(
        30, 30, 30, 100,
        "Very heavy small package"
    )

    # REJECTED packages
    print("\n\n### REJECTED PACKAGES (BULKY AND HEAVY) ###")

    print_classification(
        100, 100, 100, 20,
        "Bulky by volume AND heavy"
    )

    print_classification(
        150, 50, 50, 25,
        "Bulky by dimension AND heavy"
    )

    print_classification(
        180, 120, 90, 35,
        "Large furniture shipment"
    )

    print_classification(
        200, 200, 200, 50,
        "Extremely bulky and heavy"
    )

    # Boundary conditions
    print("\n\n### BOUNDARY CONDITIONS ###")

    print_classification(
        149.99, 10, 10, 15,
        "Just below dimension threshold"
    )

    print_classification(
        150, 10, 10, 15,
        "Exactly at dimension threshold"
    )

    print_classification(
        10, 10, 10, 19.99,
        "Just below mass threshold"
    )

    print_classification(
        10, 10, 10, 20,
        "Exactly at mass threshold"
    )

    # Error handling examples
    print("\n\n### ERROR HANDLING EXAMPLES ###")

    print("\nAttempting to classify package with negative dimension...")
    try:
        sort(-10, 50, 50, 10)
    except ValueError as e:
        print(f"Caught ValueError: {e}")

    print("\nAttempting to classify package with zero mass...")
    try:
        sort(50, 50, 50, 0)
    except ValueError as e:
        print(f"Caught ValueError: {e}")

    print("\nAttempting to classify package with non-numeric input...")
    try:
        sort("100", 50, 50, 10)
    except TypeError as e:
        print(f"Caught TypeError: {e}")

    # Summary
    print("\n\n" + "="*70)
    print("SUMMARY")
    print("="*70)
    print("\nClassification Rules:")
    print("  • STANDARD: Not bulky and not heavy")
    print("  • SPECIAL:  Either bulky or heavy (but not both)")
    print("  • REJECTED: Both bulky and heavy")
    print("\nBulky Criteria:")
    print("  • Volume ≥ 1,000,000 cm³, OR")
    print("  • Any dimension ≥ 150 cm")
    print("\nHeavy Criteria:")
    print("  • Mass ≥ 20 kg")
    print("="*70 + "\n")


if __name__ == "__main__":
    main()
