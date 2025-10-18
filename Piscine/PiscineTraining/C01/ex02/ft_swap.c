/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_swap.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: roandrie <roandrie@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/07/28 15:46:22 by roandrie          #+#    #+#             */
/*   Updated: 2025/07/28 16:05:53 by roandrie         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

void	ft_swap(int *a, int *b)
{
	int	temp;
	
	temp = *b;
	*b = *a;
	*a = temp;
}
/*
#include <stdio.h>
#include <stdlib.h>
int	main(int argc, char *argv[])
{
	if (argc == 3)
	{
		int	a = atoi(argv[1]);
		int b = atoi (argv[2]);
		int* val1 = &a;
		int* val2 = &b;
		printf("%d ", a);
		printf("%d \ndeviennent\n", b);
		ft_swap(val1, val2);
		printf("%d ", a);
		printf("%d\n", b);
	}
	else
		printf("Erreur");
	return (0);
}*/