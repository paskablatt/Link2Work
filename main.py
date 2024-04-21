# ------------------------------------------------------
#   Link2Work Project Start File
#   Urfu Project Digital Portfolio
# ------------------------------------------------------
#  
# Description:
#   main.py - entrypoint file
#   auth.py - file with user authentication logic
#   files.py - file with file upload/delete/etc logic
#   userprofile.py - file with logic for user's profile management
#   web.py - file with deploying web site logic   
# 
#
# Author:
#   Team «Мы»


import logging
import argparse
from routes import deploy_web
from db import Database

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
                    add_help=True,
                    description=
                        "link2work.py - it is URFU Digital Project\
                        for managing users's achievements and awards \
                        in one self-hosted solution")
    parser.add_argument("-debug", action="store_true", help='Turn Debug output ON')
    parser.add_argument("-port", action="store", help="From 1 to 65536 port value on which web server will be started", default=80)

    options = parser.parse_args()

    if options.debug is True:
        logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
    else:
        logging.basicConfig(level=logging.CRITICAL, format='%(asctime)s - %(levelname)s - %(message)s')
    
    if options.port is not None:
        port = options.port

    Database.setup_db()
    deploy_web(debug=options.debug, port=port)
    