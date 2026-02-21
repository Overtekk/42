/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   chained_queue.c                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: roandrie <roandrie@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/02/13 09:12:27 by roandrie          #+#    #+#             */
/*   Updated: 2026/02/21 16:10:05 by roandrie         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "codexion.h"

/**
 * Add a specific coder to the queue. This list is used for the 'First In, First
 * Out' scheduler.
 *
 * Create a new node that point toward the coder and put it first if there is
 * no one. Otherwise, put it at the end of the list.
 */

int	add_to_queue(t_queue_manager *manager, t_coder *coder_to_add)
{
	t_queue	*node;

	node = malloc(sizeof(t_queue));
	if (node == NULL)
		return (1);
	node->coder = coder_to_add;
	node->next = NULL;
	if (manager->first == NULL)
	{
		manager->first = node;
		manager->last = node;
	}
	else
	{
		manager->last->next = node;
		manager->last = node;
	}
	return (0);
}

/**
 * Remove the first coder from the list, free is memory and put the next one
 * (if exist) to the first position.
 */

int	remove_from_queue(t_queue_manager *manager)
{
	t_queue	*temp;

	if (manager->first == NULL)
		return (1);
	temp = manager->first;
	manager->first = temp->next;
	if (manager->first == NULL)
		manager->last = NULL;
	free (temp);
	return (0);
}
