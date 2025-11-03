/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   get_next_line.c                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: roandrie <roandrie@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/27 10:26:13 by roandrie          #+#    #+#             */
/*   Updated: 2025/11/03 15:54:31 by roandrie         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "get_next_line.h"

char	*clear_buffer(char *large_buffer)
{
	char	*new_buffer;
	int		i;

	i = 0;
	while (large_buffer[i] != '\n')
		i++;
	new_buffer = large_buffer;
	return (new_buffer);
}

char	*fill_line(char *large_buffer)
{
	char	*line;
	int		i;

	i = 0;
	while (large_buffer[i] != '\n')
		i++;
	line = ft_substr(large_buffer, 0, i);
	line[i] = '\n';
	return (line);
}

char	*read_line(int fd, char *large_buffer)
{
	char	*buffer_read;
	int		byte_read;

	buffer_read = malloc(sizeof(char) * BUFFER_SIZE + 1);
	if (buffer_read == NULL)
		return (NULL);
	byte_read = 1;
	while (byte_read > 0)
	{
		byte_read = read(fd, buffer_read, BUFFER_SIZE);
		if (byte_read <= -1)
			return (NULL);
		large_buffer = buffer_read;
		if (ft_strchr(large_buffer, '\n'))
			break ;
	}
	return (large_buffer);
}

char	*get_next_line(int fd)
{
	static char	*large_buffer;
	char		*line;

	if (ft_strchr(large_buffer, '\n') == NULL)
		large_buffer = read_line(fd, large_buffer);

	line = fill_line(large_buffer);
	large_buffer = clear_buffer(large_buffer);
	return (line);
}
