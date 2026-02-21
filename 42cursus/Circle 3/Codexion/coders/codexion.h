/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   codexion.h                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: roandrie <roandrie@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/02/05 17:21:24 by roandrie          #+#    #+#             */
/*   Updated: 2026/02/21 16:34:04 by roandrie         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef CODEXION_H
# define CODEXION_H

// -------------------- //
//		INCLUDES		//
// -------------------- //

# include <stdio.h>
# include <pthread.h>
# include <stdlib.h>
# include <string.h>
# include <sys/time.h>
# include <unistd.h>

// -------------------- //
//		MACROS			//
// -------------------- //

// Errors message //
# define STR_ERR_MALLOC		"Could not allocate memory.\n"
# define STR_ERR_INV_ARG	"Invalid argument"

// Logs message //
# define LOG_TAKE_DONGLE	"[%lld] Coder %d has taken dongle %s\n"
# define LOG_COMPILING		"[%lld] Coder %d is compiling (%d)\n"
# define LOG_DEBUGGING		"[%lld] Coder %d is debugging\n"
# define LOG_REFACTOR		"[%lld] Coder %d is refactoring\n"
# define LOG_BURNS_OUT		"[%lld] Coder %d burned out\n"
# define LOG_SUCCESS		"All coders have compiled. They can rest... for now"

// Action //
# define ACT_TAKE		"takedongle"
# define ACT_COMP		"compile"
# define ACT_DEBUG		"debug"
# define ACT_REFAC		"refac"
# define ACT_BURNS		"burns_out"
# define REMOVE_QUEUE	"remove_q"
# define ADD_QUEUE		"add_q"

// Max coders //
# define MAX_CODERS 	300

// Scheduler //
# define FIFO			"fifo"
# define EDF			"edf"

// -------------------- //
//		STRUCTURES		//
// -------------------- //

typedef struct s_data			t_data;
typedef struct s_coder			t_coder;
typedef struct s_dongle			t_dongle;
typedef struct s_queue			t_queue;
typedef struct s_queue_manager	t_queue_manager;
typedef struct s_heap			t_heap;

typedef struct s_queue
{
	t_coder			*coder;
	struct s_queue	*next;
}					t_queue;

typedef struct s_queue_manager
{
	t_queue			*first;
	t_queue			*last;
	pthread_mutex_t	lock;
	pthread_cond_t	cond;
}					t_queue_manager;

typedef struct s_heap
{
	t_coder			*tree[MAX_CODERS];
	int				size;
	pthread_mutex_t	lock;
	pthread_cond_t	cond;
}					t_heap;

typedef struct s_coder
{
	t_data			*data;
	t_dongle		*left_dongle;
	t_dongle		*right_dongle;
	long long		time_bournout;
	int				id;
	int				code_compiled;
	int				have_finished;
	pthread_t		thread_id;
	pthread_mutex_t	mutex_burnout;
	pthread_mutex_t	mutex_finish;
}					t_coder;

typedef struct s_dongle
{
	t_data			*data;
	long long		cooldown;
	char			id[10];
	pthread_mutex_t	lock;
}					t_dongle;

typedef struct s_data
{
	t_coder			*coder;
	t_dongle		*dongle;
	t_heap			heap_control;
	t_queue_manager	queue_control;
	long long		burnout_max;
	long long		time_comp;
	long long		time_debug;
	long long		time_refac;
	long long		dongle_cooldown;
	long long		start_time;
	char			*scheduler;
	int				compile_required;
	int				nbr_coders;
	int				nbr_dongle;
	int				simulation_active;
	pthread_t		monitoring_id;
	pthread_mutex_t	mutex_print;
	pthread_mutex_t	mutex_simu;
}					t_data;

// -------------------- //
//		PROTOTYPES		//
// -------------------- //

// Parsing //
int				check_arg(t_data *data, char **arg);
int				init_struct(t_data *data);

// Threads, mutex management //
void			init_thread(t_data *data);
void			join_thread(t_data *data);
void			init_mutex(t_data *data);
void			destroy_mutex(t_data *data);

// Queue, heap management //
int				add_to_queue(t_queue_manager *manager, t_coder *coder_to_add);
int				remove_from_queue(t_queue_manager *manager);
void			heap_push(t_heap *manager, t_coder *coder);
void			heap_pop(t_heap *manager, t_coder *coder);

// Simulation //
void			*monitoring_simulation(void *arg);
void			*coder_thread(void *arg);
int				take_dongle(t_coder *coder);
int				try_take_dongle(t_dongle *dongle, t_data *data);
void			release_dongles(t_coder *coder, t_data *data);
int				scheduler_fifo(t_data *data, t_coder *coder, char *action);
void			scheduler_edf_add(t_data *data, t_coder *coder);

// Getter, Setter //
int				get_simulation(t_data *data);
long long		get_burnout(t_coder *coder);
void			set_burnout(t_coder *coder);
int				get_have_finished(t_coder *coder);
void			set_finished(t_coder *coder);

// Logs //
void			print_logs(int index, char *dongle_id, char *action,
					t_data *data);

// Functionalities //
long long		get_time_ms(void);
long long		get_sim_time(t_data *data);
int				is_fifo(t_data *data);
int				print_error(char *str, char *details, t_data *data);
void			free_memory(t_data *data);
char			*print_usage(void);

// Debug //
void			debug_print_struct(t_data *data);
void			debug_print_queue(t_queue_manager *manager);

#endif
