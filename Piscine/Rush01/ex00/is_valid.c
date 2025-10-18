/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   is_valid.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: vilecali <vilecali@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/07/19 12:19:56 by reazzouz          #+#    #+#             */
/*   Updated: 2025/07/20 20:36:51 by vilecali         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

int	verif_col_top(int grind[4][4], int argvi[4][4])
{
	int	k;
	int	j;
	int	n_max;
	int	count_view;

	k = 0;
	while (k < 4)
	{
		n_max = 0;
		count_view = 0;
		j = 0;
		while (j < 4)
		{
			if (grind[j][k] > n_max)
			{
				n_max = grind[j][k];
				count_view++;
			}
			j++;
		}
		if (argvi[0][k] != count_view)
			return (0);
		k++;
	}
	return (1);
}

int	verif_col_bottom(int grind[4][4], int argvi[4][4])
{
	int	k;
	int	j;
	int	n_max;
	int	count_view;

	k = 0;
	while (k < 4)
	{
		n_max = 0;
		count_view = 0;
		j = 3;
		while (j >= 0)
		{
			if (grind[j][k] > n_max)
			{
				n_max = grind[j][k];
				count_view++;
			}
			j--;
		}
		if (argvi[1][k] != count_view)
			return (0);
		k++;
	}
	return (1);
}

int	verif_row_left(int grind[4][4], int argvi[4][4])
{
	int	j;
	int	k;
	int	highest;
	int	count;

	j = 0;
	while (j < 4)
	{
		highest = 0;
		count = 0;
		k = 0;
		while (k < 4)
		{
			if (grind[j][k] > highest)
			{
				highest = grind[j][k];
				count++;
			}
			k++;
		}
		if (argvi[2][j] != count)
			return (0);
		j++;
	}
	return (1);
}

int	verif_row_right(int grind[4][4], int argvi[4][4])
{
	int	j;
	int	k;
	int	highest;
	int	count;

	j = 0;
	while (j < 4)
	{
		highest = 0;
		count = 0;
		k = 3;
		while (k >= 0)
		{
			if (grind[j][k] > highest)
			{
				highest = grind[j][k];
				count++;
			}
			k--;
		}
		if (count != argvi[3][j])
			return (0);
		j++;
	}
	return (1);
}

int	is_valid(int grind[4][4], int argvi[4][4])
{
	if (verif_col_bottom(grind, argvi) && verif_col_top(grind, argvi))
	{
		if (verif_row_left(grind, argvi) && verif_row_right(grind, argvi))
			return (1);
	}
	return (0);
}
