/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_printnumber.c                                   :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: roandrie <roandrie@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/30 10:34:30 by roandrie          #+#    #+#             */
/*   Updated: 2025/10/30 11:37:23 by roandrie         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_printf.h"

int	ft_printnumber(int n)
{
	int	count_numbers;
	int	n_copy;

	count_numbers = 0;
	n_copy = n;
	if (n == 0)
		count_numbers++;
	while (n_copy != 0)
	{
		n_copy = n_copy / 10;
		count_numbers++;
	}
	ft_putnbr_fd(n, 1);
	return (count_numbers);
}
