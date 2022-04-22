from typing import List


from .QuoteModel import QuoteModel 
from .IngestorInterface import Ingestorinterface
from .CsvIngestor import CSVIngestor 
from .PdfIngestor import PDFIngestor 
from .DocsIngestor import DocsIngestor 
from .TxtIngestor import TxtIngestor 

class Ingestor(Ingestorinterface):
    """Chcek type of file using the abstract method can_ingest the perform parser using matching format ingestor"""

    ingestors = [CSVIngestor, PDFIngestor, DocsIngestor, TxtIngestor]

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
