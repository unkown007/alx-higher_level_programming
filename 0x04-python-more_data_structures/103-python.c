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
	PyBytesObject *item;
	char *buff;
	int len = 0, i = 0, bytes;

	fprintf(stdout, "[.] bytes object info\n");
	item = (PyBytesObject *) p;
	if (!PyBytes_Check(p))
	{
		fprintf(stderr, "  [ERROR] Invalid Bytes Object\n");
		return;
	}
	else
	{
		len = PyBytes_Size(p);
		bytes = len + 1;
		fprintf(stdout, "  size: %d\n", len);
		buff = item->ob_sval;
		fprintf(stdout, "  trying string: %s\n", buff);
		bytes = (bytes >= 10) ? 10 : bytes;
		fprintf(stdout, "  first %d bytes: ", bytes);
		for (i = 0; i < bytes - 1; i++)
		{
			fprintf(stdout, "%02x ", (unsigned char) buff[i]);
		}
		printf("%02x\n", (unsigned char) buff[i]);
	}
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
	fprintf(stdout, "[*] Python list info\n");
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
