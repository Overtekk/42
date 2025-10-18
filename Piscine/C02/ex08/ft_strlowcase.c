/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strlowcase.c                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: roandrie <roandrie@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/07/15 11:06:28 by roandrie          #+#    #+#             */
/*   Updated: 2025/07/15 11:08:51 by roandrie         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

char	*ft_strlowcase(char *str)
{
	int	i;

	i = 0;
	while (str[i] != '\0')
	{
		if (str[i] >= 'A' && str[i] <= 'Z')
		{
			str[i] = str[i] + 32;
		}
		i++;
	}
	return (str);
}
/*
int main(void)
{
    char str[] = "coucou toi";
    char str2[] = "graou :)";
    char str3[] = "LA PISCINE";
    char str4[] = "Oh JE sUiS BiZZZ";
    printf("coucou toi => %s\n", ft_strlowcase(str));
    printf("graou :) => %s\n", ft_strlowcase(str2));
    printf("LA PISCINE => %s\n", ft_strlowcase(str3));
    printf("Oh JE sUiS BiZZZ => %s\n", ft_strlowcase(str4));
}*/