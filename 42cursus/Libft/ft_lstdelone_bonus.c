/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_lstdelone_bonus.c                               :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: roandrie <roandrie@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/24 10:32:40 by roandrie          #+#    #+#             */
/*   Updated: 2025/10/24 12:18:55 by roandrie         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

void	ft_lstdelone(t_list *lst, void (*del)(void *))
{
	(*del)(lst->content);
	free(lst);
}

void	ft_delete(void *)
{
	lst->content = NULL;
}

int main()
{
	t_list *list = NULL;
	t_list	*listcpy;
	t_list *elem1 = ft_lstnew("Un");
	t_list *elem2 = ft_lstnew("Deux");
	t_list *elem3 = ft_lstnew("Trois");
	t_list *elem4 = ft_lstnew("Quatre");
	ft_lstadd_front(&list, elem4);
	ft_lstadd_front(&list, elem3);
	ft_lstadd_front(&list, elem2);
	ft_lstadd_front(&list, elem1);
	listcpy = list;
	printf("Without Deleting\n");
	while (listcpy)
	{
		printf("%s\n", (char *)listcpy->content);
		listcpy = listcpy->next;
	}
	printf("\nWith Deleted node\n");
	ft_lstdelone(elem2, ft_delete);
	while (list)
	{
		printf("%s\n", (char *)list->content);
		list = list->next;
	}
	free (elem1);
	free (elem2);
	free (elem3);
	free (elem4);
}
