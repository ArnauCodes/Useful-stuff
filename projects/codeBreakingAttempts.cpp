#include <iostream>
#define ll long long
#define sh short

using namespace std;

ll factorial(sh n){
  return n == 1 ? 1 : n * factorial(n - 1);
}

ll permute(sh object, sh sample){
  sh denominator = object - sample;
  return factorial(object) / factorial(denominator);
}

// Change the values of ints while there are < 35
int main()
{
  sh lower_case_letters = 8, nums = 1, samp = lower_case_letters + nums, p_len;
  cout << "Password length: ";
  cin >> p_len;
  cout << "There are " << permute(samp, p_len) << " ways of creating a password with these options" << "\n";
}
