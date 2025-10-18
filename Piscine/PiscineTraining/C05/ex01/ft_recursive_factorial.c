/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_recursive_factorial.c                           :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: roandrie <roandrie@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/07/22 08:53:58 by roandrie          #+#    #+#             */
/*   Updated: 2025/07/27 10:16:56 by roandrie         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdio.h>

int	ft_recursive_factorial(int nb)
{
	if (nb == 0)
		return (1);
	else if (nb < 0)
		return (0);
	else
		return (nb * ft_recursive_factorial(nb - 1));
}
/*
int	main(int argc, char *argv[])
{
	if (argc == 2)
	{
		int nbr = atoi(argv[1]);
		printf("%d\n", ft_recursive_factorial(nbr));
	}
	else
		printf("Erreur\n");
	return (0);
}*/