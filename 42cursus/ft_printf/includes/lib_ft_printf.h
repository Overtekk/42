/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   lib_ft_printf.h                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: roandrie <roandrie@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/28 15:27:55 by roandrie          #+#    #+#             */
/*   Updated: 2025/10/28 16:13:58 by roandrie         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef LIB_FT_PRINTF_H
# define LIB_FT_PRINTF_H

#include <unistd.h>

int		ft_printf(const char *, ...);

// ## SRCS ## //
void	ft_putchar_fd(char c, int fd);

#endif
