from typing import TypedDict, List

class AgentState(TypedDict):
    question: str
    search_results: List[dict]
    pages: List[dict]
    summary: str
    sources: List[str]
    steps: int