from flask import Flask, request
from router.query_router import setup_query_engines
from utils import response_utils
import config

app = Flask(__name__)
app.config['preprocessed_data'] = None


def preprocessing():
    print("Preprocessing data...")  # Perform preprocessing tasks
    _arc_engine, _admin_engine, _api_engine = setup_query_engines()
    app.config['preprocessed_data'] = {  # Store the preprocessed data in the app's config
        'arc_engine': _arc_engine,
        'admin_engine': _admin_engine,
        'api_engine': _api_engine
    }
    print("Preprocessing complete.")


with app.app_context():  # Run preprocessing when the application context is initialized
    preprocessing()


def generic_handle_data(engine_name: str):
    if request.is_json:
        generic_engine = app.config['preprocessed_data'][engine_name]  # Access preprocessed data
        api_request = request.get_json().get('request')
        return response_utils.enrich_response(generic_engine.query(api_request)), 200
    else:
        return 'Request must be JSON.', 400


@app.route('/api/arc_engine', methods=['POST'])
def arc_engine():
    return generic_handle_data('arc_engine')


@app.route('/api/admin_engine', methods=['POST'])
def admin_engine():
    return generic_handle_data('admin_engine')


@app.route('/api/api_engine', methods=['POST'])
def api_engine():
    return generic_handle_data('api_engine')


@app.route('/')
def home():
    return "API controller app\n"


def run_server():
    app.run(debug=config.server[config.DEBUG], port=config.server[config.PORT],
            host=config.server[config.DEFAULT_HOST])

# if __name__ == '__main__':
    # run_server()
