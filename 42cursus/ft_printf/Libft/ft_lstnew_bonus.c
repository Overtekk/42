/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_lstnew_bonus.c                                  :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: roandrie <roandrie@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/23 09:35:51 by roandrie          #+#    #+#             */
/*   Updated: 2025/10/23 16:31:12 by roandrie         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

t_list	*ft_lstnew(void *content)
{
	t_list	*p_content;

	p_content = malloc(sizeof(t_list));
	if (!p_content)
		return (NULL);
	p_content->content = content;
	p_content->next = NULL;
	return (p_content);
}
