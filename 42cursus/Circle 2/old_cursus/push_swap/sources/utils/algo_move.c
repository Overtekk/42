/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   algo_move.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: roandrie <roandrie@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/06 20:32:59 by roandrie          #+#    #+#             */
/*   Updated: 2025/12/06 20:40:46 by roandrie         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../../include/push_swap.h"

static	void	move_stack_b_2(t_data *data, t_stack *cheapest_node)
{
	while (cheapest_node != data->stack_b)
	{
		if (cheapest_node->middle == 1)
			rb(data);
		else
			rrb(data);
	}
	while (cheapest_node->target_node != data->stack_a)
	{
		if (cheapest_node->target_node->middle == 1)
			ra(data);
		else
			rra(data);
	}
}

void	move_stack_b(t_data *data, t_stack *cheapest_node)
{
	if (cheapest_node->middle == 1 && cheapest_node->target_node->middle == 1)
	{
		while (data->stack_b != cheapest_node && data->stack_a
			!= cheapest_node->target_node)
			rr(data);
	}
	else if (cheapest_node->middle == 0
		&& cheapest_node->target_node->middle == 0)
	{
		while (data->stack_b != cheapest_node
			&& data->stack_a != cheapest_node->target_node)
			rrr(data);
	}
	move_stack_b_2(data, cheapest_node);
}

static	void	move_stack_a_2(t_data *data, t_stack *cheapest_node)
{
	while (cheapest_node != data->stack_a)
	{
		if (cheapest_node->middle == 1)
			ra(data);
		else
			rra(data);
	}
	while (cheapest_node->target_node != data->stack_b)
	{
		if (cheapest_node->target_node->middle == 1)
			rb(data);
		else
			rrb(data);
	}
}

void	move_stack_a(t_data *data, t_stack *cheapest_node)
{
	if (cheapest_node->middle == 1 && cheapest_node->target_node->middle == 1)
	{
		while (data->stack_a != cheapest_node && data->stack_b
			!= cheapest_node->target_node)
			rr(data);
	}
	else if (cheapest_node->middle == 0
		&& cheapest_node->target_node->middle == 0)
	{
		while (data->stack_a != cheapest_node
			&& data->stack_b != cheapest_node->target_node)
			rrr(data);
	}
	move_stack_a_2(data, cheapest_node);
}
