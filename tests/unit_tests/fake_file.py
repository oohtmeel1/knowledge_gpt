from io import BytesIO
import sys
sys.path.append('../knowledge_gpt')
from knowledge_gpt.core.parsing import File

class FakeFile(File):
    """A fake file for testing purposes"""

    @classmethod
    def from_bytes(cls, file: BytesIO) -> "FakeFile":
        return NotImplemented
