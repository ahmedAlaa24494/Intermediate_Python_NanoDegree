"""Csv reader and ingester Module."""
from typing import List
import pandas as pd
from .QuoteModel import QuoteModel
from .IngestorInterface import IngestorInterface


class CsvIngestor(IngestorInterface):
    """Read and Ingest Csv file into quote modules."""

    allowed_extensions = ['csv']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse content of csv file to return list of quotes.

        Arguments :
            path {str} : directory path where the file exist

        Returns:
            List(quotes): list of quote moduels
        """
        if not cls.can_ingest(path):
            raise Exception("File cannot be ingested")

        quotes = []
        df = pd.read_csv(path, header=0)

        for i, row in df.iterrows():

            new_quote = QuoteModel(body=row['body'], author=row['author'])
            quotes.append(new_quote)
        return quotes
