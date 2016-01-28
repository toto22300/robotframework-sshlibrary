#summary Release notes for all the SSHLibrary releases
#labels Featured



# SSHLibrary 2.0.2 #
| **ID** | **Type** | **Priority** | **Summary** |
|:-------|:---------|:-------------|:------------|
| [Issue 101](https://code.google.com/p/robotframework-sshlibrary/issues/detail?id=101) | Defect   | High         | Execute Command hangs when large enough output |

Altogether 1 issues.

# SSHLibrary 2.0.1 #

| **ID** | **Type** | **Priority** | **Summary** |
|:-------|:---------|:-------------|:------------|
| [Issue 95](https://code.google.com/p/robotframework-sshlibrary/issues/detail?id=95) | Defect   | High         | Not possible to gracefully stop hanging `Execute Command` |
| [Issue 97](https://code.google.com/p/robotframework-sshlibrary/issues/detail?id=97) | Enhancement | High         | Add support to naming arguments passed to `SSHClient` to ease programmatic usage |

Altogether 2 issues.

# SSHLibrary 2.0 #

SSHLibrary 2.0 was released on Wednesday the 27th of November, 2013.

This release introduces several new keywords, mainly for the SFTP functionality, adds the support for character encodings and now has extensive documentation and library usage examples.

For installation see [the instructions](InstallationInstructions.md). The source distribution is now hosted at [PyPI](https://pypi.python.org/pypi/robotframework-sshlibrary/2.0).

Questions and comments related to the release can be sent to
[the mailing lists](https://code.google.com/p/robotframework/wiki/MailingLists) and possible bugs can be kindly submitted to [the issue tracker](https://code.google.com/p/robotframework-sshlibrary/issues).

## Most important enhancements ##

### Support for configuring the character encoding ###

SSHLibrary now supports configuring the character encoding as the library default or per
connection ([issue 60](https://code.google.com/p/robotframework-sshlibrary/issues/detail?id=60)). All the inputs are encoded before they are sent to the remote host. Respectively, all the outputs from the server are decoded before they are handled by the library and the test data. This also applies to the file and directory names on the remote host. If no encoding is explicitly defined, UTF-8 is assumed.

### New keywords for transferring directories ###

Keywords `Get Directory` and `Put Directory` were added for downloading and uploading directories including their content, additionally with their subdirectories recursively included ([issue 66](https://code.google.com/p/robotframework-sshlibrary/issues/detail?id=66)).

### New keyword for getting the connection information ###

Keyword `Get Connection` was added for the purpose of querying the connection index and the connection specific configuration ([issue 72](https://code.google.com/p/robotframework-sshlibrary/issues/detail?id=72)). The keyword returns an object identical to the objects returned by keyword `Get Connections`.

### Possible to wait for more content with keyword `Read` ###

Keyword `Read` now has an optional argument `delay` ([issue 90](https://code.google.com/p/robotframework-sshlibrary/issues/detail?id=90)). If `delay` is given, the keyword waits that amount of time and reads output from the server again. This wait-read cycle is repeated as long as further reads return more output or the timeout expires. This is to help ensuring that all the output has definitely been read from the server.

### General documentation enhancements ###

The library documentation was greatly improved as part of this release. The major documentation improvements were done related to configuration ([issue 73](https://code.google.com/p/robotframework-sshlibrary/issues/detail?id=73)), interactive sessions ([issue 77](https://code.google.com/p/robotframework-sshlibrary/issues/detail?id=77)) and handling the command output ([issue 59](https://code.google.com/p/robotframework-sshlibrary/issues/detail?id=59)). Also, the most of the keyword usage examples were rewritten to match their practical use cases better. The old runnable examples, formerly included in the source distribution, were removed and merged with the keyword examples ([issue 61](https://code.google.com/p/robotframework-sshlibrary/issues/detail?id=61)).

## Backward incompatible changes ##

### New keywords for listing and asserting remote files and directories ###

Keywords `List Directory`, `List Files In Directory` and `List Directories in Directory` were added for listing the content on the remote host ([issue 75](https://code.google.com/p/robotframework-sshlibrary/issues/detail?id=75)). Additionally, keywords `File Should Exist`, `File Should Not Exist`, `Directory Should Exist` and `Directory Should Not Exist` were added for asserting if the file or directory exists or not on the remote host ([issue 74](https://code.google.com/p/robotframework-sshlibrary/issues/detail?id=74)). All of these keywords work similarly as the ones in OperatingSystem library.

If both OperatingSystem and SSHLibrary are used in the test data, the keyword names will conflict. The easiest way to fix this is to prefix the keyword with the library name, such as `OperatingSystem.List Directory` or `SSHLibrary.List Directory`. Because the lines can then grow quite long, it's a good idea to import the libraries with custom shorter names e.g. as following:
```
  *** Settings ***
  Library  SSHLibrary       WITH NAME  Remote
  Library  OperatingSystem  WITH NAME  Local

  *** Variables ***
  ${test_file}  hello.txt

  *** Test Cases ***
  [Setup]  Local.File Should Exist  ${test_file}
  Remote.Put File  ${test_file}
  Remote.File Should Exist  ${test_file}
  [Teardown]  Remote.Execute Command  rm -f ${test_file}
```

### Deprecated keywords for configuring the defaults were removed ###

Keywords `Set Timeout`, `Set Prompt`, `Set Newline` and `Set Default Log Level`, used for configuring the library defaults, were removed in favor of `Set Default Configuration` ([issue 76](https://code.google.com/p/robotframework-sshlibrary/issues/detail?id=76)). The removed keywords were already deprecated in SSHLibrary 1.1.

### Keyword `Get File` now matches patterns case sensitively ###

When using keyword `Get File` with glob patterns given in the source file path, the paths are now matched case and space sensitively ([issue 70](https://code.google.com/p/robotframework-sshlibrary/issues/detail?id=70)). Earlier the matching was both case and space insensitive.

## Deprecated features ##

### Keyword specific path separators are now deprecated ###

Path separator is now configurable as the library default or per connection ([issue 93](https://code.google.com/p/robotframework-sshlibrary/issues/detail?id=93)). This makes more sense than passing it as an argument to the every call of keywords `Get File` and `Put File`.

It is still possible to use argument `path_separator` with keywords `Get File` and `Put File` as before but this will print a deprecation warning. The argument value is now empty by default, which in practice means that the library or the connection specific `path_separator` is then used instead.

## Full list of fixes and enhancements in 2.0 ##

| **ID** | **Type** | **Priority** | **Summary** |
|:-------|:---------|:-------------|:------------|
| [Issue 69](https://code.google.com/p/robotframework-sshlibrary/issues/detail?id=69) | Defect   | High         | `Execute Command` occasionally returns `None` instead of `0` as the exit status on Jython |
| [Issue 60](https://code.google.com/p/robotframework-sshlibrary/issues/detail?id=60) | Enhancement | High         | Support for configuring character encoding |
| [Issue 66](https://code.google.com/p/robotframework-sshlibrary/issues/detail?id=66) | Enhancement | High         | New keywords for getting and putting whole directories |
| [Issue 59](https://code.google.com/p/robotframework-sshlibrary/issues/detail?id=59) | Documentation | High         | Enhanced documentation of reading command output |
| [Issue 61](https://code.google.com/p/robotframework-sshlibrary/issues/detail?id=61) | Documentation | High         | Move library usage example to keyword documentation |
| [Issue 73](https://code.google.com/p/robotframework-sshlibrary/issues/detail?id=73) | Documentation | High         | Enhanced library and connection configuration documentation |
| [Issue 77](https://code.google.com/p/robotframework-sshlibrary/issues/detail?id=77) | Documentation | High         | Enhanced documentation of running commands in a new or in an interactive shell |
| [Issue 64](https://code.google.com/p/robotframework-sshlibrary/issues/detail?id=64) | Defect   | Medium       | SSH keys should not be used when logging in with username and password |
| [Issue 70](https://code.google.com/p/robotframework-sshlibrary/issues/detail?id=70) | Defect   | Medium       | Avoid using Robot's deprecated `utils.matches` in `Get File` |
| [Issue 80](https://code.google.com/p/robotframework-sshlibrary/issues/detail?id=80) | Defect   | Medium       | `Write` keywords should not require prompt to be set |
| [Issue 81](https://code.google.com/p/robotframework-sshlibrary/issues/detail?id=81) | Defect   | Medium       | Return server output after login correctly and also log it |
| [Issue 72](https://code.google.com/p/robotframework-sshlibrary/issues/detail?id=72) | Enhancement | Medium       | New keyword `Get Connection` for getting the current connection information |
| [Issue 74](https://code.google.com/p/robotframework-sshlibrary/issues/detail?id=74) | Enhancement | Medium       | New keywords for checking if a file or a directory (not) exists on the remote host |
| [Issue 75](https://code.google.com/p/robotframework-sshlibrary/issues/detail?id=75) | Enhancement | Medium       | New keywords for listing files, directories or both on the remote host |
| [Issue 76](https://code.google.com/p/robotframework-sshlibrary/issues/detail?id=76) | Enhancement | Medium       | Remove deprecated keywords `Set Timeout`, `Set Prompt`, `Set Newline` and `Set Default Log Level` |
| [Issue 82](https://code.google.com/p/robotframework-sshlibrary/issues/detail?id=82) | Enhancement | Medium       | Strings `false` and `False` evaluate false in `Execute Command` and `Read Command Output` arguments |
| [Issue 89](https://code.google.com/p/robotframework-sshlibrary/issues/detail?id=89) | Enhancement | Medium       | Miscellaneous and small library documentation enhancements |
| [Issue 90](https://code.google.com/p/robotframework-sshlibrary/issues/detail?id=90) | Enhancement | Medium       | Support waiting for more content with `Read` |
| [Issue 93](https://code.google.com/p/robotframework-sshlibrary/issues/detail?id=93) | Enhancement | Medium       | Path separator should be configurable per connection |
| [Issue 83](https://code.google.com/p/robotframework-sshlibrary/issues/detail?id=83) | Enhancement | Low          | Terminal type, width and height are configurable also as library defaults |
| [Issue 86](https://code.google.com/p/robotframework-sshlibrary/issues/detail?id=86) | Enhancement | Low          | Keywords `Execute Command` and `Read Command Output` automatically log the return code |

Altogether 21 issues.

# SSHLibrary 1.1 #

SSHLibrary 1.1 was released on Friday the 31st of August, 2012.

This maintenance release adds some new keywords and fixes a some defects. Most interesting of these are the ability to return the return code of executed command with `Execute Command` ([issue 49](https://code.google.com/p/robotframework-sshlibrary/issues/detail?id=49), [issue 53](https://code.google.com/p/robotframework-sshlibrary/issues/detail?id=53)) and more granular control over configuration of a single channel via new keywords ([issue56](https://code.google.com/p/robotframework-sshlibrary/issues/detail?id=56)).

| **ID** | **Type** | **Priority** | **Summary** |
|:-------|:---------|:-------------|:------------|
| [Issue 47](https://code.google.com/p/robotframework-sshlibrary/issues/detail?id=47) | Defect   | Medium       | Registered as `SSHLIbrary` on PyPI when it should be `robotframework-sshlibrary` |
| [Issue 50](https://code.google.com/p/robotframework-sshlibrary/issues/detail?id=50) | Defect   | Medium       | Installation using in `zc.buildout` fails |
| [Issue 55](https://code.google.com/p/robotframework-sshlibrary/issues/detail?id=55) | Defect   | Medium       | SSHLibrary put\_file and get\_file does not work if filename contains URL encoding |
| [Issue 28](https://code.google.com/p/robotframework-sshlibrary/issues/detail?id=28) | Enhancement | Medium       | Prompt should be set per connection |
| [Issue 33](https://code.google.com/p/robotframework-sshlibrary/issues/detail?id=33) | Enhancement | Medium       | Path separator of the target machine should be configurable |
| [Issue 46](https://code.google.com/p/robotframework-sshlibrary/issues/detail?id=46) | Enhancement | Medium       | Add possibility to configure shell/terminal size in `Open Connection` |
| [Issue 49](https://code.google.com/p/robotframework-sshlibrary/issues/detail?id=49) | Enhancement | Medium       | Enhance `Execute Command` to also return return code if requested |
| [Issue 52](https://code.google.com/p/robotframework-sshlibrary/issues/detail?id=52) | Enhancement | Medium       | New keyword `Get Connections` |
| [Issue 53](https://code.google.com/p/robotframework-sshlibrary/issues/detail?id=53) | Enhancement | Medium       | Enhance `Read Command Output` to enable returing of return code |
| [Issue 56](https://code.google.com/p/robotframework-sshlibrary/issues/detail?id=56) | Enhancement | Medium       | New keywords `Set default configuration` and `Set client configuration` |
| [Issue 57](https://code.google.com/p/robotframework-sshlibrary/issues/detail?id=57) | Enhancement | Medium       | Deprecate `Set Timeout`, `Set Prompt` and `Set Newline` |
| [Issue 51](https://code.google.com/p/robotframework-sshlibrary/issues/detail?id=51) | Documentation | Medium       | Create example test cases showing the usage scenarios |

Altogether 10 issues.

# SSHLibrary 1.0 #

SSHLibrary 1.0 was released on Monday 8th of Novemeber 2010.

This release inlcudes enhancements to `Put File` and `Login` keywords and general documentation improvements.
In the future, SSHLibrary will be integrated as a standard library of Robot Framwork and this is probably the
last independent release.

| **ID** | **Type** | **Priority** | **Summary** |
|:-------|:---------|:-------------|:------------|
| [Issue 24](https://code.google.com/p/robotframework-sshlibrary/issues/detail?id=24) | Enhancement | Medium       | Add optional parameter `newlines` to `Put File` keyword |
| [Issue 27](https://code.google.com/p/robotframework-sshlibrary/issues/detail?id=27) | Enhancement | Medium       | `Login` keyword should return the value of the login banner |
| [Issue 23](https://code.google.com/p/robotframework-sshlibrary/issues/detail?id=23) | Documentation | Medium       | Enhance documentation of keywords that can execute commands |

Altogether 3 issues.

# SSHLibrary 0.9 #

SSH Library 0.9 was released 5.3.2009.
The major new features is possibility to login using key-based authentication.
All the included issues are listed below:


| **ID** | **Type** | **Priority** | **Summary** |
|:-------|:---------|:-------------|:------------|
| [Issue 15](https://code.google.com/p/robotframework-sshlibrary/issues/detail?id=15) | Enhancement | High         | Login keyword should not log password value.  |
| [Issue 16](https://code.google.com/p/robotframework-sshlibrary/issues/detail?id=16) | Enhancement | High         | Keyword documentation needs to be enhanced |
| [Issue 12](https://code.google.com/p/robotframework-sshlibrary/issues/detail?id=12) | Defect   | Medium       | Enable SSH Logging keyword should log things before connecting |
| [Issue 13](https://code.google.com/p/robotframework-sshlibrary/issues/detail?id=13) | Enhancement | Medium       | Provide public key authentication keyword for login |
| [Issue 14](https://code.google.com/p/robotframework-sshlibrary/issues/detail?id=14) | Defect   | Medium       | Error message should be better if connection lost during testing also other keywords than Enable SSH Logging |
| [Issue 17](https://code.google.com/p/robotframework-sshlibrary/issues/detail?id=17) | Defect   | Medium       | Timeout given to init cannot be "time string" |
| [Issue 10](https://code.google.com/p/robotframework-sshlibrary/issues/detail?id=10) | Enhancement | Medium       | Clear requirement for paramiko, pycrypto and trilead in Installation Guide |

Altogether 7 issues.