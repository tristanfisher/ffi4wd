import sys
sys.path.append('..')
sys.path.append('.')

import cProfile
from jumper.blueprints.backends.fixture_data import test_cities_eleven_tuples as test_11_cities

from jumper.blueprints.backends.modules.cython \
    import ffi_cython_py_compat as ffi_py

from jumper.blueprints.backends.modules.cython \
    import ffi_cython as ffi_cy

def test_profile_backend_cypy():
    cmd = "ffi_py.backend_cython(test_11_cities)"
    cProfile.run(cmd)

def test_profile_backend_cython():
    #test_11_cities is test data
    cmd = "ffi_cy.backend_cython(test_11_cities)"
    cProfile.run(cmd)

test_profile_backend_cypy()
#test_profile_backend_cython()