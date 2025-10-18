/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strlen.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: roandrie <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/07/11 10:42:36 by roandrie          #+#    #+#             */
/*   Updated: 2025/07/11 10:45:33 by roandrie         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

int	ft_strlen(char *str)
{
	int	i;

	i = 0;
	while (str[i] != '\0')
	{
		i++;
	}
	return (i);
}
/*
int     main(void)
{ 
  char str[] = "Rooomaiiin"; //Texte a compter
  int i = ft_strlen(str);
  printf("%d", i);
  return 0;
}*/
