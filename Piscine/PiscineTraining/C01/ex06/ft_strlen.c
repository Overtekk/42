/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strlen.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: roandrie <roandrie@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/07/29 09:47:20 by roandrie          #+#    #+#             */
/*   Updated: 2025/07/29 09:50:16 by roandrie         ###   ########.fr       */
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
#include <stdio.h>
int	main(int argc, char *argv[])
{
	if (argc == 2)
	{
		char *str = argv[1];
		int nbr = ft_strlen(str);
		printf("%d", nbr);
	}
	else
		printf("Erreur");
	return (0);
*/