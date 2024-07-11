from flask import Flask, request, Response, stream_with_context
from router.query_router import setup_query_engines
from server import response_payload
import config
import logging

logging.basicConfig(level=logging.INFO)

import json

app = Flask(__name__)
app.config['preprocessed_data'] = None


def preprocessing():
    print("Preprocessing data...")  # Perform preprocessing tasks
    _consolidated_engine = setup_query_engines()
    app.config['preprocessed_data'] = {  # Store the preprocessed data in the app's config
        'consolidated_engine': _consolidated_engine
    }
    print("Preprocessing complete.")


with app.app_context():  # Run preprocessing when the application context is initialized
    preprocessing()


def generic_handle_data(engine_name: str):
    if request.is_json:
        generic_engine = app.config['preprocessed_data'][engine_name]  # Access preprocessed data
        # api_request = build_query(request.get_json().get('context'), request.get_json().get('prompt'))
        logging.info(str(request))
        api_request = request.get_json().get('prompt')[0].get('content')
        logging.info("received: " + str(api_request))
        response = generic_engine.query(api_request)
        # for node in response.source_nodes:
        #     print(f"Node ID: {str(node.node)}, Metadata: {node.node.metadata}")

        ## ask if json needed
        # return response_payload.build_response(response).toJSON(), 200
        try:
            for chunk in response.response_gen:
                yield chunk
        except Exception as e:
            logging.error(e)
    else:
        return 'Request must be JSON.', 400


@app.route('/api/consolidated_engine', methods=['POST'])
def consolidated_engine():
    # return generic_handle_data('consolidated_engine')
    return Response(stream_with_context(generic_handle_data('consolidated_engine')), mimetype='text/plain')


@app.route('/')
def home():
    return "API controller app\n"


def build_query(context, prompt):  # Temp, for now just adds context and prompt
    return context + prompt


def run_server():
    app.run(debug=config.server[config.DEBUG], port=config.server[config.PORT],
            host=config.server[config.DEFAULT_LLM_HOST], use_reloader=False)

# if __name__ == '__main__':
# run_server()
