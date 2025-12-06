/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   algo_utils.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: roandrie <roandrie@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/05 09:06:59 by roandrie          #+#    #+#             */
/*   Updated: 2025/12/06 19:50:39 by roandrie         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../../include/push_swap.h"

void	set_current_position(t_stack *stack)
{
	int		i;
	int		middle;

	i = 0;
	middle = (list_size(stack)) / 2;
	while (stack != NULL)
	{
		stack->pos = i;
		if (i <= middle)
			stack->middle = 1;
		else
			stack->middle = 0;
		stack = stack->next;
		i++;
	}
}

void	set_target_node_a(t_data *data)
{
	t_stack	*curr_a;
	t_stack	*curr_b;
	long	cmp;

	curr_a = data->stack_a;
	while (curr_a != NULL)
	{
		cmp = LONG_MIN;
		curr_a->target_node = NULL;
		curr_b = data->stack_b;
		while (curr_b != NULL)
		{
			if ((curr_b->index < curr_a->index) && (curr_b->index > cmp))
			{
				curr_a->target_node = curr_b;
				cmp = curr_b->index;
			}
			curr_b = curr_b->next;
		}
		if (curr_a->target_node == NULL)
			curr_a->target_node = find_biggest_n(data->stack_b);
		curr_a = curr_a->next;
	}
}

void	set_target_node_b(t_data *data)
{
	t_stack	*curr_a;
	t_stack	*curr_b;
	long	cmp;

	curr_b = data->stack_b;
	while (curr_b != NULL)
	{
		cmp = LONG_MAX;
		curr_b->target_node = NULL;
		curr_a = data->stack_a;
		while (curr_a != NULL)
		{
			if ((curr_a->index > curr_b->index) && (curr_a->index < cmp))
			{
				curr_b->target_node = curr_a;
				cmp = curr_a->index;
			}
			curr_a = curr_a->next;
		}
		if (curr_b->target_node == NULL)
			curr_b->target_node = find_lowest_n(data->stack_a);
		curr_b = curr_b->next;
	}
}

void	push_cost(t_stack *a, int size_a, int size_b)
{
	while (a != NULL)
	{
		if (a->middle == 1 && a->target_node->middle == 1)
		{
			if (a->pos > a->target_node->pos)
				a->push_cost = a->pos;
			else
				a->push_cost = a->target_node->pos;
		}
		else if (a->middle == 0 && a->target_node->middle == 0)
		{
			if ((size_a - a->pos) > (size_b - a->target_node->pos))
				a->push_cost = size_a - a->pos;
			else
				a->push_cost = size_b - a->target_node->pos;
		}
		else if (a->middle == 1 && a->target_node->middle == 0)
			a->push_cost = a->pos + (size_b - a->target_node->pos);
		else
			a->push_cost = (size_a - a->pos) + a->target_node->pos;
		a = a->next;
	}
}

t_stack	*find_cheapest(t_stack *stack)
{
	long	value;
	t_stack	*winner;

	value = LONG_MAX;
	winner = stack;
	while (stack != NULL)
	{
		if (stack->push_cost < value)
		{
			value = stack->push_cost;
			winner = stack;
		}
		stack->cheapest = 0;
		stack = stack->next;
	}
	winner->cheapest = 1;
	return (winner);
}
