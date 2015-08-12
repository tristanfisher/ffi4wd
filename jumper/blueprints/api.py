from time import time
from flask import Blueprint, jsonify, request
from .request_structuring import req_to_tuple

from .backends.backend_python import backend_python
from .backends.modules.cython.ffi_cython_py_compat \
    import backend_cython as backend_cypy

from .backends.modules.cython.ffi_cython \
    import backend_cython as backend_cython


blueprint_api = Blueprint("blueprint_python", __name__, url_prefix="/api")


def timer_tuple(f):
    def func_time(*args, **kwargs):
        start = time()
        result = f(*args, **kwargs)
        end = time()

        time_elapsed_seconds = format(end - start, '.6f')

        return result, time_elapsed_seconds
    return func_time


@blueprint_api.route("/python_approximation", methods=["POST"])
def api_python_approximation():

    user_data = req_to_tuple(request.form)
    start = time()
    result = backend_python(user_data, approach='approximate')
    end = time()
    time_elapsed_seconds = format(end - start, '.6f')

    return jsonify(
        backend='python',
        result=result[0],
        backend_runtime=result[1],
        total_runtime=time_elapsed_seconds
    )


@blueprint_api.route("/python", methods=["POST"])
def api_python():

    user_data = req_to_tuple(request.form)
    start = time()
    result = backend_python(user_data)
    end = time()
    time_elapsed_seconds = format(end - start, '.6f')

    return jsonify(
        backend='python',
        result=result[0],
        backend_runtime=result[1],
        total_runtime=time_elapsed_seconds
    )


@blueprint_api.route("/cython", methods=["POST"])
def api_cython():

    user_data = req_to_tuple(request.form)
    start = time()
    #result = backend_cypy(user_data)
    result = backend_cython(user_data)
    end = time()
    time_elapsed_seconds = format(end - start, '.6f')

    return jsonify(
        backend='cython',
        result=result[0],
        backend_runtime=result[1],
        total_runtime=time_elapsed_seconds
    )


@blueprint_api.route("/ctypes", methods=["POST"])
def api_ctypes():

    _stub = ((["check out the documentation https://docs.python.org/3/library/ctypes.html"], 0))

    return jsonify(
        backend='ctypes',
        result=_stub,
        backend_runtime=0,
        total_runtime=0
    )


#
# convert to c struct so we can do c++ structs?
#
@blueprint_api.route("/ffi", methods=["POST"])
def api_ffi():

    user_data = req_to_tuple(request.form)
    start = time()
    result = [0,0]

    end = time()
    time_elapsed_seconds = format(end - start, '.6f')

    return jsonify(
        backend='ffi',
        result=result[0],
        backend_runtime=result[1],
        total_runtime=time_elapsed_seconds

    )