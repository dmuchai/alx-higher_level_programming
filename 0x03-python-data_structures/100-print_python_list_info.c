#include <stdio.h>
#include <Python.h>
#include <object.h>
#include <listobject.h>
/**
 * print_python_list_info - displays basic info about Python lists
 * @p: object rep a Python list
 *
 * Return: 0
 */
void print_python_list_info(PyObject *p)
{
	long int size_list, alloc, i;

	i = 0;
	PyObject *object;

	size_list = PyList_Size(p);
	alloc = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %ld\n", size_list);
	printf("[*] Allocated = %ld\n", alloc);
	while (i < size_list)
	{
		object = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", i, Py_TYPE(obj)->tp_name);
		i++;
	}
}
