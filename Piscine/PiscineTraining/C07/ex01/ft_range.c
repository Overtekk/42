/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_range.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: roandrie <roandrie@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/07/31 10:07:00 by roandrie          #+#    #+#             */
/*   Updated: 2025/07/31 10:25:16 by roandrie         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdlib.h>
#include <stdio.h>

int	*ft_range(int min, int max)
{
	int	i;
	int	*tab;

	i = 0;
	if (min >= max)
	{
		tab = NULL;
		return (0);
	}
	tab = (int *)malloc(sizeof(int) * (max - min));
	while (max > min)
	{
		tab[i] = min;
		i++;
		min++;
	}
	return (tab);
}

int	main(void)
{
	int	i = 0;;
	int min = 0;
	int max = 9;
	int *tab = ft_range(min, max);
	if (tab == NULL)
	{
		printf("NULL");
		return (0);
	}
	while (max > min)
	{
		printf("%d ", tab[i]);
		i++;
		min++;
	}
	free (tab);
	return (0);
}