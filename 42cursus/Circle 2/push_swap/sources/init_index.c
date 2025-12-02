/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   init_index.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: roandrie <roandrie@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/02 18:00:40 by roandrie          #+#    #+#             */
/*   Updated: 2025/12/02 19:33:23 by roandrie         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../include/push_swap.h"

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
}
