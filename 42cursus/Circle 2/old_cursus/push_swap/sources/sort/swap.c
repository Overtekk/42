/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   swap.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: roandrie <roandrie@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/01 15:25:07 by roandrie          #+#    #+#             */
/*   Updated: 2025/12/02 17:22:35 by roandrie         ###   ########.fr       */
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
	if (data == NULL || data->stack_a == NULL || data->stack_a->next == NULL)
		return ;
	swap(&(data->stack_a));
	ft_printf(1, "sa\n");
}

void	sb(t_data *data)
{
	if (data == NULL || data->stack_b == NULL || data->stack_b->next == NULL)
		return ;
	swap(&(data->stack_b));
	ft_printf(1, "sb\n");
}

void	ss(t_data *data)
{
	if (data == NULL)
		return ;
	if (data->stack_a != NULL && data->stack_a->next != NULL)
		swap(&(data->stack_a));
	if (data->stack_b != NULL && data->stack_b->next != NULL)
		swap(&(data->stack_b));
	ft_printf(1, "ss\n");
}
