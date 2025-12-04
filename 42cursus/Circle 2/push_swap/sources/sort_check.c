/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   sort_check.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: roandrie <roandrie@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/04 09:10:17 by roandrie          #+#    #+#             */
/*   Updated: 2025/12/04 13:49:35 by roandrie         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../include/push_swap.h"

int	sort_three(t_data *data)
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
	if (count >= 3)
	{
		sort_three(data);
		return (0);
	}
	return (0);
}
