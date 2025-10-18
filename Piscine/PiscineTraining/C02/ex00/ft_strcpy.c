/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strcpy.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: roandrie <roandrie@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/07/29 15:12:10 by roandrie          #+#    #+#             */
/*   Updated: 2025/07/29 15:36:40 by roandrie         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

char	*ft_strcpy(char *dest, char *src)
{
	int	i;

	i = 0;
	while (src[i] != '\0')
	{
		dest[i] = src[i];
		i++;
	}
	dest[i] = '\0';
	return (dest);
}

#include <stdio.h>
int	main(int argc, char *argv[])
{
	if (argc == 2)
	{
		char *src = argv[1];
		char dest[100];
		printf("%s\n", ft_strcpy(dest, src));
	}
	else
		printf("Erreur");
	return (0);
}