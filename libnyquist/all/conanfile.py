from conans import ConanFile, CMake, tools
from conans.tools import os_info

class libnyquistConan(ConanFile):
    name = "libnyquist"
    license = "MIT"
    author = "Edgar (Edgar@AnotherFoxGuy.com)"
    url = "https://github.com/tenacityteam/conan-recipes/"
    homepage = "https://www.cs.cmu.edu/~music/libnyquist"
    description = "libnyquist is a sound synthesis and composition language offering a Lisp syntax as well as an imperative language syntax and a powerful integrated development environment."
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake"
    options = {"shared": [True, False], "fPIC": [True, False]}
    default_options = {"shared": False, "fPIC": True}
    exports_sources = ["src/*", "CMakeLists.txt"]

    # libasound2-dev

    def requirements(self):
        self.requires.add('libsndfile/[1.0.x]')
        self.requires.add('portaudio/v190600.20161030@bincrafters/stable') 

    def source(self):
        tools.get(**self.conan_data["sources"][self.version])

    def build(self):
        cmake = CMake(self)
        cmake.definitions['USE_SOURCE_LIBS'] = 'ON'
        cmake.configure()
        cmake.build()

    def package(self):
        cmake = CMake(self)
        cmake.install()

    def package_info(self):
        self.cpp_info.libs = tools.collect_libs(self)
