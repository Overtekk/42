/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_printf.h                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: roandrie <roandrie@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/28 15:27:55 by roandrie          #+#    #+#             */
/*   Updated: 2025/10/30 12:50:50 by roandrie         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef FT_PRINTF_H
# define FT_PRINTF_H

#include "Libft/libft.h"
#include <unistd.h>
#include <stdlib.h>
#include <stdarg.h>
#include <stdio.h>

int		ft_printf(const char *, ...);
int		ft_printchar(int c);
int		ft_printstr(char *str);
int		ft_printnumber(int n);
int		ft_print_unsi_number(unsigned int n);

#endif
