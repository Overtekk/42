/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   sort_check.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: roandrie <roandrie@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/04 09:10:17 by roandrie          #+#    #+#             */
/*   Updated: 2025/12/04 11:18:09 by roandrie         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../include/push_swap.h"

int	sort_three(t_data *data)
{
	size_t	count;
	t_stack *lowest;
	t_stack *biggest;

	count = list_size(data->stack_a);
	lowest = find_lowest_n(data->stack_a);
	biggest = find_biggest_n(data->stack_a);
	ft_printf(1, "Count = %d\n", count);
	ft_printf(1, "lowest number = %d\n", lowest->number);
	ft_printf(1, "biggest number = %d\n", biggest->number);
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
