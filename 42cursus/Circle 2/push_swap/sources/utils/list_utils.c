/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   list_utils.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: roandrie <roandrie@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/04 09:17:57 by roandrie          #+#    #+#             */
/*   Updated: 2025/12/04 11:15:49 by roandrie         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../../include/push_swap.h"

size_t	list_size(t_stack *lst)
{
	size_t	count;
	t_stack	*curr;

	count = 0;
	curr = lst;
	while (curr != NULL)
	{
		count++;
		curr = curr->next;
	}
	return (count);
}

t_stack	*find_lowest_n(t_stack *stack)
{
	t_stack	*lowest;

	lowest = stack;
	while (stack != NULL)
	{
		if (lowest->index > stack->index)
			lowest = stack;
		stack = stack->next;
	}
	return (lowest);
}

t_stack	*find_biggest_n(t_stack *stack)
{
	t_stack	*biggest;

	biggest = stack;
	while (stack != NULL)
	{
		if (biggest->index < stack->index)
			biggest = stack;
		stack = stack->next;
	}
	return (biggest);
}
