// A2DD.h
#ifndef CPP_WRAPP_HPP
#define CPP_WRAPP_HPP
#include <string>
#include <stddef.h>
namespace wrap {
class StringClass
{
  std::string gx;

public:
  StringClass(const std::string &stringi);
  size_t getStringLength();

};
}
#endif