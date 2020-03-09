import logging

bind = "0.0.0.0:8080"
log_level = logging.DEBUG
debug = True
accesslog = logging.getLogger("hypercorn.access")
errorlog = logging.getLogger("hypercorn.error")
