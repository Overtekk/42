/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   push.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: roandrie <roandrie@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/02 10:22:13 by roandrie          #+#    #+#             */
/*   Updated: 2025/12/02 11:42:27 by roandrie         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../../include/push_swap.h"

static	void	push(t_stack **dest, t_stack **src)
{
	t_stack	*tmp_src;

	if (src == NULL || *src == NULL)
		return ;
	tmp_src = *src;
	*src = (*src)->next;
	if (*src != NULL)
		(*src)->prev = NULL;
	if (*dest == NULL)
	{
		*dest = tmp_src;
		(*dest)->prev = NULL;
		(*dest)->next = NULL;
	}
	else
	{
		(*dest)->prev = tmp_src;
		tmp_src->next = (*dest);
		*dest = tmp_src;
		(*dest)->prev = NULL;
	}
}

void	pa(t_stack **a, t_stack **b)
{
	push(a, b);
	ft_printf(1, BLUE"pa\n"R);
}

void	pb(t_stack **a, t_stack **b)
{
	push(b, a);
	ft_printf(1, BLUE"pb\n"R);
}
