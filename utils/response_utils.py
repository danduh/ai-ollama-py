import config
from server import response_payload


# use this on a query engine query result to enrich it with references

def enrich_response(response):
    output = []
    if not config.feature_flags[config.FEATURE_FLAGS_STREAMING]:
        output.append(str(response))
    if config.feature_flags[config.FEATURE_FLAGS_REFERENCES]:
        for node in response.source_nodes:
            output.append(config.printers[config.PRINTERS_PROMPT_SEPARATOR])
            text_fmt = node.node.get_content().strip().replace("\n", " ")[:1000]
            output.append(f"Text:\t {text_fmt} ...")
            output.append(f"Metadata:\t {node.node.metadata}")
            output.append(f"Score:\t {node.score:.3f}")
    output.append(config.printers[config.PRINTERS_PROMPT_END])
    return "\n".join(output)

