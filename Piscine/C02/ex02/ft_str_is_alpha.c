/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_str_is_alpha.c                                  :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: roandrie <roandrie@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/07/14 15:33:24 by roandrie          #+#    #+#             */
/*   Updated: 2025/07/14 16:43:02 by roandrie         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

int	ft_str_is_alpha(char *str)
{
	int	i;

	i = 0;
	while (str[i] != '\0')
	{
		if (str[i] < 'a' || str[i] > 'z')
		{
			if (str[i] < 'A' || str[i] > 'Z')
			{
				return (0);
			}
		}
		i++;
	}
	return (1);
}
/*
int main(void)
{
    printf("OyeOye: %d\n", ft_str_is_alpha("OyeOye"));
    printf("Oh1cailloux: %d\n", ft_str_is_alpha("Oh1cailloux"));
    printf("Jesuisgentil: %d\n", ft_str_is_alpha("Jesuisgentil"));
    printf("0: %d\n", ft_str_is_alpha("0"));
    printf("Ehehe#: %d\n", ft_str_is_alpha("Ehehe#"));
    printf(": %d\n", ft_str_is_alpha(""));
}*/