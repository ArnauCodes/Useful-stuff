#include <iostream>
#include <string>

// Exponent must be an int
std::string solve(int *exp, std::string *variable, std::string *e_ans, double *coeff){
  double nume = (*coeff); 
  (*exp)++;
  return ((*exp)-1 == -1) ? (std::to_string(*coeff)) + "ln|" + (*variable) + "| +c" : 
  (std::to_string(nume / (*exp)) + (*variable) + (*e_ans) + std::to_string((*exp)) + ") +c");
};

int main() {
  int exp;
  double coeff;
  std::string variable, c_str = "Integrate with respect to: " + variable, e_ans = "^(";
  std::cout << c_str;
  std::cin >> variable;
  std::cout << "Exponent of " + variable + " = ";
  std::cin >> exp;
  std::cout << "Coeffiecent of " + variable + " = ";
  std::cin >> coeff;
  std::cout << solve(&exp, &variable, &e_ans, &coeff) << std::endl;
  return 0;
};
