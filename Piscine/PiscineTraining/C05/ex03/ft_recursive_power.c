/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_recursive_power.c                               :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: roandrie <roandrie@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/07/22 09:59:23 by roandrie          #+#    #+#             */
/*   Updated: 2025/07/27 10:17:29 by roandrie         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdio.h>

int	ft_recursive_power(int nb, int power)
{
	if (power < 0)
		return (0);
	else if (power == 0)
		return (1);
	else
		return (nb * ft_recursive_power(nb, power - 1));
}
/*
int	main(int argc, char *argv[])
{
	if (argc == 3)
	{
		int nbr = atoi(argv[1]);
		int power = atoi(argv[2]);
		printf("%d\n", ft_recursive_power(nbr, power));
	}
	else
		printf("Erreur\n");
	return (0);
}*/