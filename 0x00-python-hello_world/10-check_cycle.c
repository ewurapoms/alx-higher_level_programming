#include "lists.h"

/**
 * check_cycle - function checks if a singly linked list has a cycle in it
 * @list: is head ptr to a linked list
 * Return: 1 if cycle exists, otherwise 0
 */

int check_cycle(listint_t *list)
{
	listint_t *start = list;
	listint_t *loop = list;

	while (start && (start = start->next))
	{
		if (start == loop)
			return (1);
		start = start->next;
		loop = loop->next;
	}
	return (0);
}
