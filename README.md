



* Makefile, YML pipeline - By using a Makefile, developers can automate the build process and ensure that the project is built correctly and consistently across different platforms and environments. This can save time and reduce errors, particularly in larger projects with many dependencies and configurations.


* Setup and teardown @classmethod functions - are special functions that can be used to set up and tear down the test environment before and after each test case is executed. These functions are often used to create or initialize objects, open and close database connections, or perform other tasks that are required to run the test cases. One common use case for @classmethod in pytest is to define a setup method that needs to be run before any tests in the class are run. By defining a class method with the @classmethod decorator and naming it setup_class, pytest will automatically run this method before any tests in the class are run.


* Fixtures - fixtures @pytest.fixture functions define functions that we can pass and can be used only in test_ scenarios to verify processes , verify connection, or to pass configuration parameters usually its the fist steps of the testing cycle. or open a session or hold on processes like sql and requests

* Fixtures - define functions that we can pass and can be used only in test_ scenarios to verify processes or to pass configuration parameters usually its the fist steps of the testing cycle. or open a session or hold on processes like sql and requests

```
import pytest


@pytest.fixture
def fixture_func_hi():
    return 'hi'


@pytest.fixture
def fixture_func_bye():
    return 'bye'


def test_somthing(fixture_func_hi, fixture_func_bye):
    assert fixture_func_hi == 'hi', 'Was expected to get hi'
    assert fixture_func_bye == 'hello', 'Was expected to get bye'
```


* Django  https://docs.djangoproject.com/en/3.1/intro/tutorial01/ Create project folder Django-admin startproject mysite Python manage.py runserver Starting development server at http://127.0.0.1:8000/


working with files and paths - OS - operating systems library
* import os
* os.name: Returns the name of the operating system.
* os.getcwd(): Returns the current working directory.
* os.chdir(path): Changes the current working directory to the specified path.
* os.listdir(path='.'): Returns a list of all files and directories in the specified path.
* os.mkdir(path): Creates a new directory with the specified path.
* os.makedirs(path): Creates a new directory and all necessary parent directories with the specified path.
* os.remove(path): Deletes the file with the specified path.
* os.rmdir(path): Deletes the directory with the specified path (directory must be empty).
* os.removedirs(path): Deletes the directory and all parent directories with the specified path (directories must be empty).
* os.rename(src, dst): Renames the file or directory with the specified source path to the specified destination path.
* os.path.exists(path): Returns True if the file or directory with the specified path exists, otherwise False.
* os.path.isdir(path): Returns True if the specified path is a directory, otherwise False.
* os.path.isfile(path): Returns True if the specified path is a file, otherwise False.
* os.path.join(path1, path2, ...): Joins two or more path components together, using the appropriate separator for the operating system.
* os.path.abspath(path): Returns the absolute path of the specified path.
* os.path.basename(path): Returns the base name of the specified path (i.e. the file or directory name).
* os.path.commonpath(paths): Returns the longest common sub-path of the specified paths.
* os.path.commonprefix(paths): Returns the longest common prefix of the specified paths.
* os.path.dirname(path): Returns the directory name of the specified path.
* os.path.exists(path): Returns True if the specified path exists, otherwise False.
* os.path.expanduser(path): Expands the initial component of the path to the user's home directory.
* os.path.expandvars(path): Expands environment variables in the specified path.
* os.path.getatime(path): Returns the last access time of the specified path as a floating-point number of seconds since the epoch.
* os.path.getctime(path): Returns the creation time of the specified path as a floating-point number of seconds since the epoch.
* os.path.getmtime(path): Returns the last modification time of the specified path as a floating-point number of seconds since the epoch.
* os.path.getsize(path): Returns the size of the specified file in bytes.
* os.path.isabs(path): Returns True if the specified path is an absolute path, otherwise False.
* os.path.isdir(path): Returns True if the specified path is a directory, otherwise False.
* os.path.isfile(path): Returns True if the specified path is a file, otherwise False.
* os.path.islink(path): Returns True if the specified path is a symbolic link, otherwise False.
* os.path.ismount(path): Returns True if the specified path is a mount point, otherwise False.
* os.path.join(path1, path2, ...): Joins two or more path components together, using the appropriate separator for the operating system.
* os.path.normcase(path): Normalizes the case of the specified path.
* os.path.normpath(path): Normalizes the specified path by removing redundant separators and up-level references.
* os.path.realpath(path): Returns the absolute path of the specified path, resolving any symbolic links.
* os.path.relpath(path, start='.'): Returns a relative path from start to the specified path.
* os.path.samefile(path1, path2): Returns True if the two specified paths refer to the same file, otherwise False.
* os.path.sameopenfile(fp1, fp2): Returns True if the two specified open files refer to the same file, otherwise False.
* os.path.amestat(stat1, stat2): Returns True if the two specified file stat structures refer to the same file, otherwise False.
* os.path.split(path): Splits the specified path into a directory and file name.
* os.path.splitdrive(path): Splits the specified path into a drive letter and the rest of the path.
* os.path.splitext(path): Splits the specified path into a base name and extension


