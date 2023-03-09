#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list.
 * @head: list head
 * @number: number to store in the new node
 * Return: pointer to the new node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *recent;
	listint_t *new;

	runner = *head;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;

	if (*head == NULL || (*head)->n > number)
	{
		new->next = *head;
		*head = new;
		return (new);
	}

	while (recent->next != NULL)
	{
		if ((recent->next)->n >= number)
		{
			new->next = recent->next;
			recent->next = new;
			return (new);
		}
		recent = recent->next;
	}

	new->next = NULL;
	recent->next = new;
	return (new);
}
