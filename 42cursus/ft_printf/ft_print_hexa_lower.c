/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_print_hexa_lower.c                              :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: roandrie <roandrie@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/30 13:41:06 by roandrie          #+#    #+#             */
/*   Updated: 2025/10/31 15:20:59 by roandrie         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_printf.h"

static	int	ft_puthexa_lower_fd(unsigned int n, int fd)
{
	char	*base;
	int		i;

	i = 0;
	base = "0123456789abcdef";
	if (n >= 16)
	{
		i+= ft_puthexa_lower_fd(n / 16, fd);
		i+= ft_puthexa_lower_fd(n % 16, fd);
	}
	else
		i+= ft_printchar(base[n]);
	return (i);
}

static	int	ft_puthexa_upper_fd(unsigned int n, int fd)
{
	char	*base;
	int		i;

	i = 0;
	base = "0123456789ABCDEF";
	if (n >= 16)
	{
		i+= ft_puthexa_upper_fd(n / 16, fd);
		i+= ft_puthexa_upper_fd(n % 16, fd);
	}
	else
		i+= ft_printchar(base[n]);
	return (i);
}

int	ft_print_hexa(unsigned int n, char c)
{
	int	count_hexa;

	count_hexa = 0;
	if (c == 'x')
		count_hexa = ft_puthexa_lower_fd(n, 1);
	else
		count_hexa = ft_puthexa_upper_fd(n, 1);
	return (count_hexa);
}
