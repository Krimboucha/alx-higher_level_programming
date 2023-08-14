#include "lists.h"

int calculate_length(listint_t *head)
{
	int length = 0;
	listint_t *current = head;

	while (current != NULL)
	{
		length++;
		current = current->next;
	}
	return (length / 2);
}
listint_t* reverseList(listint_t* head)
{
	listint_t *prev = NULL;
        listint_t *current = head;
        listint_t *next = NULL;

	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}
	return (prev);
}
int is_palindrome(listint_t **head)
{
	listint_t *reversedHead = reverseList(*head);
	int middle = calculate_length(*head);
	listint_t *originalCurrent = *head;
	listint_t *reversedCurrent = reversedHead;
	int i;

	i = 0;
	while (i <= middle)
	{
		if (originalCurrent->value != reversedCurrent->value)
    			return (0);
		originalCurrent = originalCurrent->next;
		reversedCurrent = reversedCurrent->next;
		i++;
	}
	listint_t *current = reversedHead;

	while (current != NULL)
	{
		listint_t *temp = current;
		current = current->next;
		free(temp);
	}
	return (1);
}
