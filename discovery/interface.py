from dataclasses import dataclass
@dataclass
class Candidate:
    url:str; title:str; creator:str; source_name:str
    license_name:str="UNKNOWN"; license_url:str=""; attribution:str=""; notes:str=""
class SourceAdapter:
    """Implement API-compliant adapters; never bypass access controls."""
    def search(self, query, limit=10): raise NotImplementedError
