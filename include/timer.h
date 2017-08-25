#include <time.h>

typedef struct timespec TimeSpec;

double time_elapsed (TimeSpec*, TimeSpec*);
int now(TimeSpec*);
