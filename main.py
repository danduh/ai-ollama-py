import config
import utils.response_utils as utils
import logging
import server.app as app
from router.query_router import admin_engine


def test_queries():
    if admin_engine is not None:
        logging.info(f'attempting query')
        results = admin_engine.query("im getting an error for adding a device, what are the reasons for that")
        logging.info(f'query complete')
        if config.feature_flags[config.FEATURE_FLAGS_STREAMING]:
            results.print_response_stream()
        return utils.enrich_response(results)


if __name__ == "__main__":
    # setup rest service
    app.run_server()
    # print(test_queries())
