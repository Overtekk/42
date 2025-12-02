/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   main.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: roandrie <roandrie@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/29 12:36:59 by roandrie          #+#    #+#             */
/*   Updated: 2025/12/02 15:11:12 by roandrie         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../include/push_swap.h"

static	void	temp_print(t_data *data)
{
	t_stack	*curr;

	curr = data->stack_a;
	ft_printf(1, "\nStack A:\n");
	while (curr != NULL)
	{
		ft_printf(1, "[%d] ", curr->number);
		curr = curr->next;
	}
	ft_printf(1, "\nStack B:\n");
	curr = data->stack_b;
	while (curr != NULL)
	{
		ft_printf(1, "[%d] ", curr->number);
		curr = curr->next;
	}
	ft_printf(1, "\n");
}

int	main(int argc, char **argv)
{
	t_data	data;

	if (argc < 2)
		return (1);
	data.stack_a = NULL;
	data.stack_b = NULL;
	if (convert_argv(argc, argv, &data) == 1)
		return (ft_error(&(data.stack_a), NULL));
	temp_print(&(data));
	pb(&(data.stack_a), &(data.stack_b));
	pb(&(data.stack_a), &(data.stack_b));
	pb(&(data.stack_a), &(data.stack_b));
	temp_print(&(data));
	rra(&(data));
	temp_print(&(data));
	ft_double_lstclear(&(data.stack_a));
	ft_double_lstclear(&(data.stack_b));
	return (0);
}
