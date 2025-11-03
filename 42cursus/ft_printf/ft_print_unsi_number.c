/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_print_unsi_number.c                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: roandrie <roandrie@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/30 12:13:54 by roandrie          #+#    #+#             */
/*   Updated: 2025/11/03 11:00:48 by roandrie         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_printf.h"

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

static	void	ft_putnbr_unsigned_fd(unsigned int n)
{
	if (n >= 10)
	{
		ft_putnbr_unsigned_fd(n / 10);
		ft_putnbr_unsigned_fd(n % 10);
	}
	else
		ft_putchar_fd((n + 48), 1);
}

int	ft_print_unsi_number(unsigned int n)
{
	int	count_number;

	count_number = ft_count_unsigned_number(n);
	ft_putnbr_unsigned_fd(n);
	return (count_number);
}
