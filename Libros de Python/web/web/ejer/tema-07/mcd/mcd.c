
int mcd (int a, int b)
{
  if (a < 0)
    a = -a;
  if (b < 0)
    b = -b;

  a = a % b;
  if (a > 0)
    return mcd (b, a);
  else
    return b;
}
