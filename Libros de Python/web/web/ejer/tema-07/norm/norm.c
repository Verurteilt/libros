
#include <stddef.h>
#include <math.h>

float norm (float* data, size_t size)
{
  float* end = data + size;
  float  res = 0;

  while (data < end)
    {
      res += *data * *data;
      ++ data;
    }

  return sqrtf (res);
}
