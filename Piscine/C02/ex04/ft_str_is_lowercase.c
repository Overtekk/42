/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_str_is_lowercase.c                              :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: roandrie <roandrie@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/07/14 16:48:09 by roandrie          #+#    #+#             */
/*   Updated: 2025/07/14 16:49:18 by roandrie         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

int	ft_str_is_lowercase(char *str)
{
	int	i;

	i = 0;
	while (str[i] != '\0')
	{
		if (str[i] < 'a' || str[i] > 'z')
		{
			return (0);
		}
		i++;
	}
	return (1);
}
/*
int main(void)
{
    printf("oyeye: %d\n", ft_str_is_lowercase("oyeye"));
    printf("Oh1cailloux: %d\n", ft_str_is_lowercase("Oh1cailloux"));
    printf("jesuisgentil: %d\n", ft_str_is_lowercase("jesuisgentil"));
    printf("0: %d\n", ft_str_is_lowercase("0"));
    printf("Ehehe#: %d\n", ft_str_is_lowercase("Ehehe#"));
    printf(": %d\n", ft_str_is_lowercase(""));
}*/