/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_print_unsi_number.c                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: roandrie <roandrie@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/30 12:13:54 by roandrie          #+#    #+#             */
/*   Updated: 2025/11/29 13:42:30 by roandrie         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../include/libft.h"

static	int	ft_count_unsigned_number(unsigned int n)
{
	int	count_number;

	count_number = 0;
	if (n == 0)
		return (1);
	else
	{
		while (n != 0)
		{
			n = n / 10;
			count_number++;
		}
	}
	return (count_number);
}

static	void	ft_putnbr_unsigned_fd(int fd, unsigned int n)
{
	if (n >= 10)
	{
		ft_putnbr_unsigned_fd(fd, (n / 10));
		ft_putnbr_unsigned_fd(fd, (n % 10));
	}
	else
		ft_putchar_fd((n + 48), fd);
}

int	ft_print_unsi_number(int fd, unsigned int n)
{
	int	count_number;

	count_number = ft_count_unsigned_number(n);
	ft_putnbr_unsigned_fd(fd, n);
	return (count_number);
}
