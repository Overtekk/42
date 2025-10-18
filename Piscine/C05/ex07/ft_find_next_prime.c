/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_find_next_prime.c                               :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: roandrie <roandrie@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/07/30 09:52:59 by roandrie          #+#    #+#             */
/*   Updated: 2025/07/30 14:40:20 by roandrie         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

int	ft_is_prime(int nb)
{
	int	i;

	i = 3;
	if (nb <= 1)
		return (0);
	if (nb == 2)
		return (1);
	if ((nb % 2) == 0)
		return (0);
	while (i * i <= nb)
	{
		if (nb % i == 0)
			return (0);
		i += 2;
	}
	return (1);
}

int	ft_find_next_prime(int nb)
{
	int	next_prime;

	next_prime = nb;
	nb = ft_is_prime(nb);
	if (nb == 1)
		return (next_prime);
	else
	{
		while (nb != 1)
		{
			next_prime++;
			nb = ft_is_prime(next_prime);
		}
		return (next_prime);
	}
}
/*
#include <stdio.h>
int	main(void)
{
	int nbr = 7;
	printf("%d\n", ft_find_next_prime(nbr));
	return (0);
}*/