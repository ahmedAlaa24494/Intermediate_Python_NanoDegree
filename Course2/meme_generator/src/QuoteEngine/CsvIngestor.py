from typing import List
import pandas as pd 
from .QuoteModel import QuoteModel 
from .IngestorInterface import Ingesterinterface



class CsvIngestor(Ingesterinterface):
    allowed_extensions = ['csv']

    @classmethod
    def parser(cls, path:str) -> List[QuoteModel]: 
        """Parse content of csv file to return list of quotes
        
        Arguments : 
        path {str} : directory path where the file exist
        
        """


        
        if not cls.can_ingest(path): 
            raise Exception("File cannot be ingested")

        quotes = [] 
        df = pd.read_csv(path , header=0)

        for i, row in df.iterrows()  :
            new_quote = QuoteModel(body = row['body'] , auther = row['auther'])
            quotes.append(new_quote)
        return quotes 

