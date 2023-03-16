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
		fprintf(stdout, "  [ERROR] Invalid Bytes Object\n");
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
	int i = 0, len = 0;
	PyObject *item;

	fprintf(stdout, "[*] Python list info\n");
	len = PyList_GET_SIZE(p);
	fprintf(stdout, "[*] Size of the Python List = %d\n", len);
	fprintf(stdout, "[*] Allocated = %d\n", (int) ((PyListObject *)p)->allocated);
	for (; i < len; ++i)
	{
		item = PyList_GET_ITEM(p, i);
		fprintf(stdout, "Element %d: %s\n", i, item->ob_type->tp_name);

		if (PyBytes_Check(item))
			print_python_bytes(item);
	}
}
