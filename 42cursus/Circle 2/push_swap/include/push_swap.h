/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   push_swap.h                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: roandrie <roandrie@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/29 12:37:22 by roandrie          #+#    #+#             */
/*   Updated: 2025/12/01 14:36:37 by roandrie         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef PUSH_SWAP_H
# define PUSH_SWAP_H

// ======================
//		COLORS
// ======================
# define RED 	"\e[1;91m"
# define GRN 	"\e[1;92m"
# define BLUE	"\e[1;94m"
# define R		"\e[0m"

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
//		PROTOTYPE
// ======================
//	Check Parameters
int		convert_argv(int argc, char **argv, t_data *data);
int		ft_compare(int a, int b);

// ======================
//		PROTOTYPE UTILS
// ======================
//	Functions to create Doubly Linked List
t_stack	*ft_double_lstnew(int content);
void	ft_double_lstadd_back(t_stack **lst, t_stack *node);
void	ft_double_lstclear(t_stack **stack);

//	Error gestion
int		ft_error(t_stack **stack_a, t_stack **stack_b);

#endif
