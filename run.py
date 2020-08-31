#!/usr/bin/python
# -*- coding: UTF-8 -*

import os

from api import create_app
from config import configuration

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
if __name__ == '__main__':
    host, port, debug = configuration.get_start_config()
    app.run(host=host, port=port, debug=eval(debug))