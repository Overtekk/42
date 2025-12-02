/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   rotate.c                                           :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: roandrie <roandrie@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/02 11:50:46 by roandrie          #+#    #+#             */
/*   Updated: 2025/12/02 17:22:26 by roandrie         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../../include/push_swap.h"

static	void	rotate(t_stack **stack)
{
	t_stack	*tmp;

	if (stack == NULL || *stack == NULL || (*stack)->next == NULL)
		return ;
	tmp = *stack;
	*stack = tmp->next;
	(*stack)->prev = NULL;
	ft_double_lstadd_back(stack, tmp);
}

void	ra(t_data *data)
{
	if (data == NULL || data->stack_a == NULL || data->stack_a->next == NULL)
		return ;
	rotate(&(data->stack_a));
	ft_printf(1, "ra\n");
}

void	rb(t_data *data)
{
	if (data == NULL || data->stack_b == NULL || data->stack_b->next == NULL)
		return ;
	rotate(&(data->stack_b));
	ft_printf(1, "rb\n");
}

void	rr(t_data *data)
{
	if (data == NULL)
		return ;
	if (data->stack_a != NULL && data->stack_a->next != NULL)
		rotate(&(data->stack_a));
	if (data->stack_b != NULL && data->stack_b->next != NULL)
		rotate(&(data->stack_b));
	ft_printf(1, "rr\n");
}
