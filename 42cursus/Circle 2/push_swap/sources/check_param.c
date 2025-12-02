/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   check_param.c                                      :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: roandrie <roandrie@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/29 13:20:23 by roandrie          #+#    #+#             */
/*   Updated: 2025/12/02 18:19:26 by roandrie         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../include/push_swap.h"

static	int	check_double_number(t_data *data)
{
	t_stack	*curr;
	t_stack	*checker;

	curr = data->stack_a;
	while (curr != NULL)
	{
		checker = curr->next;
		while (checker != NULL)
		{
			if (curr->number == checker->number)
				return (1);
			checker = checker->next;
		}
		curr = curr->next;
	}
	return (0);
}

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

static	int	put_in_list(char *argv, t_data *data)
{
	t_stack	*node;
	long	n;

	if (check_valid_argv(argv) == 1)
		return (1);
	n = ft_atol(argv);
	if (n > INT_MAX || n < INT_MIN)
		return (1);
	node = ft_double_lstnew(n);
	if (node == NULL)
		return (1);
	ft_double_lstadd_back(&(data->stack_a), node);
	return (0);
}

static	int	convert_string(char *argv, t_data *data)
{
	char	**tab;
	int		i;
	int		error;

	i = 0;
	error = 0;
	tab = ft_split(argv, ' ');
	while (tab[i] != NULL)
	{
		if (put_in_list(tab[i], data) == 1)
			error = 1;
		i++;
	}
	i = 0;
	while (tab[i] != NULL)
		free (tab[i++]);
	free (tab);
	if (error == 1)
		return (1);
	return (0);
}

int	convert_argv(int argc, char **argv, t_data *data)
{
	int		i;

	i = 1;
	if (argc > 2)
	{
		while (argv[i] != NULL)
		{
			if (put_in_list(argv[i], data) == 1)
				return (1);
			i++;
		}
	}
	else
	{
		if (convert_string(argv[1], data) == 1)
			return (1);
	}
	if (check_double_number(data) == 1)
		return (1);
	return (0);
}
