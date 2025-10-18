#include <unistd.h>

void    putstr(char *str)
{
    int i;

    i = 0;
    while (str[i] != '\0')
    {
        write(1, &str[i], 1);
        write(1, "   ", 3);
        i++;
    }
}

int main(int argc, char *argv[])
{
    if (argc == 2)
    {
        char    *str = argv[1];
        putstr(str);
        write(1, "\n", 1);
    }
    else
        putstr("Error");
    return (0);
}


// Dans la chaine de caracteres, ajouter 3 espaces entre chaques caracteres
// avec un nl