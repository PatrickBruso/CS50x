// Implements a dictionary's functionality

#include <ctype.h>
#include <stdbool.h>
#include <strings.h>

#include "dictionary.h"

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
}
node;

// TODO: Choose number of buckets in hash table
const unsigned int N = 1000;

// Hash table
node *table[N];

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    // lookup hash value in list from Kernighan & Ritchie
    node *n;
    for (n = table[hash(word)]; n != NULL; n = n->next)
    {
        if (strcasecmp(word, n->word) == 0)
        {
            return true;
        }
    }

    return false;
}

// Hashes word to a number
unsigned int hash(const char *word)
{
    // Improve this hash function (Thanks Doug Lloyd!)
    int sum = 0;
    for (int i = 0; str[i] != '\0'; i++)
    {
        sum += tolower(str[j]);
    }
    return sum % N
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    // TODO
    // Open dictionary file
    FILE *dictionary = fopen(dictionary, "r");  // Not sure this works for using dictionary variable as pathname
    if (f = NULL)
    {
        return false;
    }


    int length = 0; // Variable for length of dictionary array
    char **words = loadfile(dictionary, &length); //set pointer array to load dictionary and determine length of file
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    // TODO
    return 0;
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    // TODO
    return false;
}
