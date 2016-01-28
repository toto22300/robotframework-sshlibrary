This guide explains how to install Robot Framework SSHLibrary on Linux and Windows. The Linux parts likely work for other Unix-like operating systems (like OS X) as well.

The guide is divided as following:


# Dependencies #

## Python ##

To use SSHLibrary with Python, a module named [Paramiko](http://www.lag.net/paramiko) is required, and additionally Paramiko requires [PyCrypto](http://www.pycrypto.org) module as its dependency.

### Linux ###

Depending on the [installation approaches](#Installation.md) discussed further below, Paramiko and PyCrypto may be installed automatically by SSHLibrary.

If not automatically installed, you may use your distribution's package manager. For example on Debian variants, running `sudo apt-get install python-paramiko` should install them.

Alternatively, you can always install them using the source distributions from PyPI:
  * PyCrypto: https://pypi.python.org/pypi/pycrypto
  * Paramiko: https://pypi.python.org/pypi/paramiko

### Windows ###

On Windows, you should always install PyCrypto using the [binary installer](http://www.voidspace.org.uk/python/modules.shtml#pycrypto) **before** installing Paramiko. This is because installing PyCrypto automatically would require a C compiler. Make sure you pick the correct Paramiko installer depending on your Python version and CPU architecture.

Like on Linux, Paramiko may be installed automatically by SSHLibrary, but you can also install it yourself using the [source distribution](https://pypi.python.org/pypi/paramiko).

## Jython ##

To use SSHLibrary with Jython, Trilead SSH library is required.

Regardless of the operating system, you need to download [Trilead SSH JAR distribution](http://search.maven.org/remotecontent?filepath=com/trilead/trilead-ssh2/1.0.0-build217/trilead-ssh2-1.0.0-build217.jar) and append its path to your CLASSPATH.


# Installation #

The easiest way to install SSHLibrary is using [pip package manager](http://www.pip-installer.org).

If you do not want to install pip, or are using Jython which does not support it, you can always install SSHLibrary using the source distribution.

If you have [setuptools](http://pythonhosted.org/setuptools/) (or its fork [distribute](http://pythonhosted.org/distribute/)) installed,  [the dependencies](#Dependencies.md) should be installed automatically by both of the following approaches. However, on Windows you still need to install PyCrypto binaries first.

## Using pip ##

With `pip`, all you need to do is run the following command:
```
pip install robotframework-sshlibrary
```

## Using source distribution ##

  1. Download the source tar.gz at https://pypi.python.org/pypi/robotframework-sshlibrary.
  1. Extract the package to a temporary location.
  1. Open a terminal / command prompt.
  1. `cd` to the extracted directory.
  1. Run `python setup.py install` or `jython setup.py install`, depending on which interpreter you are using.


# Verifying the installation #

To test that the installation of SSHLibrary and its dependencies was successful, run in a terminal / command prompt:

```
    python -c "import SSHLibrary"
```
or
```
    jython -c "import SSHLibrary"
```

If you get no error messages, SSHLibrary is installed correctly.