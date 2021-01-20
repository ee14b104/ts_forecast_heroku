#!/usr/bin/env python3

import connexion

from swagger_server import encoder
import os


def main():
    app = connexion.App(__name__, specification_dir='./swagger/')
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('swagger.yaml', arguments={'title': 'sktime forecast'}, pythonic_params=True)
    ON_HEROKU = os.environ.get('ON_HEROKU')
    if ON_HEROKU:
    # get the heroku port 
        port = int(os.environ.get("PORT", 17995))  # as per OP comments default is 17995
    else:
        port = 8080
    app.run(port=port)


if __name__ == '__main__':
    main()
