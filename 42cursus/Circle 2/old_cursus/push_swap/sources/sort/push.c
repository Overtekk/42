/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   push.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: roandrie <roandrie@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/02 10:22:13 by roandrie          #+#    #+#             */
/*   Updated: 2025/12/02 17:22:02 by roandrie         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../../include/push_swap.h"

static	void	push(t_stack **dest, t_stack **src)
{
	t_stack	*tmp;

	if (src == NULL || *src == NULL)
		return ;
	tmp = *src;
	*src = (*src)->next;
	if (*src != NULL)
		(*src)->prev = NULL;
	ft_double_lstadd_front(dest, tmp);
}

void	pa(t_stack **a, t_stack **b)
{
	push(a, b);
	ft_printf(1, "pa\n");
}

void	pb(t_stack **a, t_stack **b)
{
	push(b, a);
	ft_printf(1, "pb\n");
}
