/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   clear_memory.c                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: roandrie <roandrie@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/09 10:39:28 by roandrie          #+#    #+#             */
/*   Updated: 2025/12/09 10:40:55 by roandrie         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../../include/push_swap.h"

int	clear_data(t_stack **stack_a, t_stack **stack_b)
{
	if (stack_a != NULL)
		ft_double_lstclear(stack_a);
	if (stack_b != NULL)
		ft_double_lstclear(stack_b);
	return (0);
}
