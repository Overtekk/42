/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   reverse_rotate.c                                   :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: roandrie <roandrie@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/02 14:49:51 by roandrie          #+#    #+#             */
/*   Updated: 2025/12/02 15:16:16 by roandrie         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../../include/push_swap.h"

static	void	reverse_rotate(t_stack **stack)
{
	t_stack	*tmp;
	t_stack	*tmp_last;

	if (stack == NULL || *stack == NULL || (*stack)->next == NULL)
		return ;
	tmp_last = get_last_node(*stack);
	tmp = tmp_last->prev;
	tmp->next = NULL;
	ft_double_lstadd_front(stack, tmp_last);
}

void	rra(t_data *data)
{
	if (data == NULL || data->stack_a == NULL || data->stack_a->next == NULL)
		return ;
	reverse_rotate(&(data->stack_a));
	ft_printf(1, BLUE"rra\n"R);
}

void	rrb(t_data *data)
{
	if (data == NULL || data->stack_b == NULL || data->stack_b->next == NULL)
		return ;
	reverse_rotate(&(data->stack_b));
	ft_printf(1, BLUE"rrb\n"R);
}

void	rrr(t_data *data)
{
	if (data == NULL)
		return ;
	if (data->stack_a != NULL && data->stack_a->next != NULL)
		reverse_rotate(&(data->stack_a));
	if (data->stack_b != NULL && data->stack_b->next != NULL)
		reverse_rotate(&(data->stack_b));
	ft_printf(1, BLUE"rrr\n"R);
}
