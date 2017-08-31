#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <math.h>
#include <string.h>

typedef struct DynamicTable {
  // Amount of memory allocated
  int max_size;

  // No. of items inserted
  int size;

  // Factor by which to increase amount of
  // allocated memory
  float inc_factor;

  // Factor by which to decrease amount of
  // allocated memory
  float dec_factor;

  // Pointer to allocated location
  int* data;

  // If true, while increasing, uses malloc+memcpy
  // If false, uses realloc
  bool use_malloc;
} DynamicTable;

// Create new dynamic table
DynamicTable* new(int, float, float, bool);

// Free memory alllocated to prevent leaks
DynamicTable* destroy(DynamicTable*);

// Push and pop both alter the data and may resize the allocated
// memory. Both also return time taken for that operation.
double push(DynamicTable*, int);
double pop(DynamicTable*);

int display(DynamicTable*);

