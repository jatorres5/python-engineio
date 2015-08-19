import importlib

try:
    queue = importlib.import_module('queue')
except ImportError:  # pragma: no cover
    queue = importlib.import_module('Queue')  # pragma: no cover

async = {
    'threading': importlib.import_module('threading'),
    'queue': queue,
    'queue_class': 'Queue',
    'websocket': None,
    'websocket_class': None
}