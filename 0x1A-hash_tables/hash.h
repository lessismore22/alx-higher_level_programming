#ifndef HASH_H
#define HASH_H

typedef struct hash_node {
	char *key;
	char *value;
	struct hash_node *next;
}node;

typedef struct hash_table {
	node **head;
}


#endif
