/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   push_swap.h                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: roandrie <roandrie@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/29 12:37:22 by roandrie          #+#    #+#             */
/*   Updated: 2025/12/04 11:15:31 by roandrie         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef PUSH_SWAP_H
# define PUSH_SWAP_H

// ======================
//		LIBRARY
// ======================
# include <unistd.h>
# include <stdlib.h>
# include <fcntl.h>
# include <stdio.h>
# include <string.h>
# include <limits.h>
# include "../libft/include/libft.h"

// ======================
//		STRUCTURE
// ======================

typedef struct s_stack
{
	int				number;
	int				index;
	struct s_stack	*next;
	struct s_stack	*prev;
}					t_stack;

typedef struct s_data
{
	t_stack			*stack_a;
	t_stack			*stack_b;
}					t_data;

// ======================
//	GENERAL PROTOTYPE
// ======================
//	Check Parameters
int		convert_argv(int argc, char **argv, t_data *data);
//	Init Index
void	init_index(t_data *data);
//	Check if sort is needed
int		is_already_sort(t_data *data);
//	Check what algo to use
int		check_numbers(t_data *data);

// ======================
//	PROTOTYPE UTILS
// ======================
//	Functions for Doubly Linked List
t_stack	*ft_double_lstnew(int content);
void	ft_double_lstadd_back(t_stack **lst, t_stack *node);
void	ft_double_lstadd_front(t_stack **lst, t_stack *node);
void	ft_double_lstclear(t_stack **stack);
t_stack	*get_last_node(t_stack *list);
size_t	list_size(t_stack *lst);
t_stack	*find_lowest_n(t_stack *stack);
t_stack	*find_biggest_n(t_stack *stack);

//	See stack if you need
void	debug_print(t_data *data);

// ======================
//	PROTOTYPE SORT OPTIONS
// ======================
//	Swap
void	sa(t_data *data);
void	sb(t_data *data);
void	ss(t_data *data);
//	Push
void	pa(t_stack **a, t_stack **b);
void	pb(t_stack **a, t_stack **b);
//	Rotate
void	ra(t_data *data);
void	rb(t_data *data);
void	rr(t_data *data);
//	Reverse Rotate
void	rra(t_data *data);
void	rrb(t_data *data);
void	rrr(t_data *data);

//	Error gestion
int		ft_error(t_stack **stack_a, t_stack **stack_b);

#endif
