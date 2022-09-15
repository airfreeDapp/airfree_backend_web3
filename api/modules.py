from leanapi.server import Modules
from .routes.airfree.airfree import AirFree

modules = Modules.controllers([AirFree])
