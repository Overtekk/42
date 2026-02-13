/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   queue_fifo.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: roandrie <roandrie@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/02/13 09:12:27 by roandrie          #+#    #+#             */
/*   Updated: 2026/02/13 11:08:19 by roandrie         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "codexion.h"

int	add_to_queue(t_queue_manager *manager, t_coder *coder_to_add)
{
	t_queue	*node;

	node = malloc(sizeof(t_queue));
	if (node == NULL)
		return (1);
	node->coder = coder_to_add;
	node->next = NULL;
	pthread_mutex_lock(&manager->lock);
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
	pthread_mutex_unlock(&manager->lock);
	return (0);
}
