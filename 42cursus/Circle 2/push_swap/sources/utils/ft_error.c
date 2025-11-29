/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_error.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: roandrie <roandrie@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/29 21:58:33 by roandrie          #+#    #+#             */
/*   Updated: 2025/11/29 22:09:31 by roandrie         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../../include/push_swap.h"

int	ft_error(t_stack **stack_a, t_stack **stack_b)
{
	if (stack_a != NULL)
		ft_double_lstclear(stack_a);
	if (stack_b != NULL)
		ft_double_lstclear(stack_b);
	ft_putstr_fd(RED"Error\n"R, 2);
	return (1);
}
