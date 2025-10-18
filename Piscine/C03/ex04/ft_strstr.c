/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strstr.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: roandrie <roandrie@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/07/30 11:56:32 by roandrie          #+#    #+#             */
/*   Updated: 2025/07/30 13:53:25 by roandrie         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

char	*ft_strstr(char *str, char *tp_find)
{
	int	i;

	i = 0;
	str[i] = tp_find[i];
	while (str[i] != '\0')
	{
		i++;
	}
	return (str);
}

#include <stdio.h>
int	main(void)
{
	char	str[] = "oh, tu as une jolie maison";
	char	tp_find[] = "une";
	ft_strstr(str, tp_find);
	printf("%s\n", str);
	return (0);
}