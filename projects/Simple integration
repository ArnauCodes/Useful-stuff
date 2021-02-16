#include <iostream>
#include <string>

# Upgraded in the future to integrate more complex functions
std::string solve(int *exp, std::string *variable, std::string *e_ans, std::string *e_den){
  int dd = std::int_fast16_t((*exp)++);
  int exp_pp = std::int_fast16_t((*exp));
  return (("(("+*variable)+")" + (*e_ans) + std::to_string(*exp))+")" + (*e_den) + std::to_string(*exp) + " +c";
}

int main() {
  int exp;
  std::string variable, c_str = "Integrate with respect to: " + variable, e_ans = "^", e_den = "/";
  std::cout << c_str;
  std::cin >> variable;
  std::cout << "Exponent of " + variable + " = ";
  std::cin >> exp;
  std::cout << solve(&exp, &variable, &e_ans, &e_den) << std::endl;
  return 0;
}
