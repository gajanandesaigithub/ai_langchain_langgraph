import logging


## Configuring logging
logging.basicConfig(
    filename='app.log',
    filemode='w',
    level=logging.DEBUG,
    format='%(asctime)s-%(name)s-%(levelname)s-%(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    force=True                          #In Python logging, logging.basicConfig() only works once per process. force = True will 1) Remove existing handlers, 2) Reconfigure logging using your settings
)

