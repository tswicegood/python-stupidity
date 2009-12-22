#!/usr/bin/env python
from barfoo import base_barfoo # <-- loads barfoo/__init__.py
import foobar # <-- tries to import from barfoo/__init__.py, but gets hung up on foobar.barfoo

