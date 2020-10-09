from conans import ConanFile, CMake, tools

class GKlibConan(ConanFile):
  name = "GKlib"
  version = "0.0.1"
  license = "MIT"
  author = "Jeremy Iverson (jiverson002@csbsju.edu)"
  url = "https://github.com/jiverson002/GKlib"
  homepage = "https://github.com/jiverson002/GKlib"
  description = "A library of various helper routines and frameworks used by many of the lab's software."
  topics = ("utilities")
  settings = "os", "compiler", "build_type", "arch"
  options = {
    "shared": [True, False],
    "fPIC": [True, False],
    "visibility": ["hidden", "default"]
  }
  default_options = {
    "shared": False,
    "fPIC": True,
    "visibility": "default" # FIXME: hidden causes build to fail
  }
  exports = ["LICENSE"]
  scm = {
    "type": "git",
    "url": "https://github.com/jiverson002/GKlib.git",
    "revision": "feature/modern-cmake"
  }

  def build(self):
    cmake = CMake(self)
    cmake.definitions["CMAKE_C_VISIBILITY_PRESET"] = self.options.visibility
    #cmake.verbose = True
    cmake.configure()
    cmake.build()
    #cmake.test()
    cmake.install()

  def package(self):
    self.copy("*.h", dst="include/GKlib", src="include")
    self.copy("*GKlib.lib", dst="lib", keep_path=False)
    self.copy("*.dll", dst="bin", keep_path=False)
    self.copy("*.so", dst="lib", keep_path=False)
    self.copy("*.dylib", dst="lib", keep_path=False)
    self.copy("*.a", dst="lib", keep_path=False)
