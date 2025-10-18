/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strchr.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: roandrie <roandrie@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/15 09:16:06 by roandrie          #+#    #+#             */
/*   Updated: 2025/10/17 14:13:55 by roandrie         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

char	*ft_strchr(const char *s, int c)
{
	const char	*p;

	p = s;
	while (*p != (char)c)
	{
		if (!*p)
			return (NULL);
		p++;
	}
	return ((char *)p);
}
