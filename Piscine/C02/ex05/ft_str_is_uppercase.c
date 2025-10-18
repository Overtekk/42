/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_str_is_uppercase.c                              :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: roandrie <roandrie@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/07/14 16:50:17 by roandrie          #+#    #+#             */
/*   Updated: 2025/07/14 16:51:31 by roandrie         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

int	ft_str_is_uppercase(char *str)
{
	int	i;

	i = 0;
	while (str[i] != '\0')
	{
		if (str[i] < 'A' || str[i] > 'Z')
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
    printf("OYEYE: %d\n", ft_str_is_uppercase("OYEYE"));
    printf("Oh1cailloux: %d\n", ft_str_is_uppercase("Oh1cailloux"));
    printf("jesuisgentil: %d\n", ft_str_is_uppercase("jesuisgentil"));
    printf("0: %d\n", ft_str_is_uppercase("0"));
    printf("EHEHE: %d\n", ft_str_is_uppercase("EHEHE"));
    printf(": %d\n", ft_str_is_uppercase(""));
}*/