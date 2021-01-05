from enum import Enum

class TransferStatus(str, Enum):
    CANCELED = "canceled"
    FAILED = "failed"
    REVIEWABLE = "reviewable"
    PENDING = "pending"
    PROCESSED = "processed"

    def __str__(self) -> str:
        return str(self.value)