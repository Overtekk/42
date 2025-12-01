/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   swap.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: roandrie <roandrie@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/01 15:25:07 by roandrie          #+#    #+#             */
/*   Updated: 2025/12/01 16:17:11 by roandrie         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../../include/push_swap.h"

static	void	swap(t_stack **stack)
{
	t_stack	*first;
	t_stack	*second;
	t_stack	*third;

	if (stack == NULL || *stack == NULL || (*stack)->next == NULL)
		return ;
	first = *stack;
	second = (*stack)->next;
	third = (*stack)->next->next;
	*stack = second;
	second->prev = NULL;
	second->next = first;
	first->prev = second;
	first->next = third;
	if (third != NULL)
		third->prev = first;
}

void	sa(t_data *data)
{
	swap(&(data->stack_a));
	ft_printf(1, "sa\n");
}

void	sb(t_data *data)
{
	swap(&(data->stack_b));
	ft_printf(1, "sb\n");
}

void	ss(t_data *data)
{
	sa(data);
	sb(data);
	ft_printf(1, "ss\n");
}
