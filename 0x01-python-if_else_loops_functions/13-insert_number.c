#include "lists.h"
#include <stdlib.h>
#include <stdio.h>
/**
* insert_node - function inserts a number into a sorted linked list
* @head: pointer to a pointer to the first node on the linked list
* @number: number to be inserted
* Return: The address of the new node or NULL if it failed
*/

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current = *head;
	listint_t *new_node;

	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);

	new_node->n = number;
	if (*head == NULL || (*head)->n >= new_node->n)
	{
		new_node->next = *head;
		*head = new_node;
		return (new_node);
	}
	while (current && current->next && current->next->n < new_node->n)
	{
		current = current->next;
	}

	new_node->next = current->next;
	current->next = new_node;
	return (new_node);
}
