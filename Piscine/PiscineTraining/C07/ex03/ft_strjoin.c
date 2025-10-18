/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strjoin.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: roandrie <roandrie@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/07/28 10:02:36 by roandrie          #+#    #+#             */
/*   Updated: 2025/07/28 11:09:01 by roandrie         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdio.h>
#include <stdlib.h>

int	ft_strlen(char *str)
{
	int	i;

	i = 0;
	while(str[i] != '\0')
	{
		if (str[i] == 32)
			return (i);
		i++;
	}
	return (i);
}

char	*ft_strjoin(int size, char **strs, char *sep)
{
	int	i;
	int	*tab;

	i = 0;
	tab = (char *)malloc(sizeof(char) * (taille + 1));
	while (strs[i] != '\0')
	{
		ft_strlen(strs);
	}
	return (strs);
}

int	main(void)
{
	int size = 6;
	char str[] = {"bonjour", "les", "amis", "comment", "ca", "va"};
	char sep = ",";
	int p;
	p = ft_strjoin(size, str, sep);
	printf(ft_strjoin(size, str, sep));
	free (p);
	return (0);
}