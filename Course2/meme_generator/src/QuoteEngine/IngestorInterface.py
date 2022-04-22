from abc import ABC, abstractmethod

from typing import List
from .QuoteModel import QuoteModel 


class IngestorInterface(ABC):
    """Interface class to be inherted from all ingesters classes"""
    allowed_extensions = []

    @classmethod
    def can_ingest(cls, path):
        """Check file extention"""
        ext = path.split('.')[-1]
        return ext in cls.allowed_extensions

    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        pass