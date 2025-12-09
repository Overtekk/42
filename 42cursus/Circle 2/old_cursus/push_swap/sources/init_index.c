/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   init_index.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: roandrie <roandrie@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/02 18:00:40 by roandrie          #+#    #+#             */
/*   Updated: 2025/12/06 17:36:07 by roandrie         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../include/push_swap.h"

static	void	init_list_size(t_data *data)
{
	data->size_a = list_size(data->stack_a);
	data->size_b = list_size(data->stack_b);
}

void	init_index(t_data *data)
{
	t_stack	*curr;
	t_stack	*cmp;

	curr = data->stack_a;
	while (curr != NULL)
	{
		cmp = data->stack_a;
		while (cmp != NULL)
		{
			if (cmp->number < curr->number)
				curr->index++;
			cmp = cmp->next;
		}
		curr = curr->next;
	}
	init_list_size(data);
}
