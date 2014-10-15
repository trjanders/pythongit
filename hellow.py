# single line comment in python
"""
multiline comment in python
"""

# remove shoes

# Log Setup
# do some inline logging to help figure out any errors
# set log filename to program name with .log extension
# while in development environment set log level to most detailed logging DEBUG
# reference https://docs.python.org/3.4/howto/logging.html
#
import logging
# hellow.log was created automagically when i ran this file using F5 in Python IDLE
logging.basicConfig(filename='hellow.log',level=logging.DEBUG)
logging.debug('This is a DEBUG message and should go to the log file')
logging.info('INFO message for logging general events and above')
logging.warning('WARNING message for logging warnings and above, the default')
logging.error('ERROR message for logging only ERRORs')


# Log the Version of Python Being Executed
# todo, works now
# need to import sys at top of file
import sys
# then print(sys.version) where you want detailed version info output
print(sys.version)
# or print("The Python version is %s.%s.%s" % sys.version_info[:3]) to filter detail
print("The Python version is %s.%s.%s" % sys.version_info[:3])


# Some Printing Examples
# hello python world
print ('Hello Python World with single quotes')
print ("Hello Python World with double quotes")
print('print Hello Python World with no space between print and parens, better')
# with inline line break
# the below \n works, but some say \r\n is most correct on windows platform
print('print with newline \n inline')  # works
print('print with carriage return \r inline')  # creates a space only when run in IDLE
print('print with carriage return and newline \r\n inline')  # works

# Exit Codes
# does python use exit codes?

