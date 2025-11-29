/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   check_param.c                                      :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: roandrie <roandrie@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/29 13:20:23 by roandrie          #+#    #+#             */
/*   Updated: 2025/11/29 22:11:10 by roandrie         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../include/push_swap.h"

static	int	check_valid_argv(char *str)
{
	int	i;

	i = 0;
	if (str[i] == '\0')
		return (1);
	if (str[i] == '-' || str[i] == '+')
		i++;
	if (str[i] == '\0')
		return (1);
	while (str[i] != '\0')
	{
		if (str[i] >= '0' && str[i] <= '9')
			i++;
		else
			return (1);
	}
	return (0);
}

int	convert_argv(int argc, char **argv, t_data *data)
{
	t_stack	*node;
	long	n;
	int		i;

	i = 1;
	if (argc > 2)
	{
		while (argv[i] != NULL)
		{
			if (check_valid_argv(argv[i]) == 1)
				return (1);
			n = ft_atol(argv[i]);
			if (n > INT_MAX || n < INT_MIN)
				return (1);
			node = ft_double_lstnew(n);
			if (node == NULL)
				return (1);
			ft_double_lstadd_back(&(data->stack_a), node);
			i++;
		}
	}
	return (0);
}
