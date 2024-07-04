import json
from dataclasses import dataclass, asdict
import config
@dataclass
class Metadata:
    page_label: str
    file_name: str
    file_path: str
    file_type: str
    file_size: int
    creation_date: str
    last_modified_date: str

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
@dataclass
class Source:
    Text: str
    metadata: Metadata
    score: float


@dataclass
class QueryResponse:
    answer: str
    sources: list
    def toJSON(self):
        return json.dumps(
            self,
            default=lambda o: o.__dict__,
            sort_keys=True,
            indent=4)

def build_response(response):
    sources = []
    answer = str(response).replace('\\n', '\n')
    built_response = QueryResponse(answer, sources)
    if config.feature_flags[config.FEATURE_FLAGS_REFERENCES]:
        for node in response.source_nodes:
            text_fmt = node.node.get_content().strip().replace("\n", " ")[:1000]
            metadata = Metadata(**node.node.metadata)
            score = node.score
            sources.append(Source(text_fmt, metadata,score))
        built_response.sources = sources
    return built_response


if __name__ == "__main__":

    metadata1 = Metadata(page_label="Page 1", file_name="example.txt", file_path="/path/to/file", file_type="text/plain", file_size=1024, creation_date="2023-01-05", last_modified_date="2023-01-05")
    source1 = Source(Text="Sample text 1", metadata=metadata1, score=0.8)

    metadata2 = Metadata(page_label="Page 2", file_name="example.docx", file_path="/path/to/file", file_type="application/vnd.openxmlformats-officedocument.wordprocessingml.document", file_size=2048, creation_date="2023-01-05", last_modified_date="2023-01-05")
    source2 = Source(Text="Sample text 2", metadata=metadata2, score=0.9)

    sources = [source1, source2]
    query_response = QueryResponse(answer="This is the answer.", sources=sources)

    print(query_response.toJSON())