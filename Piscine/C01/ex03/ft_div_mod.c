/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_div_mod.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: roandrie <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/07/10 15:26:04 by roandrie          #+#    #+#             */
/*   Updated: 2025/07/10 16:19:35 by roandrie         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

void	ft_div_mod(int a, int b, int *div, int *mod)
{
	*div = a / b;
	*mod = a % b;
}
/*
int     main(void)
{ 
  int nbr1, nbr2, result, rest;
  int* div = &result;
  int* mod = &rest;
  
  nbr1 = 9; //Valeur 1
  nbr2 = 2; //Valeur 2
  
  ft_div_mod(nbr1, nbr2, div, mod);
  printf("Le resultat est : %d\n", result);
  printf("Le reste est : %d\n", rest);
}*/
