/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_ultimate_div_mod.c                              :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: roandrie <roandrie@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/07/28 16:29:20 by roandrie          #+#    #+#             */
/*   Updated: 2025/07/28 16:35:24 by roandrie         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

void	ft_ultimate_div_mod(int *a, int *b)
{
	int	div;
	int	mod;

	div = *a / *b;
	mod = *a % *b;

	*a = div;
	*b = mod;
}

/*
#include <stdio.h>
#include <stdlib.h>
int	main(int argc, char *argv[])
{
	if (argc == 3)
	{
		int		nb = atoi(argv[1]);
		int 	nb2 = atoi(argv[2]);
		ft_ultimate_div_mod(&nb, &nb2);
		printf("Division de %d et %d = %d\n", nb, nb2, nb);
		printf("Modulo de %d et %d = %d\n", nb, nb2, nb2);
	}
	else
		printf("Erreur");
	return (0);
}*/