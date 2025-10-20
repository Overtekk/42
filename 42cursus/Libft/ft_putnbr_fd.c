/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_putnbr_fd.c                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: roandrie <roandrie@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/19 17:30:47 by roandrie          #+#    #+#             */
/*   Updated: 2025/10/20 14:52:43 by roandrie         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

void	ft_putnbr_fd(int n, int fd)
{
	int	sign;

	sign = 1;
	if (n < 0)
	{
		ft_putchar_fd('-', fd);
		sign = -sign;
	}
	if (n / 10)
	{
		ft_putnbr_fd((n / 10) * sign, fd);
		ft_putnbr_fd((n % 10) * sign, fd);
	}
	else
		ft_putchar_fd(((n * sign) + '0'), fd);
}
