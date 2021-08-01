from conans import ConanFile, MSBuild, tools, AutoToolsBuildEnvironment
from conans.tools import os_info


class VampConan(ConanFile):
    name = "vamp"
    license = "MIT"
    author = "Edgar (Edgar@AnotherFoxGuy.com)"
    url = "https://github.com/tenacityteam/conan-recipes/"
    homepage = "https://vamp-plugins.org"
    description = "Vamp is an audio processing plugin system for plugins that extract descriptive information from audio data"
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False], "fPIC": [True, False]}
    default_options = {"shared": False, "fPIC": True}

    def source(self):
        tools.get(**self.conan_data["sources"][self.version], strip_root=True)

    def build(self):
        if os_info.is_windows:
            msbuild = MSBuild(self)
            msbuild.build("build/VampHostSDK.vcxproj")
            msbuild.build("build/VampPluginSDK.vcxproj")
        else:
            autotools = AutoToolsBuildEnvironment(self)
            autotools.configure(args=["--disable-programs"])
            autotools.make()

    def package(self):
        self.copy("*.h", dst="include/vamp", src="vamp")
        self.copy("*.h", dst="include/vamp-hostsdk", src="vamp-hostsdk")
        self.copy("*.h", dst="include/vamp-sdk", src="vamp-sdk")
        self.copy("*.lib", dst="lib", src="build", keep_path=False)
        self.copy("*.dll", dst="bin", src="build", keep_path=False)
        self.copy("libvamp-*.so", dst="lib", keep_path=False)
        self.copy("libvamp-*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = tools.collect_libs(self)
