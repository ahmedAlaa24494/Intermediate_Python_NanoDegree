from typing import List
import docx

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class DocxIngestor(IngestorInterface):
    """Ingests quotes from docx file"""

    allowed_extensions = ["docx"]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse the content of docs file to list of QuoteModel objects.

        Arguments:
            path (str): Path to file.
        """

        if not cls.can_ingest(path):
            raise Exception("cannot ingest exception")

        quotes = []
        doc = docx.Document(path)

        for line in doc.paragraphs:
            if line.text != "":
                body, author = line.text.split(" - ")
                
                quotes.append(QuoteModel(body, author))

        return quotes