/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_swap.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: roandrie <roandrie@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/07/10 12:55:46 by roandrie          #+#    #+#             */
/*   Updated: 2025/07/16 09:21:33 by roandrie         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

void	ft_swap(int *a, int *b)
{
	int	swap;
	int	swapt;

	swap = *a;
	swapt = *b;
	*a = swapt;
	*b = swap;
}
/*
int     main(void)
{ 
  
  int val1 = 10;
  int val2 = 100;
  int* p1 = &val1;
  int* p2 = &val2;
  
  printf("Valeur 1 actuelle %d\n", val1);
  printf("Valeur 2 actuelle %d\n", val2);
  printf("\n");
  printf("HOP LE SWAP");
  printf("\n");
  ft_swap(p1, p2);
  printf("Valeur 1 nouvelle %d\n", val1);
  printf("Valeur 2 nouvelle %d\n", val2);
}*/
