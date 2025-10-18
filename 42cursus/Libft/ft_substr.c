/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_substr.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: roandrie <roandrie@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/17 10:44:29 by roandrie          #+#    #+#             */
/*   Updated: 2025/10/17 15:27:19 by roandrie         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

char	*ft_substr(char const *s, unsigned int start, size_t len)
{
	size_t		i;
	size_t		j;
	char		*subs;

	i = 0;
	j = 0;
	if (!s)
		return (NULL);
	if (start > ft_strlen(s))
		return (ft_strdup(""));
	subs = malloc(len + 1);
	if (!subs)
		return (NULL);
	while (start > i)
		i++;
	while (len > j)
	{
		subs[j] = s[i];
		i++;
		j++;
	}
	subs[j] = 0;
	return (subs);
}
