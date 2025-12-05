/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   algo_utils.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: roandrie <roandrie@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/05 09:06:59 by roandrie          #+#    #+#             */
/*   Updated: 2025/12/05 17:21:08 by roandrie         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../../include/push_swap.h"

void	set_current_position(t_stack *stack)
{
	t_stack	*curr;
	int		i;
	int		middle;

	i = 0;
	middle = (list_size(stack)) / 2;
	curr = stack;
	while (curr != NULL)
	{
		curr->pos = i;
		if (i <= middle)
			curr->middle = 1;
		else
			curr->middle = 0;
		curr = curr->next;
		i++;
	}
}

void	set_target_node(t_data *data)
{
	t_stack	*curr_a;
	t_stack	*curr_b;
	long	cmp;

	curr_a = data->stack_a;
	while (curr_a != NULL)
	{
		cmp = LONG_MIN;
		curr_a->target_node = NULL;
		curr_b = data->stack_b;
		while (curr_b != NULL)
		{
			if ((curr_b->index < curr_a->index) && (curr_b->index > cmp))
			{
					curr_a->target_node = curr_b;
					cmp = curr_b->index;
			}
			curr_b = curr_b->next;
		}
		if (curr_a->target_node == NULL)
			curr_a->target_node = find_biggest_n(data->stack_b);
		curr_a = curr_a->next;
	}
}
