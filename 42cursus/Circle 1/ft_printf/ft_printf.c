/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_printf.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: roandrie <roandrie@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/28 15:53:22 by roandrie          #+#    #+#             */
/*   Updated: 2025/11/03 10:33:31 by roandrie         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_printf.h"

int	ft_check_sign(char str, va_list args)
{
	int	print_chars;

	print_chars = 0;
	if (str == 'c')
		print_chars += ft_printchar((va_arg(args, int)));
	else if (str == 's')
		print_chars += ft_printstr((va_arg(args, char *)));
	else if (str == 'd' || str == 'i')
		print_chars += ft_printnumber((va_arg(args, int)));
	else if (str == 'p')
		print_chars += ft_print_ptr((va_arg(args, void *)));
	else if (str == 'u')
		print_chars += ft_print_unsi_number((va_arg(args, unsigned int)));
	else if (str == 'x' || str == 'X')
		print_chars += ft_print_hexa((va_arg(args, unsigned int)), str);
	else if (str == '%')
		print_chars += ft_printchar('%');
	return (print_chars);
}

int	ft_printf(const char *str, ...)
{
	va_list		args;
	int			count;
	int			i;

	va_start (args, str);
	count = 0;
	i = 0;
	while (str[i] != '\0')
	{
		if (str[i] == '%')
			count += ft_check_sign(str[++i], args);
		else
			count += ft_printchar(str[i]);
		i++;
	}
	va_end (args);
	return (count);
}
