#include "../include/timer.h"

double time_elapsed (TimeSpec* start, TimeSpec* end) {
  long long sms_s = ((long long) start->tv_sec * 1000000000);
  long long sms_n = (long long) (start->tv_nsec);

  long long ems_s = ((long long) end->tv_sec * 1000000000);
  long long ems_n = (long long) (end->tv_nsec);

  double te = (((double)-sms_s-sms_n+ems_s+ems_n)/1000000.0);
  return te > 0.0 ? te : 0.0;
}

int now(TimeSpec* ts) {
  clock_gettime(CLOCK_REALTIME, ts);
  return 0;
}

