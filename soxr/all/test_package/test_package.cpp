#include <cstdlib>
#include <iostream>
#include <soxr.h>

int main()
{
    std::cout << "SoX version: " << SOXR_THIS_VERSION_STR << std::endl;
    return EXIT_SUCCESS;
}
