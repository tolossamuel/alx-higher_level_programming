#ifndef LISTS_H
#define LISTS_H

#include <stdlib.h>

/**
 * struct listint_s - linked list
 * @n: variables
 * @next: next node
 */
typedef struct listint_s
{
	int n;
	struct listint_s *next;
} listint_t;

size_t print_listint(const listint_t *h);
listint_t *add_node(listint_t **head, const int n);
void free_int(listint_t *head);
int check_cycle(listint_t *list);

#endif /* LISTS_H */
