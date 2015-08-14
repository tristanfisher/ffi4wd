#!/usr/bin/env python

import sys
sys.path.append('..')
sys.path.append('.')

from jumper.blueprints.backends.modules.ctypes.ffi_ctypes import FFICTypes

t = FFICTypes()
t.example_world()
