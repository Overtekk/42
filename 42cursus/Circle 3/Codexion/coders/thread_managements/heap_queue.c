/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   heap_queue.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: roandrie <roandrie@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/02/20 08:31:51 by roandrie          #+#    #+#             */
/*   Updated: 2026/02/21 16:07:34 by roandrie         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "codexion.h"

static void	heap_check_deadline(t_heap	*manager, int i);
static int	heap_compare(t_coder *curr_coder, t_coder *coder);
static void	heap_swap(t_coder **tree, int i, int j);

/**
 * Adds a coder to the heap priority queue.
 *
 * Inserts the new coder at the end of the tree, then pull up the coder by
 * swapping it with its parent until the coder with the earliest deadline is at
 * the top of the tree.
 */

void	heap_push(t_heap *manager, t_coder *coder)
{
	int	i;

	i = manager->size;
	manager->tree[i] = coder;
	manager->size += 1;
	while (i > 0)
	{
		if (heap_compare(manager->tree[i], manager->tree[(i - 1) / 2]))
		{
			heap_swap(manager->tree, i, (i - 1) / 2);
			i = (i - 1) / 2;
		}
		else
			break ;
	}
}

/**
 * Removes a specific coder from the queue.
 *
 * Finds the coder in the tree, replaces it with the last element of the heap,
 * decreases the size, and then restores the heap property by either pull it up
 * or pull down the replacement element.
 */

void	heap_pop(t_heap *manager, t_coder *coder)
{
	int	i;

	i = 0;
	while (i < manager->size)
	{
		if (manager->tree[i] == coder)
			break ;
		i++;
	}
	if (i == manager->size)
		return ;
	manager->size--;
	manager->tree[i] = manager->tree[manager->size];
	while (i > 0 && heap_compare(manager->tree[i], manager->tree[(i - 1) / 2]))
	{
		heap_swap(manager->tree, i, (i - 1) / 2);
		i = (i - 1) / 2;
	}
	heap_check_deadline(manager, i);
}

/**
 * Maintains the queue property by shifting an element down the tree.
 *
 * Compares the current element with its children. If a child has a more urgent
 * deadline, the elements are swapped. This process continues down the branches.
 */

static void	heap_check_deadline(t_heap	*manager, int i)
{
	int	left;
	int	right;
	int	smallest;

	while ((i * 2) + 1 < manager->size)
	{
		left = (i * 2) + 1;
		right = (i * 2) + 2;
		smallest = left;
		if (right < manager->size && heap_compare(manager->tree[right],
				manager->tree[left]))
		{
			smallest = right;
		}
		if (heap_compare(manager->tree[smallest], manager->tree[i]))
		{
			heap_swap(manager->tree, i, smallest);
			i = smallest;
		}
		else
			break ;
	}
}

/**
 * Compares two coders based on their burnout deadlines.
 *
 * Evaluates which of the two coders has the earliest burnout time to determine
 * their priority in the min-heap.
 *
 * Return 1 if the current coder has an earlier deadline, 0 otherwise.
 */

static int	heap_compare(t_coder *curr_coder, t_coder *coder)
{
	return (get_burnout(curr_coder) < get_burnout(coder));
}

/**
 * Swaps the position of two coders in the heap array
 */

static	void	heap_swap(t_coder **tree, int i, int j)
{
	t_coder	*temp;

	temp = tree[i];
	tree[i] = tree[j];
	tree[j] = temp;
}
