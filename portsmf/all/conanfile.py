from conans import ConanFile, CMake, tools
from conans.tools import os_info

class PortSMFConan(ConanFile):
    name = "portsmf"
    license = "MIT"
    author = "Edgar (Edgar@AnotherFoxGuy.com)"
    url = "https://github.com/tenacityteam/conan-recipes/"
    homepage = "https://github.com/tenacityteam/portsmf"
    description = "Portsmf is Port Standard MIDI File, a cross-platform, C++ library for reading and writing Standard MIDI Files."
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False], "fPIC": [True, False]}
    default_options = {"shared": False, "fPIC": True}

    def source(self):
        tools.get(**self.conan_data["sources"][self.version], strip_root=True)

    def build(self):
        cmake = CMake(self)
        cmake.definitions['BUILD_APPS'] = 'OFF'
        cmake.definitions['BUILD_TESTING'] = 'OFF'
        cmake.definitions['BUILD_SHARED_LIBS'] = self.options.shared
        cmake.configure()
        cmake.build()

    def package(self):
        cmake = CMake(self)
        cmake.install()

    def package_info(self):
        self.cpp_info.libs = tools.collect_libs(self)
