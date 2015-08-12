#!/usr/bin/env python
import sys
sys.path.append('..')
sys.path.append('.')

from jumper.blueprints.backends.modules.ffi import fficpp
print(fficpp.system('ls'))
