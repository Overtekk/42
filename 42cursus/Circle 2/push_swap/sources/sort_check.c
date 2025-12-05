/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   sort_check.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: roandrie <roandrie@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/04 09:10:17 by roandrie          #+#    #+#             */
/*   Updated: 2025/12/05 09:09:05 by roandrie         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../include/push_swap.h"

static	void	sort_three(t_data *data)
{
	t_stack	*big;

	big = find_biggest_n(data->stack_a);
	if (data->stack_a->index == big->index)
		ra(data);
	else if (data->stack_a->next->index == big->index)
	{
		sa(data);
		ra(data);
	}
	if (data->stack_a->index > data->stack_a->next->index)
		sa(data);
}

static	void	sort_four(t_data *data)
{
	t_stack	*lowest_n;

	lowest_n = find_lowest_n(data->stack_a);
	while (data->stack_a != lowest_n)
	{
		ra(data);
	}
	pb(&(data->stack_a), &(data->stack_b));
	sort_three(data);
	pa(&(data->stack_a), &(data->stack_b));
}

static	void	move_to_top(t_data *data, int target_index)
{
	size_t	size;
	size_t	pos;

	while (data->stack_a->index != target_index)
	{
		size = list_size(data->stack_a);
		pos = get_pos(data, target_index);
		if (pos < (size / 2))
			ra(data);
		else
			rra(data);
	}
}

static	void	sort_five(t_data *data)
{
	int		i;

	i = 0;
	while (i < 2)
	{
		move_to_top(data, i);
		pb(&(data->stack_a), &(data->stack_b));
		i++;
	}
	sort_three(data);
	pa(&(data->stack_a), &(data->stack_b));
	pa(&(data->stack_a), &(data->stack_b));
}

int	check_sort_algo(t_data *data)
{
	size_t	count;

	count = list_size(data->stack_a);
	if (count == 2)
	{
		if (data->stack_a->index > data->stack_a->next->index)
			sa(data);
		return (0);
	}
	else if (count == 3)
		return (sort_three(data), 0);
	else if (count == 4)
		return (sort_four(data), 0);
	else if (count == 5)
		return (sort_five(data), 0);
	else
		return (sort_all(data), 0);
	return (0);
}
