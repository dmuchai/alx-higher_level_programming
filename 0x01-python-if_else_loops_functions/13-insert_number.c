#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - Inserts a number into a sorted singly linked list.
 * @head: Double pointer to the head of the list.
 * @number: The number to insert into the list.
 * Return: Address of the new node, or NULL if it failed.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *my_new_node, *current;

	my_new_node = malloc(sizeof(listint_t));
	if (my_new_node == NULL)
	return (NULL);

	my_new_node->n = number;
	my_new_node->next = NULL;

	if (*head == NULL || (*head)->n >= number)
	{
		my_new_node->next = *head;
		*head = my_new_node;
		return (my_new_node);
	}

	current = *head;
	while (current->next != NULL && current->next->n < number)
	{
		current = current->next;
	}

	my_new_node->next = current->next;
	current->next = my_new_node;

	return (my_new_node);
}
