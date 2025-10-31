/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_print_hexa_lower.c                              :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: roandrie <roandrie@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/30 13:41:06 by roandrie          #+#    #+#             */
/*   Updated: 2025/10/31 13:25:29 by roandrie         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_printf.h"

void	ft_putchar_fd(char c, int fd)
{
	write(fd, &c, 1);
}

static	void	ft_puthexa_fd(unsigned int n, int fd)
{
	char	*base = "0123456789abcdef";
	int	count_hexa;

	if (n >= 16)
	{
		ft_puthexa_fd(n / 16, fd);
		ft_puthexa_fd(n % 16, fd);
	}
	else
	{
		ft_putchar_fd(base[n], fd);
		count_hexa++;
	}

	printf("\nCount = %d\n", count_hexa);
}

int	ft_print_hexa_lower(int n)
{
	int	count_hexa;

	count_hexa = 0;
	ft_puthexa_fd(n, 1);
	return (count_hexa);
}

#include <stdio.h>
int main()
{
	int n = 256;
	int	count = 0;

	count = ft_print_hexa_lower(n);
	printf("\n%d\n", count);
}
