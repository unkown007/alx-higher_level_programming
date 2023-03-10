#include <stdlib.h>
#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: head of the listint_t list
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *node;
	int size, sum1, sum2, i;

	if (*head == NULL)
		return (1);
	size = 0;
	node = *head;
	while (node)
	{
		size++;
		node = node->next;
	}
	node = *head;
	sum1 = sum2 = 0;
	i = 1;
	while (node)
	{
		if (i <= (size / 2))
			sum1 += node->n;
		else
			sum2 += node->n;
		i++;
		node = node->next;
	}
	if (sum1 == sum2)
		return (1);
	return (0);
}
