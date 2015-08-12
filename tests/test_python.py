import sys
sys.path.append('..')
sys.path.append('.')

from jumper.blueprints.backends import backend_python

# backend_python.py
if __name__ == "__main__":

    from jumper.blueprints.backends.fixture_data import test_cities_eleven_tuples
    from cProfile import run
    cmd = "backend_python(test_cities_eleven_tuples)"
    run(cmd)
