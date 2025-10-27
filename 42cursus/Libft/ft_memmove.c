/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_memmove.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: roandrie <roandrie@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/14 15:07:31 by roandrie          #+#    #+#             */
/*   Updated: 2025/10/27 12:59:44 by roandrie         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

void	*ft_memmove(void *dest, const void *src, size_t n)
{
	char		*pdest;
	const char	*psrc;

	pdest = dest;
	psrc = src;
	if (pdest == NULL && psrc == NULL)
		return (NULL);
	if (src < dest && src + n > dest)
	{
		psrc += n - 1;
		pdest += n - 1;
		while (n-- > 0)
			*pdest-- = *psrc--;
	}
	else
	{
		while (n-- > 0)
			*pdest++ = *psrc++;
	}
	return (dest);
}
