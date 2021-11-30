#include <Python.h>

/**
* print_python_list_info - function prints python list infor
* @p: A pointer object
* Return: void
*/

void print_python_list_info(PyObject *p)
{
	Py_ssize_t size, all, index;

	size = PyList_Size(p);
	all = ((PyListObject *)p)->allocated;
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", all);

	for (index = 0; index < size; index++;)
	{
		printf("Element %ld: %s\n", index,
				(PY_TYPE(PyList_GetItem(p, index)))->tp_name);
	}
}
