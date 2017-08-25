#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <math.h>
#include <string.h>

typedef struct DynamicTable {
  int max_size;
  int size;
  float inc_factor;
  float dec_factor;

  int* data;

  // custom fields
  bool use_malloc;
} DynamicTable;

DynamicTable* new(int, float, float, bool);
double push(DynamicTable*, int);
int display(DynamicTable*);

