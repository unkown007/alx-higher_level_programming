#include <stdlib.h>
#include "lists.h"

/**
 * isPalindrome -  checks if a singly linked list is a palindrome
 * @left: head of the listint_t list
 * @right: last element of listint_t list
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int isPalindrome(listint_t **left, listint_t *right)
{
	int isp, isp1;

	if (right == NULL)
		return (1);
	isp = isPalindrome(left, right->next);
	if (isp == 0)
		return (0);
	isp1 = (right->n == (*left)->n) ? 1 : 0;
	*left = (*left)->next;
	return (isp1);
}

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: head of the listint_t list
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	/*listint_t *node;
	int size, sum1, sum2, i;

	if (head == NULL)
		return (0);
	if (*head == NULL)
		return (1);
	size = 0;
	node = *head;
	while (node)
	{
		size++;
		node = node->next;
	}
	if (size == 1)
		return (1);
	node = *head;
	sum1 = sum2 = 0;
	i = 1;
	while (node && i <= (size / 2))
	{
		sum1 += node->n;
		i++;
		node = node->next;
	}
	if (size % 2 != 0 && node)
		node = node->next;
	while (node)
	{
		sum2 += node->n;
		node = node->next;
	}
	if (sum1 == sum2)
		return (1);
	return (0);*/
	return (isPalindrome(head, *head));
}
