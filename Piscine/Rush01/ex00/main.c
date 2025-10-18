/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   main.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: vilecali <vilecali@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/07/20 20:37:30 by vilecali          #+#    #+#             */
/*   Updated: 2025/07/20 22:38:38 by vilecali         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <unistd.h>

int		fill(int grid[4][4], int x, int y, int argvi[4][4]);
void	affichage(int grid[4][4]);

void	ft_convert(int argvi[4][4], char **argv)
{
	int	i;
	int	four;
	int	count;

	i = 0;
	count = 0;
	four = 0;
	while (argv[1][i])
	{
		if (count == 4)
		{
			four++;
			count = 0;
		}
		if (argv[1][i] >= '1' && argv[1][i] <= '9')
		{
			argvi[four][count] = argv[1][i] - '0';
			count++;
		}
		i++;
	}
}

int	ft_intput(char **argv)
{
	int	i;

	i = 0;
	while (argv[1][i])
	{
		if (!(argv[1][i] >= '1' && argv[1][i] <= '4') && argv[1][i] != ' ')
		{
			write(1, "ERREUR", 6);
			return (0);
		}
		i++;
	}
	if (i != 31)
	{
		write(1, "ERREUR", 6);
		return (0);
	}
	return (1);
}

int	main(int argc, char *argv[])
{
	int	grid[4][4];
	int	argvi[4][4];

	if (argc < 2)
	{
		write(1, "ERREUR veuillez saisir une seule chaine de caractere", 52);
		return (0);
	}
	if (ft_intput(argv) == 0)
		return (0);
	ft_convert(argvi, argv);
	if (fill(grid, 0, 0, argvi))
		affichage(grid);
	return (0);
}
