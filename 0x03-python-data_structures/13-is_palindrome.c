#include "lists.h"
#include <stdlib.h>
#include <stdio.h>

/**
* is_palindrome -  function checks if a singly linked list is a palindrome
* @head: pointer to a pointer to the head of the node
* Return: Returns 1 if palindrome, 0 otherwise
*/

int is_palindrome(listint_t **head)
{
	listint_t *node = *head;

	return (check_palindrome(&node, node));
}
