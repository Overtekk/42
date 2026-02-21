/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   exit.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: roandrie <roandrie@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/02/06 11:29:15 by roandrie          #+#    #+#             */
/*   Updated: 2026/02/21 15:31:43 by roandrie         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "codexion.h"

void	free_memory(t_data *data);

/**
 * Prints a custom error message to the standard error output and free memory.
 */

int	print_error(char *str, char *details, t_data *data)
{
	if (data != NULL)
		free_memory(data);
	fprintf(stderr, "ERROR: %s", str);
	if (details != NULL)
		fprintf(stderr, " (%s)", details);
	fprintf(stderr, "\n");
	return (1);
}

/**
 * Free memory of structure if there are not empty.
 */

void	free_memory(t_data *data)
{
	t_queue	*curr;
	t_queue	*next;

	curr = data->queue_control.first;
	if (data->coder != NULL)
		free(data->coder);
	if (data->dongle != NULL)
		free(data->dongle);
	while (curr != NULL)
	{
		next = curr->next;
		free(curr);
		curr = next;
	}
}

/**
 * Print a custom message used to tell the user how to launch the program.
 */

char	*print_usage(void)
{
	return ("Invalid arguments. Use:\n./codexion <number_of_coders> "
		"<time_to_burnout> <time_to_compile> <time_to_debug> <time_to_refactor>"
		" <number_of_compiles_required> <dongle_cooldown> <scheduler>");
}
