/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_print_ptr.c                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: roandrie <roandrie@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/31 15:28:24 by roandrie          #+#    #+#             */
/*   Updated: 2025/11/29 13:43:08 by roandrie         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../include/libft.h"

static	int	ft_puthexa_ptr_fd(unsigned long int n, int fd)
{
	char	*base;
	int		i;

	i = 0;
	base = "0123456789abcdef";
	if (n >= 16)
	{
		i += ft_puthexa_ptr_fd(n / 16, fd);
		i += ft_puthexa_ptr_fd(n % 16, fd);
	}
	else
		i += ft_printchar(fd, base[n]);
	return (i);
}

int	ft_print_ptr(int fd, void *ptr)
{
	int	count_number;

	count_number = 0;
	if (ptr == NULL)
	{
		ft_putstr_fd("(nil)", fd);
		return (5);
	}
	count_number += ft_printstr(fd, "0x");
	count_number += ft_puthexa_ptr_fd((unsigned long int)ptr, fd);
	return (count_number);
}
