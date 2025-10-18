/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_sort_int_tab.c                                  :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: roandrie <roandrie@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/07/29 09:59:37 by roandrie          #+#    #+#             */
/*   Updated: 2025/07/29 11:15:05 by roandrie         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

int	ft_strcmp(int *s1, int *s2)
{
	int	i;

	i = 0;
	if ((s1[i] == s2[i]) && (s1[i] != '\0' && s2[i] != '\0'))
	{
		i++;
	}
	return (s1[i] - s2[i]);
}

void	ft_swap(int *s1, int *s2)
{
	int	temp;

	temp = *s2;
	*s2 = *s1;
	*s1 = temp;
}

void	ft_sort_int_tab(int *tab, int size)
{
	int	i;

	i = 0;
	while (i < size)
	{
		if (ft_strcmp(&tab[i], &tab[i + 1]) > 0)
		{
			ft_swap (&tab[i], &tab[i + 1]);
			i = 0;
		}
		else
			i++;
	}
}
/*
#include <stdio.h>
int	main(void)
{
	int tab[10] = {9,3,5,0,1,7,8,6,2,4};
	int size = 10;
	int i = 0;
	ft_sort_int_tab(tab, size);
	while (i < size)
	{
		printf("%d ", tab[i]);
		i++;
	}
	return (0);
}*/