/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_print_unsi_number.c                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: roandrie <roandrie@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/30 12:13:54 by roandrie          #+#    #+#             */
/*   Updated: 2025/10/30 13:01:27 by roandrie         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_printf.h"

static	void	ft_putnbr_unsigned_fd(unsigned int n, int fd)
{
	if (n >= 10)
	{
		ft_putnbr_unsigned_fd(n / 10, fd);
		ft_putnbr_unsigned_fd(n % 10, fd);
	}
	else
		ft_putchar_fd(n + 48, fd);
}

int	ft_print_unsi_number(unsigned int n)
{
	int	count_numbers;
	int	n_copy;

	count_numbers = 0;
	n_copy = n;
	if (n == 0)
		count_numbers++;
	else if (n_copy < 0)
		count_numbers = 10;
	else
	{
		while (n_copy != 0)
		{
			n_copy = n_copy / 10;
			count_numbers++;
		}
	}
	ft_putnbr_unsigned_fd(n, 1);
	return (count_numbers);
}
