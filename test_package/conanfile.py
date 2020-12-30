import os

from conans import ConanFile, CMake, tools

class GKlibTestConan(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake"

    def build(self):
        cmake = CMake(self)
        #cmake.verbose = True
        cmake.configure()
        cmake.build()

    def imports(self):
        self.copy("*.dll", dst="bin", src="bin")
        self.copy("*.dylib*", dst="lib", src="lib")
        self.copy('*.so*', dst='lib', src='lib')

    def test(self):
        os.chdir("bin")
        self.run(".%sexample" % os.sep)
