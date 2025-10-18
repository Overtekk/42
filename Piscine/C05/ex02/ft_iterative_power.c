/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_iterative_power.c                               :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: roandrie <roandrie@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/07/22 09:30:47 by roandrie          #+#    #+#             */
/*   Updated: 2025/07/30 14:37:43 by roandrie         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

int	ft_iterative_power(int nb, int power)
{
	int	result;

	result = 1;
	if (power < 0)
		return (0);
	if (nb == 0)
		return (1);
	if (nb > 0)
	{
		while (power > 0)
		{
			result *= nb;
			power--;
		}
	}
	return (result);
}
/*
#include <stdio.h>
int	main(void)
{
	int nbr = 8;
	int power = 2;
	printf("%d\n", ft_iterative_power(nbr, power));
	return (0);
}*/