/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_printstr.c                                      :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: roandrie <roandrie@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/30 09:41:13 by roandrie          #+#    #+#             */
/*   Updated: 2025/11/29 13:34:20 by roandrie         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../include/libft.h"

int	ft_printstr(int fd, char *str)
{
	int	len;

	if (str == NULL)
	{
		ft_putstr_fd("(null)", fd);
		return (6);
	}
	len = ft_strlen(str);
	ft_putstr_fd(str, fd);
	return (len);
}
