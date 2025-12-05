/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   push_swap.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: roandrie <roandrie@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/04 17:50:12 by roandrie          #+#    #+#             */
/*   Updated: 2025/12/05 09:20:17 by roandrie         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../include/push_swap.h"

void	sort_all(t_data *data)
{
	pb(&(data->stack_a), &(data->stack_b));
	pb(&(data->stack_a), &(data->stack_b));
	set_current_position(data->stack_a);
	set_current_position(data->stack_b);
}
