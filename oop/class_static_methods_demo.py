class Calculator:
    # Class attribute
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """Static method: performs addition without accessing class data."""
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """Class method: can access class attributes via 'cls'."""
        print(f"Calculation type: {cls.calculation_type}")
        return a * b
