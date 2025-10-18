/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strcmp.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: roandrie <roandrie@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/07/16 09:35:06 by roandrie          #+#    #+#             */
/*   Updated: 2025/07/21 15:36:44 by roandrie         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdio.h> 

int	ft_strcmp(char *s1, char *s2)
{
	int	i;

	i = 0;
	while (s1[i] == s2[i] && s1[i] != '\0' && s2[i] != '\0')
	{
		i++;
	}
	return (s1[i] - s2[i]);
}
/*
int     main(void)
{ 
	char	str1[] = "ABC"; 
	char	str2[] = "ABC";
	printf("'%s'", str1);
	printf(" and '%s'", str2);
	printf(" %d\n", ft_strcmp(str1, str2));
}*/