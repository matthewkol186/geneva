import os
import random
import binascii
from layers.layer import Layer
from scapy.all import fuzz
from scapy.layers.http import HTTPRequest


class HTTPRequestLayer(Layer):
    """
    Defines an interface to access HTTP header fields.
    """
    name = "HTTPRequest"
    protocol = HTTPRequest
    _fields = [
        'Method',
        'Path',
    ]
    fields = _fields

    def __init__(self, layer):
        """
        Initializes the HTTP layer.
        """
        Layer.__init__(self, layer)
        # Special methods to help access fields that cannot be accessed normally
        self.getters = {
        }
        self.setters = {
        }
        # Special methods to help generate fields that cannot be generated normally
        self.generators = {
        }
