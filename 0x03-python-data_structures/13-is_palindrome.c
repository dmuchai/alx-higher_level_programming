#include "lists.h"

/**
 * is_palindrome_recursive - Helper function that uses recursion to check palindrome.
 * @left: Pointer to the left node (used to traverse the list from start).
 * @right: Pointer to the right node (used to traverse the list to end).
 *
 * Return: 1 if the list is a palindrome, 0 otherwise.
 */
int is_palindrome_recursive(listint_t **left, listint_t *right)
{
	int result;

	if (right == NULL)
		return (1);

	result = is_palindrome_recursive(left, right->next);
	if (result == 0)
		return (0);

	if (right->n != (*left)->n)
		return (0);

	*left = (*left)->next;
		return (1);
}

/**
 * is_palindrome - Main function to check if a singly linked list is a palindrome.
 * @head: Double pointer to the head of the list.
 *
 * Return: 1 if the list is a palindrome, 0 otherwise.
 */
int is_palindrome(listint_t **head)
{
	if (head == NULL || *head == NULL)
	return (1);

	return (is_palindrome_recursive(head, *head));
}
