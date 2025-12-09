/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   push_swap.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: roandrie <roandrie@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/04 17:50:12 by roandrie          #+#    #+#             */
/*   Updated: 2025/12/06 22:31:06 by roandrie         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../include/push_swap.h"

static	void	turk_algorithm_a_to_b(t_data *data)
{
	t_stack	*cheapest_node;
	int		new_size_a;
	int		new_size_b;
	int		i;

	i = 0;
	while ((data->size_a - 5) > i)
	{
		new_size_a = list_size(data->stack_a);
		new_size_b = list_size(data->stack_b);
		set_current_position(data->stack_a);
		set_current_position(data->stack_b);
		set_target_node_a(data);
		push_cost(data->stack_a, new_size_a, new_size_b);
		cheapest_node = find_cheapest(data->stack_a);
		move_stack_a(data, cheapest_node);
		pb(&(data->stack_a), &(data->stack_b));
		i++;
	}
}

static	void	turk_algorithm_b_to_a(t_data *data)
{
	t_stack	*target_in_a;

	while (data->stack_b != NULL)
	{
		set_current_position(data->stack_a);
		set_current_position(data->stack_b);
		set_target_node_b(data);
		target_in_a = data->stack_b->target_node;
		while (data->stack_a != target_in_a)
		{
			if (target_in_a->middle == 1)
				ra(data);
			else
				rra(data);
		}
		pa(&(data->stack_a), &(data->stack_b));
	}
}

static	void	turk_algorithm_last(t_data *data)
{
	t_stack	*min;

	set_current_position(data->stack_a);
	min = find_lowest_n(data->stack_a);
	while (data->stack_a != min)
	{
		if (min->middle == 1)
			ra(data);
		else
			rra(data);
	}
}

void	sort_all(t_data *data)
{
	pb(&(data->stack_a), &(data->stack_b));
	pb(&(data->stack_a), &(data->stack_b));
	turk_algorithm_a_to_b(data);
	sort_three(data);
	turk_algorithm_b_to_a(data);
	turk_algorithm_last(data);
}
