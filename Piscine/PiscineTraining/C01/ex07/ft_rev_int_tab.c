/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_rev_int_tab.c                                   :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: roandrie <roandrie@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/07/29 09:50:34 by roandrie          #+#    #+#             */
/*   Updated: 2025/07/29 10:04:09 by roandrie         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

void	ft_rev_int_tab(int *tab, int size)
{
	int	i;
	int temp;

	i = 0;
	while (i < size / 2)
	{
		temp = tab[i];
		tab[i] = tab[(size - 1) - i];
		tab[(size - 1) - i] = temp;
		i++;
	}
}
/*
#include <stdio.h>
int	main(void)
{
	int	tab[10] = {0,1,2,3,4,5,6,7,8,9};
	int size = 10;
	int i = 0;
	ft_rev_int_tab(tab, size);
	while (i < 10)
	{
		printf("%d", tab[i]);
		i++;
	}
	return (0);
}*/