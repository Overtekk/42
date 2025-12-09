/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   check_order.c                                      :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: roandrie <roandrie@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/02 17:57:25 by roandrie          #+#    #+#             */
/*   Updated: 2025/12/02 18:15:43 by roandrie         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../include/push_swap.h"

int	is_already_sort(t_data *data)
{
	t_stack	*curr;

	curr = data->stack_a;
	while (curr != NULL)
	{
		if (curr->next == NULL)
			break ;
		if (curr->number > curr->next->number)
			return (0);
		curr = curr->next;
	}
	return (1);
}
