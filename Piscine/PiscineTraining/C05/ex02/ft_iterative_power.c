/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_iterative_power.c                               :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: roandrie <roandrie@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/07/22 09:30:47 by roandrie          #+#    #+#             */
/*   Updated: 2025/07/27 10:17:14 by roandrie         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdio.h>

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
int	main(int argc, char *argv[])
{
	if (argc == 3)
	{
		int nbr = atoi(argv[1]);
		int power = atoi(argv[2]);
		printf("%d\n", ft_iterative_power(nbr, power));
	}
	else
		printf("Erreur\n");
	return (0);
}*/