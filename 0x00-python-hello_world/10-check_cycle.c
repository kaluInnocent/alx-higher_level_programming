#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
/**
* check_cycle - function checks if asingly linked list has a cylde in it
* @list: a node pointer
* Return: Retruns 1 if exists and 0 otherwise
*/
int check_cycle(listint_t *list)
{
	listint_t *slow;
	listint_t *fast;

	slow = list;
	fast = list;

	while (slow && fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
			return (1);
	}
	return (0);
}
