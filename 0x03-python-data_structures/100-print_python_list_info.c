#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include <stdio.h>

/**
 * print_python_list_info - prints some basic info about Python lists
 * @p: pointer to Python object
 */
void print_python_list_info(PyObject *p)
{
	Py_ssize_t i, n;
	PyObject *item;

	n = PyList_Size(p);
	if (n < 0)
		return;
	fprintf(stdout, "[*] Size of the Python List = %ld\n", n);
	fprintf(stdout, "[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);
	for (i = 0; i < n; i++)
	{
		fprintf(stdout, "Element %ld: ", i);
		item = PyList_GetItem(p, i);
		if (PyLong_Check(item))
		{
			fprintf(stdout, "int\n");
		}
		if (PyFloat_Check(item))
		{
			fprintf(stdout, "float\n");
		}
		if (PyUnicode_Check(item))
		{
			fprintf(stdout, "str\n");
		}
		if (PyList_Check(item))
		{
			fprintf(stdout, "list\n");
		}
		if (PyTuple_Check(item))
		{
			fprintf(stdout, "tuple\n");
		}
	}
}
