/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   sort_check.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: roandrie <roandrie@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/04 09:10:17 by roandrie          #+#    #+#             */
/*   Updated: 2025/12/04 14:56:02 by roandrie         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../include/push_swap.h"

static	int	sort_three(t_data *data)
{
	t_stack	*lowest_n;

	lowest_n = find_lowest_n(data->stack_a);
	while (data->stack_a != lowest_n)
		ra(data);
	pb(&(data->stack_a), &(data->stack_b));
	if (data->stack_a->index > data->stack_a->next->index)
		sa(data);
	pa(&(data->stack_a), &(data->stack_b));
	return (0);
}

static	int	sort_four(t_data *data)
{
	t_stack	*lowest_n;
	int		i;

	i = 2;
	while (i > 0)
	{
		lowest_n = find_lowest_n(data->stack_a);
		while (data->stack_a != lowest_n)
			ra(data);
		pb(&(data->stack_a), &(data->stack_b));
		i--;
	}
	if (data->stack_a->index > data->stack_a->next->index)
		sa(data);
	if (data->stack_b->index < data->stack_b->next->index)
		sb(data);
	pa(&(data->stack_a), &(data->stack_b));
	pa(&(data->stack_a), &(data->stack_b));
	return (0);
}

int	check_numbers(t_data *data)
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
	return (0);
}
