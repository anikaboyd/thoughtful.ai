def sort(width, height, length, mass):
    """
    Sort packages based on size and weight.
    Returns: STANDARD, SPECIAL, or REJECTED
    """
    # Validate inputs
    _validate_inputs(width, height, length, mass)

    is_bulky = _is_bulky(width, height, length)
    is_heavy = _is_heavy(mass)

    # Both bulky and heavy means rejected
    if is_bulky and is_heavy:
        return "REJECTED"
    # Either bulky or heavy needs special handling
    elif is_bulky or is_heavy:
        return "SPECIAL"
    # Normal package
    else:
        return "STANDARD"


def _validate_inputs(width, height, length, mass):
    """Validate that inputs are valid numbers"""
    params = [
        ("width", width),
        ("height", height),
        ("length", length),
        ("mass", mass)
    ]

    for name, value in params:
        if not isinstance(value, (int, float)):
            raise TypeError(f"{name} must be a number")
        if value <= 0:
            raise ValueError(f"{name} must be positive")


def _is_bulky(width, height, length):
    """Check if package is bulky by volume or dimension"""
    volume = width * height * length
    # Bulky if volume >= 1 million cm³ or any dimension >= 150 cm
    if volume >= 1_000_000:
        return True
    if max(width, height, length) >= 150:
        return True
    return False


def _is_heavy(mass):
    """Check if package is heavy (>= 20 kg)"""
    if mass >= 20:
        return True
    return False
