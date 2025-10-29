/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_itoa.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: roandrie <roandrie@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/20 11:57:52 by roandrie          #+#    #+#             */
/*   Updated: 2025/10/20 16:11:23 by roandrie         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

static char	*ft_reverse(char *temp, int len)
{
	char	*s;
	int		j;

	j = 0;
	s = malloc(sizeof(char) * (len + 1));
	if (!s)
		return (NULL);
	while (--len >= 0)
	{
		s[j] = temp[len];
		j++;
	}
	s[j] = 0;
	return (s);
}

char	*ft_itoa(int n)
{
	char	temp[12];
	int		sign;
	int		i;

	i = 0;
	sign = 1;
	if (n == 0)
	{
		temp[i++] = 0 + '0';
		return (ft_reverse(temp, i));
	}
	if (n < 0)
		sign *= -1;
	while (n != 0)
	{
		temp[i] = ((n % 10) * sign + '0');
		n = n / 10;
		i++;
	}
	if (sign == -1)
		temp[i++] = '-';
	return (ft_reverse(temp, i));
}
