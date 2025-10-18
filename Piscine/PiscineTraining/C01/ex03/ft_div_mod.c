/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_div_mod.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: roandrie <roandrie@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/07/28 16:06:08 by roandrie          #+#    #+#             */
/*   Updated: 2025/07/28 16:29:08 by roandrie         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

void	ft_div_mod(int a, int b, int *div, int *mod)
{
	*div = a / b;
	*mod = a % b;
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
		int resultdiv, resultmod;
		int*	div = &resultdiv;
		int*	mod = &resultmod;
		ft_div_mod(nb, nb2, div, mod);
		printf("Division de %d et %d = %d\n", nb, nb2, resultdiv);
		printf("Modulo de %d et %d = %d\n", nb, nb2, resultmod);
	}
	else
		printf("Erreur");
	return (0);
}*/