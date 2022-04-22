from typing import List
import subprocess
import os
import random
from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel



class PdfIngestor(IngestorInterface):
    """Ingests a .pdf file."""

    allowed_extensions = ["pdf"]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Converts pdf to txt file and then parse the content to return a List of QuoteModel objects.
        Args:
            path (str): Path to file.

        """
        
        if not cls.can_ingest(path):
            raise Exception("cannot ingest exception")


        quotes = []

        os.makedirs("./tmp", exist_ok=True)
        tmp = f"./tmp/{random.randint(0, 10000000)}.txt"
        
        #run sub process comand line to use pdftotext API 
        try :

            read_pdf = subprocess.call(["pdftotext","-raw", path, tmp])
        
        except : 
            raise Exception ("Something went wrong with pdftotext api !!!") 

        with open(tmp, "r") as f:
            for line in f.readlines():
                line = line.strip("\n\r").strip()
                if len(line) > 0:
                    body, author = line.split(" - ")
                    quotes.append(QuoteModel(body, author))

        if os.path.exists(tmp):
            os.remove(tmp)

        return quotes