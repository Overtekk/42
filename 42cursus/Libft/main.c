/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   main.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: roandrie <roandrie@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/18 14:35:15 by roandrie          #+#    #+#             */
/*   Updated: 2025/10/19 16:16:57 by roandrie         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"
#include <stdio.h>

int	main()
{
	// ft_isalpha
	//test 1
	printf("--ft_isalpha--\n");
	int s_isalpha = 'a';
	if (ft_isalpha(s_isalpha))
		printf("(%c) Test 1: ok\n", s_isalpha);
	else
		printf("(%c) Test 1: failed\n", s_isalpha);
	//test 2
	s_isalpha = 'H';
	if (ft_isalpha(s_isalpha))
		printf("(%c) Test 2: ok\n", s_isalpha);
	else
		printf("(%c) Test 2: failed\n", s_isalpha);
	//test 3
	s_isalpha = '5';
	if (ft_isalpha(s_isalpha) == 0)
		printf("(%c) Test 3: ok\n", s_isalpha);
	else
		printf("(%c) Test 3: failed\n", s_isalpha);

	// ft_isdigit
	//test 1
	printf("--ft_isdigit--\n");
	int s_isdigit = '5';
	if (ft_isdigit(s_isdigit))
		printf("(%c) Test 1: ok\n", s_isdigit);
	else
		printf("(%c) Test 1: failed\n", s_isdigit);
	//test 2
	s_isdigit = 'j';
	if (ft_isdigit(s_isdigit) == 0)
		printf("(%c) Test 2: ok\n", s_isdigit);
	else
		printf("(%c) Test 2: failed\n", s_isdigit);

	// ft_isalnum
	//test 1
	printf("--ft_isalnum--\n");
	int s_isalnum = '5';
	if (ft_isalnum(s_isalnum))
		printf("(%c) Test 1: ok\n", s_isalnum);
	else
		printf("(%c) Test 1: failed\n", s_isalnum);
	//test 2
	s_isalnum = 'j';
	if (ft_isalnum(s_isalnum))
		printf("(%c) Test 2: ok\n", s_isalnum);
	else
		printf("(%c) Test 2: failed\n", s_isalnum);
	//test 3
	s_isalnum = '(';
	if (ft_isalnum(s_isalnum) == 0)
		printf("(%c) Test 3: ok\n", s_isalnum);
	else
		printf("(%c) Test 3: failed\n", s_isalnum);

	// ft_isascii
	//test 1
	printf("--ft_isascii--\n");
	int s_isascii = 127;
	if (ft_isascii(s_isascii))
		printf("(%d) Test 1: ok\n", s_isascii);
	else
		printf("(%d) Test 1: failed\n", s_isascii);
	//test 2
	s_isascii = 128;
	if (ft_isascii(s_isascii) == 0)
		printf("(%d) Test 2: ok\n", s_isascii);
	else
		printf("(%d) Test 2: failed\n", s_isascii);

	// ft_isprint
	//test 1
	printf("--ft_isprint--\n");
	int s_isprint = ' ';
	if (ft_isprint(s_isprint))
		printf("(%c) Test 1: ok\n", s_isprint);
	else
		printf("(%c) Test 1: failed\n", s_isprint);
	//test 2
	s_isprint = 'A';
	if (ft_isprint(s_isprint))
		printf("(%c) Test 2: ok\n", s_isprint);
	else
		printf("(%c) Test 2: failed\n", s_isprint);
	//test 3
	s_isprint = 31;
	if (ft_isprint(s_isprint) == 0)
		printf("(%c) Test 3: ok\n", s_isprint);
	else
		printf("(%c) Test 3: failed\n", s_isprint);

	// ft_strlen
	//test 1
	printf("--ft_strlen--\n");
	char *s_strlen = "Hello"; // 5
	if (ft_strlen(s_strlen) == 5)
		printf("(%s) Test 1: ok\n", s_strlen);
	else
		printf("(%s) Test 1: failed\n", s_strlen);
	//test 2
	s_strlen = "";
	if (ft_strlen(s_strlen) == 0)
		printf("(%s) Test 2: ok\n", s_strlen);
	else
		printf("(%s) Test 2: failed\n", s_strlen);

	// ft_memset / ft_bzero
	printf("--ft_memset / ft_bzero--\n");
	char s_memset[10];
	//test 1 ft_memset
	ft_memset(s_memset, 'A', 5);
	if (s_memset[0] == 'A' && s_memset[4] == 'A' && s_memset[5] != 'A')
		printf("ft_memset Test 1: ok\n");
	else
		printf("ft_memset Test 1: failed\n");
	//test 2 ft_bzero
	ft_bzero(s_memset, 5);
	if (s_memset[0] == 0 && s_memset[4] == 0)
		printf("ft_bzero Test 2: ok\n");
	else
		printf("ft_bzero Test 2: failed\n");

	// ft_memcpy
	printf("--ft_memcpy--\n");
	char src_memcpy[] = "ABCDEF";
	char dst_memcpy[10];
	//test 1
	ft_memcpy(dst_memcpy, src_memcpy, 4); // Copie ABCD
	if (dst_memcpy[0] == 'A' && dst_memcpy[3] == 'D' && dst_memcpy[4] != 'E')
		printf("ft_memcpy Test 1: ok\n");
	else
		printf("ft_memcpy Test 1: failed\n");
	//test 2
	ft_memcpy(dst_memcpy, src_memcpy, 0); // Copie 0 octet
	if (dst_memcpy[0] == 'A') // Vérifie que rien n'a bougé
		printf("ft_memcpy Test 2: ok\n");
	else
		printf("ft_memcpy Test 2: failed\n");

	// ft_memmove
	printf("--ft_memmove--\n");
	char buffer_memmove[] = "ABCDEFG";
	//test 1 (Chevauchement vers l'avant : src < dest)
	ft_memmove(buffer_memmove + 3, buffer_memmove, 4); // Copie ABCD à partir de G
	// Devrait donner ABCABCDG
	if (buffer_memmove[3] == 'A' && buffer_memmove[6] == 'D')
		printf("ft_memmove Test 1 (Avant): ok\n");
	else
		printf("ft_memmove Test 1 (Avant): failed\n");
	//test 2 (Chevauchement vers l'arrière : dest < src)
	char buffer_memmove2[] = "ABCDEFG";
	ft_memmove(buffer_memmove2, buffer_memmove2 + 3, 4); // Copie DEFG au début
	// Devrait donner DEFGDEFG
	if (buffer_memmove2[0] == 'D' && buffer_memmove2[3] == 'G')
		printf("ft_memmove Test 2 (Arriere): ok\n");
	else
		printf("ft_memmove Test 2 (Arriere): failed\n");

	// ft_strlcpy
	printf("--ft_strlcpy--\n");
	char src_lcpy[] = "Hello";
	char dst_lcpy[5];
	//test 1 (Troncature: besoin de 6, size=5)
	size_t ret_lcpy = ft_strlcpy(dst_lcpy, src_lcpy, 5);
	if (ret_lcpy == 5 && dst_lcpy[4] == '\0') // Doit retourner slen (5) et dst[4] doit être '\0'
		printf("ft_strlcpy Test 1 (Troncature): ok\n");
	else
		printf("ft_strlcpy Test 1 (Troncature): failed\n");
	//test 2 (Pas de troncature)
	ret_lcpy = ft_strlcpy(dst_lcpy, src_lcpy, 10);
	if (ret_lcpy == 5 && dst_lcpy[4] == 'o')
		printf("ft_strlcpy Test 2 (Complet): ok\n");
	else
		printf("ft_strlcpy Test 2 (Complet): failed\n");

	// ft_strlcat
	printf("--ft_strlcat--\n");
	char dst_lcat[10];
	strcpy(dst_lcat, "ABC"); // dlen = 3
	char src_lcat[] = "DEFG"; // slen = 4
	//test 1 (Concaténation totale)
	size_t ret_lcat = ft_strlcat(dst_lcat, src_lcat, 10); // dlen+slen = 7
	if (ret_lcat == 7 && strcmp(dst_lcat, "ABCDEFG") == 0)
		printf("ft_strlcat Test 1 (Complet): ok\n");
	else
		printf("ft_strlcat Test 1 (Complet): failed\n");
	//test 2 (Troncature)
	strcpy(dst_lcat, "ABC"); // reset dlen = 3
	ret_lcat = ft_strlcat(dst_lcat, src_lcat, 5); // size=5. Espace dispo = 5-3-1=1. Copie 'D'.
	if (ret_lcat == 7 && strcmp(dst_lcat, "ABCD") == 0) // Doit retourner 7, mais dst est tronqué
		printf("ft_strlcat Test 2 (Troncature): ok\n");
	else
		printf("ft_strlcat Test 2 (Troncature): failed\n");

	// ft_toupper / ft_tolower
	printf("--ft_toupper/ft_tolower--\n");
	//test 1 ft_toupper
	if (ft_toupper('a') == 'A' && ft_toupper('A') == 'A')
		printf("ft_toupper Test 1: ok\n");
	else
		printf("ft_toupper Test 1: failed\n");
	//test 2 ft_tolower
	if (ft_tolower('A') == 'a' && ft_tolower('a') == 'a')
		printf("ft_tolower Test 2: ok\n");
	else
		printf("ft_tolower Test 2: failed\n");

	// ft_strchr
	printf("--ft_strchr--\n");
	char *s_chr = "Hello World";
	//test 1 (Caractère trouvé)
	if (ft_strchr(s_chr, 'o') == &s_chr[4])
		printf("ft_strchr Test 1: ok\n");
	else
		printf("ft_strchr Test 1: failed\n");
	//test 2 (Caractère non trouvé)
	if (ft_strchr(s_chr, 'z') == NULL)
		printf("ft_strchr Test 2: ok\n");
	else
		printf("ft_strchr Test 2: failed\n");
	//test 3 (Caractère nul)
	if (ft_strchr(s_chr, '\0') == &s_chr[11])
		printf("ft_strchr Test 3 (NULL): ok\n");
	else
		printf("ft_strchr Test 3 (NULL): failed\n");

	// ft_strrchr
	printf("--ft_strrchr--\n");
	char *s_rchr = "BonjourB";
	//test 1 (Caractère trouvé, dernière occurence)
	if (ft_strrchr(s_rchr, 'B') == &s_rchr[7])
		printf("ft_strrchr Test 1: ok\n");
	else
		printf("ft_strrchr Test 1: failed\n");
	//test 2 (Caractère nul)
	if (ft_strrchr(s_rchr, '\0') == &s_rchr[8])
		printf("ft_strrchr Test 2 (NULL): ok\n");
	else
		printf("ft_strrchr Test 2 (NULL): failed\n");

	// ft_strncmp
	printf("--ft_strncmp--\n");
	//test 1 (Identiques)
	if (ft_strncmp("abc", "abc", 3) == 0)
		printf("ft_strncmp Test 1 (Identique): ok\n");
	else
		printf("ft_strncmp Test 1 (Identique): failed\n");
	//test 2 (Différence à n)
	if (ft_strncmp("abcd", "abce", 3) == 0) // Compare 'abc' vs 'abc'
		printf("ft_strncmp Test 2 (Différence à n): ok\n");
	else
		printf("ft_strncmp Test 2 (Différence à n): failed\n");
	//test 3 (Plus grand)
	if (ft_strncmp("abz", "abc", 3) > 0)
		printf("ft_strncmp Test 3 (Plus grand): ok\n");
	else
		printf("ft_strncmp Test 3 (Plus grand): failed\n");
	//test 4 (Plus petit)
	if (ft_strncmp("abc", "abz", 3) < 0)
		printf("ft_strncmp Test 4 (Plus petit): ok\n");
	else
		printf("ft_strncmp Test 4 (Plus petit): failed\n");
	//test 5 (Nul dans la chaine)
	if (ft_strncmp("a\0bc", "a\0bz", 4) == 0) // s1[1] est \0, s2[1] est \0. Différence est faite par la \0.
		printf("ft_strncmp Test 5 (Avec NULL): ok\n");
	else
		printf("ft_strncmp Test 5 (Avec NULL): failed\n");

	// ft_memchr
	printf("--ft_memchr--\n");
	char *s_mchr = "Hello World";
	//test 1
	if (ft_memchr(s_mchr, 'o', 5) == &s_mchr[4]) // Trouvé dans les 5 premiers
		printf("ft_memchr Test 1: ok\n");
	else
		printf("ft_memchr Test 1: failed\n");
	//test 2
	if (ft_memchr(s_mchr, 'o', 3) == NULL) // Non trouvé dans les 3 premiers
		printf("ft_memchr Test 2: ok\n");
	else
		printf("ft_memchr Test 2: failed\n");

	// ft_memcmp
	printf("--ft_memcmp--\n");
	//test 1 (Identiques)
	if (ft_memcmp("abc\0d", "abc\0e", 4) == 0) // Comparaison jusqu'à n=4 (inclut le \0)
		printf("ft_memcmp Test 1 (Identique): ok\n");
	else
		printf("ft_memcmp Test 1 (Identique): failed\n");
	//test 2 (Différence)
	if (ft_memcmp("abcde", "abzde", 5) < 0) // c vs z
		printf("ft_memcmp Test 2 (Différence): ok\n");
	else
		printf("ft_memcmp Test 2 (Différence): failed\n");
	//test 3 (Nul non inclus)
	if (ft_memcmp("abc\0d", "abc\0e", 5) < 0) // Comparaison jusqu'à n=5 ('d' vs 'e')
		printf("ft_memcmp Test 3 (Apres NULL): ok\n");
	else
		printf("ft_memcmp Test 3 (Apres NULL): failed\n");

	// ft_strnstr
	printf("--ft_strnstr--\n");
	char *s_nstr = "The universe is as big as a big mac";
	//test 1 (Trouvé dans la limite)
	if (ft_strnstr(s_nstr, "big", 35) == &s_nstr[21])
		printf("ft_strnstr Test 1: ok\n");
	else
		printf("ft_strnstr Test 1: failed\n");
	//test 2 (Non trouvé car n est trop petit)
	if (ft_strnstr(s_nstr, "big", 16) == NULL)
		printf("ft_strnstr Test 2: ok\n");
	else
		printf("ft_strnstr Test 2: failed\n");
	//test 3 (Aiguille vide)
	if (ft_strnstr(s_nstr, "", 20) == s_nstr)
		printf("ft_strnstr Test 3 (Aiguille vide): ok\n");
	else
		printf("ft_strnstr Test 3 (Aiguille vide): failed\n");

	// ft_atoi
	printf("--ft_atoi--\n");
	//test 1
	if (ft_atoi("  +42") == 42)
		printf("ft_atoi Test 1 (+): ok\n");
	else
		printf("ft_atoi Test 1 (+): failed\n");
	//test 2
	if (ft_atoi("-42") == -42)
		printf("ft_atoi Test 2 (-): ok\n");
	else
		printf("ft_atoi Test 2 (-): failed\n");
	//test 3
	if (ft_atoi("  -42hey") == -42)
		printf("ft_atoi Test 3 (Mixte): ok\n");
	else
		printf("ft_atoi Test 3 (Mixte): failed\n");
	//test 4
	if (ft_atoi("hey42") == 0)
		printf("ft_atoi Test 4 (Initial non-num): ok\n");
	else
		printf("ft_atoi Test 4 (Initial non-num): failed\n");
	//test 5
	if (ft_atoi("--42") == 0)
		printf("ft_atoi Test 5 (Double signe): ok\n");
	else
		printf("ft_atoi Test 5 (Double signe): failed\n");

	// ft_calloc / ft_strdup
	printf("--ft_calloc / ft_strdup--\n");
	char *s_dup = "Test Calloc and Dup";
	//test 1 ft_calloc
	char *m_calloc = (char *)ft_calloc(5, 4); // 20 octets, mis à zéro
	if (m_calloc != NULL && m_calloc[0] == 0 && m_calloc[19] == 0)
		printf("ft_calloc Test 1: ok\n");
	else
		printf("ft_calloc Test 1: failed\n");
	free(m_calloc);
	//test 2 ft_strdup
	char *m_dup = ft_strdup(s_dup);
	if (m_dup != NULL && strcmp(s_dup, m_dup) == 0)
		printf("ft_strdup Test 2: ok\n");
	else
		printf("ft_strdup Test 2: failed\n");
	free(m_dup);

	// ft_substr
	printf("--ft_substr--\n");
	char *s_sub = "123456789";
	//test 1 (Standard)
	char *m_sub = ft_substr(s_sub, 3, 4); // Commence à '4', longueur 4 -> "4567"
	if (m_sub != NULL && strcmp(m_sub, "4567") == 0)
		printf("ft_substr Test 1: ok\n");
	else
		printf("ft_substr Test 1: failed\n");
	free(m_sub);
	//test 2 (Début trop grand)
	m_sub = ft_substr(s_sub, 100, 4); // Début au-delà de la fin
	if (m_sub != NULL && strcmp(m_sub, "") == 0) // Doit retourner "" alloué
		printf("ft_substr Test 2: ok\n");
	else
		printf("ft_substr Test 2: failed\n");
	free(m_sub);

	// ft_strjoin
	printf("--ft_strjoin--\n");
	char *s1_join = "Hello ";
	char *s2_join = "World";
	//test 1
	char *m_join = ft_strjoin(s1_join, s2_join);
	if (m_join != NULL && strcmp(m_join, "Hello World") == 0)
		printf("ft_strjoin Test 1: ok\n");
	else
		printf("ft_strjoin Test 1: failed\n");
	free(m_join);
	//test 2 (S1 vide)
	m_join = ft_strjoin("", s2_join);
	if (m_join != NULL && strcmp(m_join, "World") == 0)
		printf("ft_strjoin Test 2: ok\n");
	else
		printf("ft_strjoin Test 2: failed\n");
	free(m_join);

	// ft_strtrim
	printf("--ft_strtrim--\n");
	char s1_trim[] = "***Mai*son***";
	char *s2_trim = "*";
	//test 1
	char *m_trim = ft_strtrim(s1_trim, s2_trim);
	if (m_trim != NULL && strcmp(m_trim, "Mai*son") == 0)
		printf("ft_strtrim Test 1: ok\n");
	else
		printf("ft_strtrim Test 1: failed\n");
	free(m_trim);
	//test 2 (S1 vide)
	m_trim = ft_strtrim("", s2_trim);
	if (m_trim != NULL && strcmp(m_trim, "") == 0)
		printf("ft_strtrim Test 2: ok\n");
	else
		printf("ft_strtrim Test 2: failed\n");
	free(m_trim);
	//test 3 (trim vide)
	m_trim = ft_strtrim(s1_trim, "");
	if (m_trim != NULL && strcmp("", "") == 0)
		printf("ft_strtrim Test 3: ok\n");
	else
		printf("ft_strtrim Test 3: failed\n");
	free(m_trim);
	//test 4 (S1 uniquement de trim)
	m_trim = ft_strtrim("***", s2_trim);
	if (m_trim != NULL && strcmp(m_trim, "") == 0)
		printf("ft_strtrim Test 4: ok\n");
	else
		printf("ft_strtrim Test 4: failed\n");
	free(m_trim);

	return (0);
}
