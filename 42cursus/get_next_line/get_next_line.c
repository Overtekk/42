/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   get_next_line.c                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: roandrie <roandrie@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/27 10:26:13 by roandrie          #+#    #+#             */
/*   Updated: 2025/10/28 14:15:03 by roandrie         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "get_next_line.h"
#include <stdio.h>


char	*get_next_line(int fd)
{
	static char	*str;
	char	buffer[BUFFER_SIZE + 1];
	int		byte;

	byte = 1;
	str = (char *)malloc(sizeof(char *) * BUFFER_SIZE);
	if (!str)
		return (NULL);
	byte = read(fd, buffer, BUFFER_SIZE);
	if (byte > 0)
	{
		str = buffer;
		return (str);
	}
	return (NULL);
}
/*
char	*get_next_line(int fd)
{
	char	*str;
	int		buff;

	str = malloc(8);
	buff = 0;
	buff = read(fd, str, 8);
	if (buff > 0)
		return (str);
	return (NULL);
}*/

