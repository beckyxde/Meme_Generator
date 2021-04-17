"""Class for the quote objects."""
class QuoteModel(object):
    """Class for the quote objects."""

    def __init__(self, body, author):
        """Initialization method."""
        self.body = body
        self.author = author

    def __repr__(self):
        """Repr returns the string when object is called."""
        if self.body.startswith("\"") and self.body.endswith("\""):
            return f'{self.body} - {self.author}'
        else:
            return f'"{self.body}" - {self.author}'