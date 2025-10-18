/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_str_is_printable.c                              :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: roandrie <roandrie@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/07/14 16:56:57 by roandrie          #+#    #+#             */
/*   Updated: 2025/07/14 17:07:02 by roandrie         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

int	ft_str_is_printable(char *str)
{
	int	i;

	i = 0;
	while (str[i] != '\0')
	{
		if (str[i] < 32 || str[i] > 126)
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
    printf("OYEYE: %d\n", ft_str_is_printable("OYEYE"));
    printf("Oh1cailloux: %d\n", ft_str_is_printable("Oh1cailloux"));
    printf("jesuisgentil: %d\n", ft_str_is_printable("jesuisgentil"));
    printf("0: %d\n", ft_str_is_printable("0"));
    printf("EHEHE: %d\n", ft_str_is_printable("EHEHE"));
}*/