/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_split.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: roandrie <roandrie@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/21 14:02:11 by roandrie          #+#    #+#             */
/*   Updated: 2025/10/24 10:15:00 by roandrie         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

static int	ft_count_words(char const *s, char c)
{
	int	i;
	int	wordcount;

	i = 0;
	wordcount = 0;
	while (*s)
	{
		if (*s != c && i == 0)
		{
			wordcount++;
			i = 1;
		}
		if (*s == c)
			i = 0;
		s++;
	}
	return (wordcount);
}

static void	*ft_free_all(char **tab)
{
	int	i;

	i = 0;
	while (tab[i])
	{
		free (tab[i]);
		i++;
	}
	free (tab);
	return (NULL);
}

static char	*ft_fill_tab(char const *s, char c)
{
	size_t	len;

	len = 0;
	while (s[len] && s[len] != c)
		len++;
	return (ft_substr(s, 0, len));
}

char	**ft_split(char const *s, char c)
{
	char		**tab;
	size_t		wordcount;
	size_t		i;

	if (!s)
		return (NULL);
	wordcount = ft_count_words(s, c);
	tab = malloc(sizeof(char *) * (wordcount + 1));
	if (!tab)
		return (NULL);
	i = 0;
	while (i < wordcount)
	{
		while (*s == c)
			s++;
		tab[i] = ft_fill_tab(s, c);
		if (!tab[i])
			return (ft_free_all(tab));
		while (*s && *s != c)
			s++;
		i++;
	}
	tab[i] = 0;
	return (tab);
}
