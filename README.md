[ ![Download](https://api.bintray.com/packages/jiverson002/public-conan/GKlib%3Ajiverson002/images/download.svg) ](https://bintray.com/jiverson002/public-conan/GKlib%3Ajiverson002/_latestVersion)

## Conan package recipe for [*GKlib*](https://github.com/KarypisLib/GKlib.git)

A library of various helper routines and frameworks used by many of the lab's
software.

The packages generated with this **conanfile** can be found on [Bintray](https://bintray.com/jiverson002/public-conan/GKlib%3Ajiverson002).

## Issues

If you wish to report an issue or make a request for a package, please do so
here:

[Issues Tracker](https://github.com/jiverson002/GKlib-conan/issues)


## For Users

### Basic setup

    $ conan install GKlib/0.0.1@jiverson002/stable

### Project setup

If you handle multiple dependencies in your project it is better to add a
*conanfile.txt*

    [requires]
    GKlib/0.0.1@jiverson002/stable

    [options]
    GKlib:shared=True # False
    GKlib:fPIC=False # True
    GKlib:visibility="hidden" # "default"

    [generators]
    cmake

Complete the installation of requirements for your project running:

    $ mkdir build && cd build && conan install ..

Note: It is recommended that you run conan install from a build directory and
not the root of the project directory. This is because conan generates
*conanbuildinfo* files specific to a single build configuration which by default
comes from an autodetected default profile located in ~/.conan/profiles/default.
If you pass different build configuration options to conan install, it will
generate different *conanbuildinfo* files. Thus, they should not be added to the
root of the project, nor committed to git.

## Build and package

The following command both runs all the steps of the conan file, and publishes
the package to the local system cache. This includes downloading dependencies
from "build_requires" and "requires", and then running the build() method.

    $ conan create . jiverson002/stable

## Conan Recipe License

NOTE: The conan recipe license applies only to the files of this recipe, which
can be used to build and package GKlib.
It does *not* in any way apply or is related to the actual software being
packaged.

[MIT](LICENSE)
