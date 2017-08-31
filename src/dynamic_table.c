#include "../include/dynamic_table.h"
#include "../include/timer.h"

// Initialize new instance
DynamicTable* new(int max_size, float inc_factor, float dec_factor, bool use_malloc) {
  DynamicTable* new_dt = malloc(sizeof(DynamicTable));

  if (new_dt == NULL) {
    return NULL;
  }

  // make sure max_size is >= 1
  new_dt->max_size = max_size;
  new_dt->size = 0;

  // make sure inc_factor is > 1
  new_dt->inc_factor = inc_factor;
  new_dt->dec_factor = dec_factor;

  new_dt->data = malloc(max_size * sizeof(int));

  new_dt->use_malloc = use_malloc;

  return new_dt;
}

// Free allocated data 
DynamicTable* destroy (DynamicTable* dt) {
  free(dt->data);
  free(dt);
  return NULL;
}

double push(DynamicTable* dt, int new_val) {
  TimeSpec* start = malloc(sizeof(TimeSpec));
  TimeSpec* end = malloc(sizeof(TimeSpec));

  // Capture current time
  now(start);

  if (dt->size >= dt->max_size) {
    // check the use_malloc bool and increase space accordingly

    // new size calculated based on the inc_factor field in DynamicTable
    // ceil is used since inc_factor is float
    int new_size = (int) ceil(dt->max_size * dt->inc_factor);

    // printf("upsizing, [%d] [%d]\n", dt->max_size, new_size);

    if (dt->use_malloc) {
      // allocate a new block of memory with new_size
      // copy current data to new block
      // free old allocated memory
      // replace old pointer with new one

      int* new_data = malloc(new_size * sizeof(int));

      // since new_data is guaranteed to not overlap with dt->data,
      // we can use memcpy.
      memcpy(new_data, dt->data, dt->size * sizeof(int));

      // free dt->data
      free(dt->data);

      // update pointer with new, bigger data block
      dt->data = new_data;
    } else {
      // Realloc handles increasing memory in an efficient way.
      // If there is enough space after the current allocated memory, 
      // it will not copy. This will lead to inconsistent numbers
      // when analyzing performance, but must be used in real world 
      // application of this data structure.
      dt->data = realloc(dt->data, new_size * sizeof(int));
    }

    // update max_size
    dt->max_size = new_size;
  }

  // data maight have been resized, but definitely has some extra space.
  dt->data[dt->size] = new_val;
  (dt->size)++;

  // Capture time after operation.
  now(end);

  double te = time_elapsed(start, end);

  free(start);
  free(end);

  // Return time for this operation.
  return te;
}

// Delete last element and return time taken for doing so.
double pop (DynamicTable* dt) {
  TimeSpec* start = malloc(sizeof(TimeSpec));
  TimeSpec* end = malloc(sizeof(TimeSpec));

  now(start);

  // if there are elements to delete
  if (dt->size > 0) {
    // keep min for new_size at 1
    int new_size = dt->size == 1 ? 1 : dt->size - 1;

    // If new_size is small enough, resize
    if (new_size <= dt->max_size/dt->dec_factor) {
      // malloc should not be used here since it will be very bad
      // to copy even when we have enough new space. This is only
      // valid during deletion,
      dt->data = realloc(dt->data, new_size * sizeof(int));
      dt->max_size = new_size;
    }

    // Just decrent size by 1 to 'remove' last element
    --(dt->size);
  }

  now(end);

  double te = time_elapsed(start, end);

  free(start);
  free(end);

  // Return time for operation
  return te;
}

// Utility function to print the data for debugging.
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

