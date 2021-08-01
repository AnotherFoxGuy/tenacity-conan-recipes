from conans import ConanFile, CMake, tools
from conans.tools import os_info


class libsoxrConan(ConanFile):
    name = "libsoxr"
    license = "MIT"
    author = "Edgar (Edgar@AnotherFoxGuy.com)"
    url = "https://github.com/tenacityteam/conan-recipes/"
    homepage = "https://sourceforge.net/projects/soxr/"
    description = "The SoX Resampler library `libsoxr' performs one-dimensional sample-rate conversion—it may be used, for example, to resample PCM-encoded audio."
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake_find_package"
    options = {
        "shared": [True, False],
        "fPIC": [True, False],
        "openmp": [True, False],
        "lsr_bindings": [True, False]
    }
    default_options = {
        "shared": False,
        "fPIC": True,
        "openmp": False,
        "lsr_bindings": True
    }

    def source(self):
        tools.get(**self.conan_data["sources"][self.version], strip_root=True)

    def build(self):
        cmake = CMake(self)
        cmake.definitions['BUILD_TESTS'] = 'OFF'
        cmake.definitions['BUILD_SHARED_LIBS'] = self.options.shared
        cmake.definitions['WITH_OPENMP'] = self.options.openmp
        cmake.definitions['WITH_LSR_BINDINGS'] = self.options.lsr_bindings
        cmake.configure()
        cmake.build()

    def package(self):
        cmake = CMake(self)
        cmake.install()

    def package_info(self):
        self.cpp_info.libs = tools.collect_libs(self)
