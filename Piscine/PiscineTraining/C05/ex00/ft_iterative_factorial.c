/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_iterative_factorial.c                           :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: roandrie <roandrie@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/07/21 15:51:34 by roandrie          #+#    #+#             */
/*   Updated: 2025/07/27 10:16:36 by roandrie         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdio.h>

#include <stdio.h>
#include <stdlib.h>

int	ft_iterative_factorial(int nb)
{
	int	result;

	result = 1;
	if (nb < 0)
		return (0);
	if (nb == 0)
		return (1);
	while (nb > 0)
	{
		result *= nb;
		nb--;
	}
	return (result);
}
/*
int	main(int argc, char *argv[])
{
	if (argc == 2)
	{
		int nbr = atoi(argv[1]);
		printf("%d\n", ft_iterative_factorial(nbr));
	}
	else
		printf("Erreur\n");
	return (0);
}*/