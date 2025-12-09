/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_atol.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: roandrie <roandrie@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/29 21:26:29 by roandrie          #+#    #+#             */
/*   Updated: 2025/12/09 10:58:41 by roandrie         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../include/libft.h"

long	ft_atol(const char *nptr)
{
	int		sign;
	long	result;

	sign = 1;
	result = 0;
	while ((*nptr >= 9 && *nptr <= 13) || *nptr == 32)
		nptr++;
	if (*nptr == '-')
	{
		sign = -1;
		nptr++;
	}
	else if (*nptr == '+')
		nptr++;
	while (*nptr >= '0' && *nptr <= '9')
	{
		result = (result * 10) + (*nptr - '0');
		if (result > 2147483648)
			return (result * sign);
		nptr++;
	}
	return (result * sign);
}
