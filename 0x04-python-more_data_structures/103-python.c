#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include <stdio.h>
#include <stdlib.h>

/**
 * print_python_bytes - print some basic info about Python bytes objects
 * @p: pointer to Python Object
 */
void print_python_bytes(PyObject *p)
{
	PyObject *item;
	PyObject *ascii_obj = NULL;
	char *buff;
	Py_ssize_t len = 0, i, aux;

	fprintf(stdout, "[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		fprintf(stderr, "  [ERROR] Invalid Bytes Object\n");
		return;
	}
	item = PyBytes_FromObject(p);
	if (PyUnicode_Check(item))
	{
		ascii_obj = PyUnicode_AsASCIIString(item);
		if (PyBytes_AsStringAndSize(ascii_obj, &buff, &len) < 0)
			return;
	}
	else
	{
		if (PyBytes_AsStringAndSize(item, &buff, &len) < 0)
			return;
	}
	fprintf(stdout, "  size: %ld\n", len);
	fprintf(stdout, "  trying string: %s\n", buff);
	aux = len < 10 ? (len + 1) : 10l;
	fprintf(stdout, "  first %ld bytes: ", aux);
	for (i = 0; i < aux; i++)
	{
		fprintf(stdout, "%02hhx", buff[i]);
		if (i != aux - 1)
			fprintf(stdout, " ");
		else
			fprintf(stdout, "\n");
	}
	Py_XDECREF(ascii_obj);
}

/**
 * print_python_list - prints some basic info about Python lists
 * @p: pointer to Python object
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t i;
	PyObject *iter;
	PyObject *item;

	iter = PyObject_GetIter(p);
	if (iter == NULL)
	{
		fprintf(stdout, "List is empty!\n");
		return;
	}
	fprintf(stdout, "[*] Python List info\n");
	fprintf(stdout, "[*] Size of the Python List = %ld\n", PyList_Size(p));
	fprintf(stdout, "[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);
	i = 0;
	item = PyIter_Next(iter);
	while (item != NULL)
	{
		fprintf(stdout, "Element %ld: ", i);
		if (PyLong_Check(item))
			fprintf(stdout, "int\n");
		if (PyFloat_Check(item))
			fprintf(stdout, "float\n");
		if (PyUnicode_Check(item))
			fprintf(stdout, "str\n");
		if (PyList_Check(item))
			fprintf(stdout, "list\n");
		if (PyTuple_Check(item))
			fprintf(stdout, "tuple\n");
		if (PyBytes_Check(item))
			fprintf(stdout, "bytes\n");
		Py_DECREF(item);
		i++;
		item = PyIter_Next(iter);
	}
}
