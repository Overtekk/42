/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_is_negative.c                                   :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: roandrie <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/07/09 16:46:03 by roandrie          #+#    #+#             */
/*   Updated: 2025/07/10 08:58:26 by roandrie         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <unistd.h>

void	ft_is_negative(int n)
{
	char	p;
	char	nn;

	p = 'P';
	nn = 'N';
	if (n >= 0)
	{
		write(1, &p, 1);
	}
	else
	{
		write(1, &nn, 1);
	}
}
/*
int main()
{
    ft_is_negative(-1000);

    return 0;
}*/
