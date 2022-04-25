"""Txt file reader and ingester Module."""
from typing import List
from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class TxtIngestor(IngestorInterface):
    """Ingest quots from a txt file."""

    allowed_extensions = ["txt"]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse the content of txt file and return List of QuoteModel objects.

        Arguments:
            path (str): Path to file.

        """
        if not cls.can_ingest(path):
            raise Exception("cannot ingest exception")

        quotes = []

        with open(path, "r") as f:
            for line in f.readlines():
                line = line.strip("\n\r").strip()
                if len(line) > 0:
                    body, author = line.split(" - ")
                    quotes.append(QuoteModel(body, author))
        return quotes
