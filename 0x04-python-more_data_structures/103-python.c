#include <stdio.h>
#include <Python.h>

/**
 * print_python_bytes - function that prints the bytes information
 * @p: Python Object
 * Return: nothing
 */

void print_python_bytes(PyObject *p)
{
	char *str_;
	long int size, i, len;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	size = ((PyVarObject *)(p))->ob_size;
	str_ = ((PyBytesObject *)p)->ob_sval;

	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", str_);

	if (size >= 10)
		len = 10;
	else
		len = size + 1;

	printf("  first %ld bytes:", len);

	for (i = 0; i < len; i++)
		if (str_[i] >= 0)
			printf(" %02x", str_[i]);
		else
			printf(" %02x", 256 + str_[i]);

	printf("\n");
}

/**
 * print_python_list - function prints list info
 * @p: is a pointer to Python Object
 * Return: nothing
 */
void print_python_list(PyObject *p)
{
	long int size, i;
	PyListObject *list;
	PyObject *y;

	size = ((PyVarObject *)(p))->ob_size;
	list = (PyListObject *)p;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", list->allocated);

	for (i = 0; i < size; i++)
	{
		y = ((PyListObject *)p)->ob_item[i];
		printf("Element %ld: %s\n", i, ((y)->ob_type)->tp_name);
		if (PyBytes_Check(y))
			print_python_bytes(y);
	}
}
