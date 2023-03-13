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
	return (isPalindrome(head, *head));
}
