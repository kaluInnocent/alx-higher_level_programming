#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
* is_palindrome - function checks if a singly linked list is a palindrome
* @head: A pointer to a pointer to the start of the singly linked list
* Return: 0 if it is not a palindrome, 1 if it is
*
*/

int is_palindrome(listint_t **head)
{
	int i, j, count = 0;
	int arr[2000];
	listint_t *ptr = *head;

	if (!head || !(*head) || (*head)->next == NULL)
		return (1);

	while (ptr)
	{
		arr[count] = ptr->n;
		ptr = ptr->next;
		count++;
	}

	j = count - 1;
	for (i = 0; i < (count / 2) + 1; i++, j--)
	{
		if (arr[i] == arr[j])
			return (1);
	}
	return (0);
}
