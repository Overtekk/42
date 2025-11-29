/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   list_management.c                                  :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: roandrie <roandrie@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/29 18:16:11 by roandrie          #+#    #+#             */
/*   Updated: 2025/11/29 21:43:02 by roandrie         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../../include/push_swap.h"

t_stack	*ft_double_lstnew(int content)
{
	t_stack	*new_node;

	new_node = malloc(sizeof(t_stack));
	if (new_node == NULL)
	{
		ft_printf(2, RED"Error\nMalloc Failed when creating node \n"R);
		return (NULL);
	}
	new_node->number = content;
	new_node->next = NULL;
	new_node->prev = NULL;
	new_node->index = 0;
	return (new_node);
}

void	ft_double_lstadd_back(t_stack **lst, t_stack *node)
{
	t_stack	*tmp;

	if (*lst == NULL)
	{
		*lst = node;
		return ;
	}
	tmp = *lst;
	while (tmp->next != NULL)
		tmp = tmp->next;
	node->next = NULL;
	node->prev = tmp;
	tmp->next = node;
}

void	ft_double_lstclear(t_stack **stack)
{
	t_stack	*tmp;
	t_stack	*current;

	if (stack == NULL)
		return ;
	current = *stack;
	while (current != NULL)
	{
		tmp = current->next;
		free (current);
		current = tmp;
	}
	*stack = NULL;
}