strings
* len(string): Returns the length of the string.
* string.lower(): Returns the lowercase version of the string.
* string.upper(): Returns the uppercase version of the string.
* string.strip(): Removes leading and trailing whitespace from the string.
* string.replace(old, new): Replaces all occurrences of old in the string with new.
* string.split(separator): Splits the string into a list of substrings based on the separator.
* string.startswith(substring): Returns True if the string starts with the specified substring.
* string.endswith(substring): Returns True if the string ends with the specified substring.
* string.count(substring): Returns the number of times substring appears in the string.
* string.find(substring): Returns the index of the first occurrence of substring in the string.
* string.isnumeric(): Returns True if the string consists of only numeric characters.
* string.isalpha(): Returns True if the string consists of only alphabetic characters.
* string.isalnum(): Returns True if the string consists of only alphanumeric characters.


Lists
* len(list): Returns the number of elements in the list.
* list.append(item): Adds an element to the end of the list.
* list.insert(index, item): Inserts an element at a specific index in the list.
* list.remove(item): Removes the first occurrence of an element from the list.
* list.pop(index): Removes and returns the element at a specific index in the list.
* list.sort(): Sorts the elements of the list in ascending order.
* list.reverse(): Reverses the order of the elements in the list.
* list.index(item): Returns the index of the first occurrence of an element in the list.
* list.count(item): Returns the number of times an element appears in the list.
* list.copy(): Returns a shallow copy of the list.
* list.clear(): Removes all elements from the list.
* list.extend(iterable): Appends the elements of an iterable to the end of the list.
* len(): Returns the number of elements in the list.
* append(): Adds an element to the end of the list.
* extend(): Adds the elements of another list (or any iterable) to the end of the list.
* insert(): Inserts an element at a specified position in the list.
* remove(): Removes the first occurrence of an element from the list.
* pop(): Removes and returns the element at a specified index in the list.
* index(): Returns the index of the first occurrence of an element in the list.
* count(): Returns the number of times an element appears in the list.
* sort(): Sorts the elements of the list in ascending order.
* reverse(): Reverses the order of the elements in the list.
* copy() : make a copy of the list into a new list




