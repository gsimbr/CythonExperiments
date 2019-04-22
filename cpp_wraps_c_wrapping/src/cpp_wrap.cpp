// cpp_wrap.cpp
#include <stddef.h>
#include <string>
#include <iostream>
#include "cpp_wrap.hpp"
#include "c_code.c"

namespace wrap {
StringClass::StringClass(const std::string &stringi)
{
  std::cout << stringi << std::endl;
  gx = stringi;
}

size_t StringClass::getStringLength()
{
  const char *cstr = gx.c_str();
  return getCStringLength(cstr);
}

}