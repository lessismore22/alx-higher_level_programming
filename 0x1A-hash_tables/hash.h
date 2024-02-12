#ifndef HASH_H
#define HASH_H

/**
 * struct hash_node - Node of a hash table
 *
 * @key: The key, string
 * The key is unique in the hashtable
 * @value: The value corresponding to a key
 * @next: A pointer to the next node of the list
 */
typedef struct hash_node {
	char *key;
	char *value;
	struct hash_node *next;
}hash_node;


/**
 * struct hash_table 
 * @size: The size of the array
 *  @array: An array of size @size
 *  Each cell of this array is a pointer to the first node of a linked list
 *  because we want our hashtable to use a chaining collision handling
 */

typedef struct hash_table
{
	unsigned long int size;
	hash_node **array;
} hash_table
hash_table_t *hash_table_create(unsigned long int size);
unsigned long int hash_djb2(const unsigned char *str);
unsigned long int key_index(const unsigned char *key, unsigned long int size);
int hash_table_set(hash_table_t *ht, const char *key, const char *value);

#endif