Dictionary
* len(dictionary): Returns the number of key-value pairs in the dictionary.
* dictionary[key]: Returns the value associated with a given key in the dictionary.
* dictionary[key] = value: Associates a value with a given key in the dictionary.
* dictionary.get(key, default): Returns the value associated with a given key in the dictionary, or a default value if the key is not present.
* dictionary.pop(key): Removes a key-value pair from the dictionary and returns the corresponding value.
* dictionary.keys(): Returns a list of all keys in the dictionary.
* dictionary.values(): Returns a list of all values in the dictionary.
* dictionary.items(): Returns a list of all key-value pairs in the dictionary as tuples.
* dictionary.update(other_dictionary): Adds all key-value pairs from another dictionary to the current dictionary.
* dictionary.clear(): Removes all key-value pairs from the dictionary.
* len(): Returns the number of key-value pairs in the dictionary.
* keys(): Returns a list of all the keys in the dictionary.
* values(): Returns a list of all the values in the dictionary.
* items(): Returns a list of tuples, where each tuple contains a key-value pair.
* get(key, default): Returns the value associated with the given key, or the default value if the key is not present in the dictionary.
* pop(key, default): Removes and returns the value associated with the given key, or the default value if the key is not present in the dictionary.
* popitem(): Removes and returns a key-value pair from the dictionary in arbitrary order.
* update(dict2): Adds the key-value pairs from dict2 to the dictionary.
* clear(): Removes all the key-value pairs from the dictionary.








Unix/Linux
* Create files from the terminal: Terminal > touch “File name” -> touch filename.txt
* ls: List the contents of a directory
* cd: Change the current working directory
* pwd: Print the current working directory
* mkdir: Create a new directory
* rm: Remove a file or directory
* cp: Copy a file or directory
* mv: Move or rename a file or directory
* cat: Print the contents of a file to the screen
* grep: Search for a pattern in a file or output
* sed: Stream editor for modifying text
* awk: Text processing tool for extracting and manipulating data
* chmod: Change the permissions of a file or directory
* chown: Change the owner of a file or directory
* sudo: Run a command with elevated privileges
* ssh: Secure Shell client for remote login and execution of commands on a remote machine
* scp: Secure Copy for transferring files between machines over a secure network
* tar: Archive utility for creating and manipulating tar archives
* gzip: Compression utility for compressing files
* curl: Command-line tool for transferring data from or to a server
* wget: Command-line tool for retrieving files from the web
* ps: Display information about running processes
* top: Display a real-time view of system performance and process activity
* ps aux - checks what are the running apps


Flags in Pytest:
* -v: Increase verbosity of test output.
* -q: Decrease verbosity of test output.
* -k EXPRESSION: Only run tests whose names match the given substring expression.
* -m MARKEXPR: Only run tests that are marked with the given marker expression.
* -x: Stop the test run after the first failure.
* --maxfail=num: Stop the test run after num failures.
* --lf: Run only the tests that failed in the previous test run.
* --ff: Run all tests, but run the failures from the previous test run first.
* --tb=style: Set the traceback style. Valid styles are "auto", "long", "short", "line", and "native".
* --pdb: Drop into the Python debugger on test failures or errors.
* --capture: Set the mode for capturing stdout/stderr. Valid modes are "no", "sys", "fd", and "tee-sys".



# Environment setup:
# Local
- Download latest python version
- Download latest Pycharm version
- Configure project test runner to be pytest
- Download required packages (pip install)


# Create folders inside the project:
### functions:
- Imoprt packeges
- General functions
- General Classes
- BDD tagging
- parameters
- Dictionaries
- Lists
- Links
- Environments
- APIs
- SoapUI
- Requests
- APP scenarios

### tests:
- from functions import *
- test_ senario01()
- test_scenario02()

### YAML:
- Yaml-pipeline-file.yml , Create YAML pipeline and execute the jobs by steps via Azure devops
  setting up the branch the pool of the VM and the steps for execution downloading pythong then installing the packages then executing the scenarios with pytest
- Requirments.txt - list of all required packages and their versions to use in automation

- Execute scenarios locally and review all works

# Cloud
- Upload the code to github repo
- Create and configure Agent in Azure pools and the VM (windows, MAC, linux)
- Create the pipeline run and debug make sure all working
- Execute jobs and review the results in Azure pipelines logs or HTML report

### Extra:
- BDD add bdd folder and the bdd scenarios.sql file
- tag the functions with the BDD steps "Given When And Then And"

# Projects:
1) Python Automation framework - python + pytest + Azure pipelines integration
2) Python Mobile Automation framework - python + pytest + appium + Android emulator


