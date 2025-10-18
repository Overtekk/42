/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_ultimate_div_mod.c                              :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: roandrie <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/07/10 15:15:26 by roandrie          #+#    #+#             */
/*   Updated: 2025/07/10 17:02:19 by roandrie         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

void	ft_ultimate_div_mod(int *a, int *b)
{
	int	tempdiv;
	int	tempmod;

	tempdiv = *a / *b;
	tempmod = *a % *b;
	*a = tempdiv;
	*b = tempmod;
}
/*
int     main(void)
{ 
  int nbr1 = 9; //Valeur 1
  int nbr2 = 2; //Valeur 2
  
  
  ft_ultimate_div_mod(&nbr1, &nbr2);
  printf("Le resultat est : %d\n", nbr1);
  printf("Le reste est : %d\n", nbr2);
}*/
