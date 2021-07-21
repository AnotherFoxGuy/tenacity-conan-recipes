## Working

Windows     MSVC -> MSVC: `conan-recipes>conan create ./libmp3lame/all 3.100@ -s compiler="Visual Studio" -s compiler.version=16` -

## Not Working

Windows     MSVC -> GCC: `conan create ./libmp3lame/all 3.100@ -s:b compiler="Visual Studio" -s:b compiler.version="16" -s:h compiler="gcc" -s:h compiler.version="11.1"`
Windows     ?    -> GCC `conan create ./libmp3lame/all 3.100@ -s:h compiler="gcc" -s:h compiler.version="11.1"`