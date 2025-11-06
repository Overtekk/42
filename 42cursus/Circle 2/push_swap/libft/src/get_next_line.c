/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   get_next_line.c                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: roandrie <roandrie@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/27 10:26:13 by roandrie          #+#    #+#             */
/*   Updated: 2025/11/05 16:44:04 by roandrie         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "get_next_line.h"
#include <stdio.h>

static	char	*clear_buffer(char *large_buffer)
{
	char	*new_buffer;
	int		i;
	int		len;

	i = 0;
	len = ft_strlen(large_buffer);
	while (large_buffer[i] != '\n' && large_buffer[i] != '\0')
		i++;
	if (large_buffer[i] == '\0')
		new_buffer = ft_strdup("");
	else
		new_buffer = ft_substr(large_buffer, (i + 1), (len - i));
	free (large_buffer);
	return (new_buffer);
}

static	char	*fill_line(char *large_buffer)
{
	char	*line;
	int		i;

	i = 0;
	while (large_buffer[i] != '\n' && large_buffer[i] != '\0')
		i++;
	if (large_buffer[i] == '\0')
		line = ft_substr(large_buffer, 0, i);
	else
		line = ft_substr(large_buffer, 0, (i + 1));
	return (line);
}

static	char	*free_buffers(char *large_buffer, char *buffer_read)
{
	free (large_buffer);
	free (buffer_read);
	return (NULL);
}

static	char	*read_line(int fd, char *large_buffer)
{
	char	*buffer_read;
	char	*temp_buffer;
	int		byte_read;

	buffer_read = malloc(sizeof(char) * BUFFER_SIZE + 1);
	if (buffer_read == NULL)
		return (NULL);
	byte_read = 1;
	while (byte_read > 0)
	{
		byte_read = read(fd, buffer_read, BUFFER_SIZE);
		if (byte_read <= -1)
		{
			return (free_buffers(buffer_read, large_buffer));
		}
		buffer_read[byte_read] = '\0';
		temp_buffer = large_buffer;
		large_buffer = ft_strjoin(temp_buffer, buffer_read);
		free (temp_buffer);
		if (ft_strchr(large_buffer, '\n'))
			break ;
	}
	free (buffer_read);
	return (large_buffer);
}

char	*get_next_line(int fd)
{
	static char	*large_buffer;
	char		*line;

	if (fd < 0 || BUFFER_SIZE <= 0)
		return (NULL);
	if (large_buffer == NULL)
		large_buffer = ft_strdup("");
	if (!ft_strchr(large_buffer, '\n'))
		large_buffer = read_line(fd, large_buffer);
	if (large_buffer == NULL)
		return (NULL);
	if (*large_buffer == '\0')
	{
		free (large_buffer);
		large_buffer = NULL;
		return (NULL);
	}
	line = fill_line(large_buffer);
	large_buffer = clear_buffer(large_buffer);
	return (line);
}
