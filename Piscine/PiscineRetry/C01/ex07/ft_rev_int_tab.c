/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_rev_int_tab.c                                   :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: roandrie <roandrie@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/07/11 11:12:12 by roandrie          #+#    #+#             */
/*   Updated: 2025/07/14 13:36:51 by roandrie         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <unistd.h>

void	ft_rev_int_tab(int *tab, int size)
{
	int	temp;
	int	i;

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
int     main(void)
{ 
    int tab[10] = {0,1,2,3,4,5,6,7,8,9}; //Nombres a inverser
	int	size = 10;
	int i = 0;
    ft_rev_int_tab(tab, size);
	while (i < 10)
	{
		printf("%d", tab[i]);
		i++;
	}
}*/
