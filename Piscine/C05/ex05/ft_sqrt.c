/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_sqrt.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: roandrie <roandrie@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/07/27 10:18:19 by roandrie          #+#    #+#             */
/*   Updated: 2025/07/30 14:38:55 by roandrie         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

int	ft_sqrt(int nb)
{
	int	mult;

	mult = 1;
	if (nb < 0)
		return (0);
	while ((mult * mult) <= nb && mult < 46340)
	{
		if ((mult * mult) == nb)
			return (mult);
		mult++;
	}
	return (0);
}
/*
#include <stdio.h>
int	main(void)
{
	int nbr = 8;
	printf("%d\n", ft_sqrt(nbr));
	return (0);
}*/