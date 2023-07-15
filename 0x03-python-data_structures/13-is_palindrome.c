#include "lists.h"

int faux_palindrome(listint_t **head, listint_t *tail);

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: double pointer
 *
 * Return: 1 if the list is a palindrome, else 0
 */
int is_palindrome(listint_t **head)
{
	return (head && faux_palindrome(head, *head));
}


/**
 * faux_palindrome - Helper function for the singly list
 * @head: ptr
 * @tail: ptr
 * Return: ...
 */
int faux_palindrome(listint_t **head, listint_t *tail)
{
	int checks = 1;

	if (tail)
	{
		checks = faux_palindrome(head, tail->next);

		if (tail == *head || tail->next == *head)
			*head = tail;
		else if (checks && (*head)->n == tail->n)
			*head = (*head)->next;
		else
			checks = 0;
	}
	return (checks);
}
