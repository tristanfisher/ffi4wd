#include "Python.h"

// implictly calls stdio.h string.h errno.h stdlib.h

/*
 * Standard hello world.  We want to call:
 *
 * # test.py:
 * import fficpp
 * message = fficpp.helloworld()
 *
 */

/*
 * Create a method table
 * Create initialization function.  Must be named PyInit_x() where x is the name of the module
 *      this PyInit function should be the only non-static item in the module file
 * Reference method table in module definition structure
 * Pass module definition struction to module initialization function
 *
 *
 */

/* custom error type */
static PyObject *FFICPPError;

static PyObject *
fficpp_system(PyObject *self, PyObject *args)
{
    const char *command;
    int return_code;

    // all incoming arguments are Python ojects. PyArg_ParseTuple converts to C values.
    if (!PyArg_ParseTuple(args, "s", &command))
        return NULL;

    // call Unix function system
    return_code = system(command);

    if (return_code < 0){
        PyErr_SetString(FFICPPError, "System command failed");
        return NULL;
    }

    // if calling a void, return None (a Python object, not NULL pointer)
    // Py_INCREF(Py_None);
    // return Py_None;

    return PyLong_FromLong(return_code);  // "int" response from system
};

/* method table */
static PyMethodDef FFICppMethods[] = {
        {"system", fficpp_system, METH_VARARGS, "Execute a command shell."},
        {NULL, NULL, 0, NULL} /* sentinel to mark end of function structs */
};

static struct PyModuleDef fficppmodule = {
        PyModuleDef_HEAD_INIT,
        "fficpp",       /* module name */
        NULL,           /* module documentation e.g. static char docs[] = "blah blah" */
        -1,             /* size of per-interpreter module stat. -1 for state in global vars */
        FFICppMethods   /* module method list */
};

/* initialization function. _must_ be named PyInit_modulenamehere */
/* this declares the function as return type PyObject *, does linking,
 * and declares function as `extern "C"` for C++
 */

PyMODINIT_FUNC
PyInit_fficpp(void)
{
    return PyModule_Create(&fficppmodule);
}


/*
 * When Python imports module fficpp for the first time
 *
 * 1. PyInit_fficpp() is called
 * 2. This call PyModule_Create()
 * 3. This inserts built-in functions into our method table
 * 4. PyModule_Create returns a pointer to the module object it created
 * 5. This module object is returned to the caller, which inserts it into sys.modules in Python if return is not NULL
 */