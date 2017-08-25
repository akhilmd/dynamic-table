#include "../include/dynamic_table.h"
#include "../include/timer.h"
#include <unistd.h>
DynamicTable* new(int max_size, float inc_factor, float dec_factor, bool use_malloc) {
  DynamicTable* new_dt = malloc(sizeof(DynamicTable));

  new_dt->max_size = max_size;
  new_dt->size = 0;
  new_dt->inc_factor = inc_factor;
  new_dt->dec_factor = dec_factor;

  new_dt->data = malloc(max_size * sizeof(int));

  new_dt->use_malloc = use_malloc;

  return new_dt;
}

double push(DynamicTable* dt, int new_val) {
  TimeSpec* start = malloc(sizeof(TimeSpec));
  TimeSpec* end = malloc(sizeof(TimeSpec));

  now(start);
  if (dt->size < dt->max_size) {
    dt->data[dt->size] = new_val;
    (dt->size)++;
  } else {
    // check the use_malloc bool and increase space accordingly
  }
  now(end);

  double te = time_elapsed(start, end);

  free(start);
  free(end);
  return te;
}

int display(DynamicTable* dt) {
  int i = 0;

  printf("size: %d\tmax_size: %d\n", dt->size, dt->max_size);

  if (dt->data == NULL) {
    printf("NULL\n");
    return 0;
  }

  for (i = 0; i < dt->size; ++i) {
    printf("%d ", dt->data[i]);
  }
  printf("\n");
  return 0;
}

