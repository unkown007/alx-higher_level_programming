#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: head of the list
 * @number: number to insert
 *
 * Return: the address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new;
	listint_t *curr;
	listint_t *prev;

	curr = *head;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = number;
	if (*head == NULL)
	{
		new->next = NULL;
		*head = new;
	}
	else
	{
		while (curr && curr->n < number)
		{
			prev = curr;
			curr = curr->next;
		}
		if (curr == *head)
		{
			new->next = *head;
			*head = new;
		}
		else
		{
			new->next = curr;
			prev->next = new;
		}
	}
	return (new);
}
