/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   debug.c                                            :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: roandrie <roandrie@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/02 17:26:08 by roandrie          #+#    #+#             */
/*   Updated: 2025/12/05 10:09:50 by roandrie         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../../include/push_swap.h"

// ** Put debug_print(&(data)); where you want to see the stacks ** //

static	void	print_stack_a(t_data *data)
{
	t_stack	*curr;

	curr = data->stack_a;
	ft_printf(1, "\nStack A:\n");
	while (curr != NULL)
	{
		ft_printf(1, "[%d] ", curr->number);
		if (curr->next == NULL)
			ft_printf(1, "[NULL]");
		curr = curr->next;
	}
}

static	void	print_stack_b(t_data *data)
{
	t_stack	*curr;

	curr = data->stack_b;
	ft_printf(1, "\nStack B:\n");
	while (curr != NULL)
	{
		ft_printf(1, "[%d] ", curr->number);
		if (curr->next == NULL)
			ft_printf(1, " [NULL]");
		curr = curr->next;
	}
}

static	void	print_index_a(t_data *data)
{
	t_stack	*curr;

	curr = data->stack_a;
	while (curr != NULL)
	{
		ft_printf(1, "<%d> ", curr->index);
		curr = curr->next;
	}
}

static	void	print_index_b(t_data *data)
{
	t_stack	*curr;

	curr = data->stack_b;
	while (curr != NULL)
	{
		ft_printf(1, "<%d> ", curr->index);
		curr = curr->next;
	}
}

void	debug_print(t_data *data)
{
	print_stack_a(data);
	ft_printf(1, "\n");
	print_index_a(data);
	ft_printf(1, "\n");
	print_stack_b(data);
	ft_printf(1, "\n");
	print_index_b(data);
	ft_printf(1, "\n----------------------\n");
}
