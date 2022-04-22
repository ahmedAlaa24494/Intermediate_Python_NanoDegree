from typing import List


from .QuoteModel import QuoteModel 
from .IngestorInterface import IngestorInterface
from .CsvIngestor import CsvIngestor 
from .PdfIngestor import PdfIngestor 
from .DocxIngestor import DocxIngestor 
from .TxtIngestor import TxtIngestor 

class Ingestor(IngestorInterface):
    """Chcek type of file using the abstract method can_ingest the perform parser using matching format ingestor"""

    ingestors = [CsvIngestor, PdfIngestor, DocxIngestor, TxtIngestor]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse file with it's matching ingestor.

        Arguments:
            path (str): Path to file.

        Returns:
            List[QuoteModel]: List of QuoteModel objects.
        """
        for ingestor in cls.ingestors:
            if ingestor.can_ingest(path):
                return ingestor.parse(path)
