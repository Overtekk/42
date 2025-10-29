/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_printf.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: roandrie <roandrie@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/28 15:53:22 by roandrie          #+#    #+#             */
/*   Updated: 2025/10/29 15:23:51 by roandrie         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_printf.h"

int	ft_check_sign(char *str, va_list args, int count)
{
	int	i;

	i = 0;
	if (str[i] == 'c')
		count += ft_printchar((va_arg(args, int)));
	return (count);
}

int	ft_printf(const char *format, ...)
{
	va_list		args;
	char		*str;
	int			count;
	int			i;

	va_start (args, format);
	str = ft_strdup(format);
	count = 0;
	i = 0;
	while (str[i] != '\0')
	{
		count += ft_printchar(str[i]);
		if (str[i] == '%')
			ft_check_sign(&str[++i], args, count);
		i++;
	}
	va_end (args);
	free (str);
	return (count);
}
