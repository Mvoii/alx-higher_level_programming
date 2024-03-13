#include "lists.h"
/**
 * check_cycle - checks whether a list cycles or not
 * @list: singly linked list
 * Return: 0 for no cycles and 1 for cycles
 */
int check_cycle(listint_t *list)
{
	listint_t *current = NULL, *temp = NULL;

	if (list == NULL)
		return (0);
	current = list;
	temp = list->next;

	while (temp != NULL && temp->next != NULL)
	{
		if (temp == current)
			return (1);
		current = current->next;
		temp = (temp->next)->next;
	}
	return (0);
}
