/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_sqrt.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: roandrie <roandrie@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/07/27 10:18:19 by roandrie          #+#    #+#             */
/*   Updated: 2025/07/27 10:28:19 by roandrie         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdio.h>
#include <stdlib.h>

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
int	main(int argc, char *argv[])
{
	if (argc == 2)
	{
		int nbr = atoi(argv[1]);
		printf("%d\n", ft_sqrt(nbr));
	}
	else
		printf("Erreur\n");
	return (0);
}*/