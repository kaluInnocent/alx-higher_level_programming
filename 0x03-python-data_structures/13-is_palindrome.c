#include "lists.h"
#include <stdlib.h>
#include <stdio.h>

/**
* check_palindrome - function checks for a palindrome
* @left: pointer to a pointer to the first half of the linked list
* @right: pointer to the 2nd half of the linked list
* Return: function returns 1 iuf palindrome, 0 otherwise
*/

int check_palindrome(listint_t **left, listint_t *right)
{
	int ispalindrome;

	/*
	 * if right equals NULL, end recursion
	 */
	if (right == NULL)
		return (1);

	/*
	 * if half of the list is not a palindrome, then we need to check for
	 * current left and right, return 0
	 */
	ispalindrome = check_palindrome(left, right->next);
	if (ispalindrome != 1)
		return (0);
	/*
	 * Check values at current left and right
	 */
	if (right->n == (*left)->n)
		*left = (*left)->next;
	return (1);
}

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
