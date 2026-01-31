/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_printnumber.c                                   :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: roandrie <roandrie@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/30 10:34:30 by roandrie          #+#    #+#             */
/*   Updated: 2025/11/29 13:40:45 by roandrie         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../include/libft.h"

static	int	ft_count_number(int n)
{
	int	count_number;

	count_number = 0;
	if (n == 0)
		return (1);
	else
	{
		if (n < 0)
			count_number++;
		while (n != 0)
		{
			n = n / 10;
			count_number++;
		}
	}
	return (count_number);
}

int	ft_printnumber(int fd, int n)
{
	int	count_number;

	count_number = ft_count_number(n);
	ft_putnbr_fd(n, fd);
	return (count_number);
}
