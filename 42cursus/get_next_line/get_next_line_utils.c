/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   get_next_line_utils.c                              :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: roandrie <roandrie@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/27 10:26:54 by roandrie          #+#    #+#             */
/*   Updated: 2025/11/03 15:22:11 by roandrie         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "get_next_line.h"

size_t	ft_strlen(const char *s)
{
	int	i;

	i = 0;
	while (s[i])
		i++;
	return (i);
}

char	*ft_strdup(const char *s)
{
	size_t	len;
	char	*dup;
	int		i;

	i = 0;
	len = ft_strlen(s);
	dup = malloc(len + 1);
	if (dup == NULL)
		return (NULL);
	while (s[i])
	{
		dup[i] = s[i];
		i++;
	}
	dup[i] = 0;
	return (dup);
}

char	*ft_substr(char const *s, unsigned int start, size_t len)
{
	size_t		i;
	size_t		size;
	char		*subs;

	if (!s)
		return (NULL);
	if (start >= (unsigned int)ft_strlen(s))
		return (ft_strdup(""));
	size = ft_strlen(s + start);
	if (size < len)
		len = size;
	subs = malloc(len + 1);
	if (!subs)
		return (NULL);
	i = 0;
	while ((unsigned int)len > i)
	{
		subs[i] = s[start + i];
		i++;
	}
	subs[i] = 0;
	return (subs);
}

char	*ft_strjoin(char const *s1, char const *s2)
{
	char		*nstring;
	char		*ptr;
	size_t		lens1;
	size_t		lens2;

	if (!s1 || !s2)
		return (NULL);
	lens1 = ft_strlen(s1);
	lens2 = ft_strlen(s2);
	nstring = malloc((lens1 + lens2) + 1);
	if (!nstring)
		return (NULL);
	ptr = nstring;
	while (*s1)
		*ptr++ = *s1++;
	while (*s2)
		*ptr++ = *s2++;
	*ptr = 0;
	return (nstring);
}

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
