/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_lstclear_bonus.c                                :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: roandrie <roandrie@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/25 16:32:25 by roandrie          #+#    #+#             */
/*   Updated: 2025/10/25 17:31:38 by roandrie         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

void	ft_lstclear(t_list **lst, void (*del)(void *))
{
	t_list	*lst_cpy;
	t_list	*temp;

	lst_cpy = *lst;
	while (lst_cpy != NULL)
	{
		temp = lst_cpy->next;
		ft_lstdelone(lst_cpy, del);
		lst_cpy = temp;
	}
	*lst = NULL;
}
