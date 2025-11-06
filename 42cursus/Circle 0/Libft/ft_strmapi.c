/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strmapi.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: roandrie <roandrie@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/20 16:28:27 by roandrie          #+#    #+#             */
/*   Updated: 2025/10/21 11:00:09 by roandrie         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

char	*ft_strmapi(char const *s, char (*f)(unsigned int, char))
{
	unsigned int	i;
	size_t			len;
	char			*nstring;

	len = ft_strlen(s);
	nstring = malloc(len + 1);
	if (!nstring)
		return (NULL);
	i = 0;
	while (s[i])
	{
		nstring[i] = (*f)(i, s[i]);
		i++;
	}
	nstring[i] = 0;
	return (nstring);
}
