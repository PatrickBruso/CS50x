// Implements a dictionary's functionality

#include <ctype.h>
#include <stdbool.h>
#include <strings.h>
#include <string.h>
#include <stdio.h>
#include <stdlib.h>

#include "dictionary.h"

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
}
node;

// Choose number of buckets in hash table
const unsigned int N = 1000;  // I set this high because that's what it seemed like we needed to do

// Hash table
node *table[N];

// Counter for words in dictionary
int word_count = 0;

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    // lookup hash value in list (from Kernighan & Ritchie)
    node *n;
    for (n = table[hash(word)]; n != NULL; n = n->next)
    {
        if (strcasecmp(word, n->word) == 0) // Check if word is the same as node pointer to word
        {
            return true;
        }
    }

    return false;
}

// Hashes word to a number
unsigned int hash(const char *word)
{
    // hash function (Thanks Doug Lloyd!)
    int sum = 0;
    for (int i = 0; word[i] != '\0'; i++)
    {
        sum += tolower(word[i]) * sum;
    }
    return sum % N;
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    // Open dictionary file
    FILE *file = fopen(dictionary, "r");
    if (file == NULL)
    {
        return false;
    }

    char buffer[LENGTH + 1];
    // Load each string using fscanf
    while (fscanf(file, "%s", buffer) == 1)
    {
        // Dynamically allocate space for new node
        node *n = malloc(sizeof(node));

        // Check for NULL pointer
        if (n == NULL)
        {
            fclose(file);
            return false;
        }

        // Copy current word into node we created
        strcpy(n->word, buffer);
        // Set new node's next to NULL
        n->next = NULL;

        // Hash word and insert into table
        int index = hash(buffer);
        n->next = table[index];

        // Set index to current node
        table[index] = n;

        // Increase word count variable by one
        word_count++;
    }
    // Close file and return true
    fclose(file);
    return true;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    // return word_count variable
    return word_count;
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    // Go through each node in hash table
    for (int i = 0; i < N; i++)
    {
        // set node to table index
        node *n = table[i];

        while (n != NULL) // quit if n is NULL (hit end of table)
        {
            node *tmp = n; // assign n to temp node
            n = n->next; // assign n->next to n
            free(tmp); // free temp node
        }
    }
    return true;
}
