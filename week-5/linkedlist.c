#include <stdio.h>
#include <stlib.h>

// Create a data structure "node"
typdef struct node
{
    int number;
    struct node *next; // Pointer to next node
}
node;

int main(void)
{
    // List of size
    node *list = NULL;

    // Add a number to list
    node *n = malloc(sizeof(node));
    if (n == NULL)
    {
        return 1;
    }
    n->number = 1; // Update number in node "n" to value of 1
    n->next = NULL; // Update pointer in node "n" to value of NULL

    // Update list to point to new node
    list = n;

    // Add a number to list
    n = malloc(sizeof(node)); // Create new memory allocaiton using n
    // Check if there is space, and if not free list
    if (n == NULL)
    {
        free(list);
        return 1;
    }
    n->number = 2; // Update number value in node "n" to 2
    n->next = NULL; // Set next point in node "n" to NULL
    list->next = n; // Update next point in "list" (previously NULL) to point to n

    // Add a number to list
    n = malloc(sizeof(node));
    if (n == NULL)
    {
        free(list);
        free(list->next);
        return 1;
    }
}