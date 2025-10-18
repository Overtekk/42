/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_str_is_numeric.c                                :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: roandrie <roandrie@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/07/14 16:44:55 by roandrie          #+#    #+#             */
/*   Updated: 2025/07/14 16:46:40 by roandrie         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

int	ft_str_is_numeric(char *str)
{
	int	i;

	i = 0;
	while (str[i] != '\0')
	{
		if (str[i] < '0' || str[i] > '9')
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
    printf("OyeOye: %d\n", ft_str_is_numeric("OyeOye"));
    printf("Oh1cailloux: %d\n", ft_str_is_numeric("Oh1cailloux"));
    printf("Jesuisgentil: %d\n", ft_str_is_numeric("Jesuisgentil"));
    printf("0: %d\n", ft_str_is_numeric("0"));
    printf("Ehehe#: %d\n", ft_str_is_numeric("Ehehe#"));
    printf(": %d\n", ft_str_is_numeric(""));
}*/