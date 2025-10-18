/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strcapitalize.c                                 :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: roandrie <roandrie@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/07/15 11:09:45 by roandrie          #+#    #+#             */
/*   Updated: 2025/07/29 11:25:48 by roandrie         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

void	str_lowcase(int i, char *str);

char	*ft_strcapitalize(char *str)
{
	int	i;
	int	newword;

	i = 0;
	newword = 1;
	str_lowcase(i, str);
	while (str[i] != '\0')
	{
		if (newword == 1)
		{
			if (str[i] >= 'a' && str[i] <= 'z')
				str[i] = str[i] - 32;
		}
		newword = 0;
		if ((str[i] >= 32 && str[i] <= 47) || (str[i] >= 58 && str[i] <= 64))
			newword = 1;
		else if ((str[i] >= 91 && str[i] <= 96))
			newword = 1;
		else if ((str[i] >= 123 && str[i] <= 126))
			newword = 1;
		i++;
	}
	return (str);
}

void	str_lowcase(int i, char *str)
{
	while (str[i] != '\0')
	{
		if (str[i] >= 'A' && str[i] <= 'Z')
			str[i] = str[i] + 32;
		i++;
	}
	i = 0;
}

/*
int main(void)
{
    char str[] = "SALUT c'est uNE phrase en MAjuscule (ou presque) !o7";
    char str2[] = "hi, how are you? 42words forty-two; fifty+and+one";
	printf("Avant: %s\n", str);
    printf("Apres: %s\n", ft_strcapitalize(str));
    printf("Avant: %s\n", str2);
    printf("Apres: %s\n", ft_strcapitalize(str2));
}*/
