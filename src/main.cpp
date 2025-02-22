#include <Python.h>

// CPP functions that will be called from Python
static PyObject *functionFromCPP(PyObject *self, PyObject *args)
{
    printf("This message comes from CPP\n");
    return Py_BuildValue("s", "Hello from CPP");
}

static PyObject *functionFromCPP2(PyObject *self, PyObject *args)
{
    int a, b;
    if (!PyArg_ParseTuple(args, "ii", &a, &b))
        return NULL;
    printf("The sum of %d and %d is %d\n", a, b, a + b);
    return Py_BuildValue("i", a + b);
}

// CPP Variables that will be used in Python
static PyObject *variableFromCPP = PyLong_FromLong(42);
static PyObject *variableFromCPP2 = Py_BuildValue("s", "Hello from CPP variable 2");

// Method definition structure
static PyMethodDef MyMethods[] = {
    // Method definition structure
    {"functionFromCPP", functionFromCPP, METH_VARARGS, "Function from CPP"},
    {"functionFromCPP2", functionFromCPP2, METH_VARARGS, "Function from CPP with arguments"},
    {NULL, NULL, 0, NULL} // Sentinel
};

// Module definition to register the module
static struct PyModuleDef etkindmodule = {
    PyModuleDef_HEAD_INIT,
    "pycmtemplate_c", // Module name
    NULL,             // Module documentation
    -1,               // Size of per-interpreter state
    MyMethods};

// Module initialization
PyMODINIT_FUNC PyInit_pycmtemplate_c(void)
{
    // Create the module
    PyObject *module = PyModule_Create(&etkindmodule);
    if (module == NULL)
        return NULL;

    // Add variables to the module
    PyModule_AddObject(module, "variableFromCPP", variableFromCPP);
    PyModule_AddObject(module, "variableFromCPP2", variableFromCPP2);

    return module;
}