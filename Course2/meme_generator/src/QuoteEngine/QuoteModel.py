
class QuoteModel:
    """Encapsulate body and author of a given quote."""

    def __init__(self, body, author):
        """class object instantiation
        Arguments:
            body {str} ->  Body of the quote
            author {str}-> Author of the quote
        """
        self.body = body
        self.author = author
    def __repr__(self):
        """Representation of the QuoteModel instance in a more readable format.

        Returns:
            str: QuoteModel instance representation.
        """
        return f"QuoteModel \n (body = {self.body}, author = {self.author}) "