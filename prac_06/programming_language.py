class ProgrammingLanguage:
    """Represent a Programming Language."""

    def __init__(self, name, typing, reflection, year):
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """returns True/False if the programming language is dynamically typed or not"""
        return self.typing.lower() == 'dynamic'

    def __str__(self):
        return (f"{self.name} ({self.year}), Typing: {self.typing}, Reflection: {self.reflection}, "
                f"First appeared in {self.year}")

