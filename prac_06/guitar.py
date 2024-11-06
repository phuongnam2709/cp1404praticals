class Guitar:
    """Represent a Guitar object."""

    def __init__(self, name="", year=0, cost=0.0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return a string representation of the guitar."""
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def get_age(self):
        """Return the age of the guitar."""
        current_year = 2024
        return current_year - self.year

    def is_vintage(self):
        """Return True/False if the guitar is vintage (50 or more years old) or not."""
        return self.get_age() >= 50
