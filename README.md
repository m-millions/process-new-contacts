CONFIGURATION INSTRUCTIONS
--------------------------
This project is meant to be a small stand alone scrip with no specific
configuration requirement other than having Python 2.7 intalled and running.


INSTALLATION INSTRUCTIONS
-------------------------
A 'requirements.txt' has been included ( as good practice ), but has been left
empty on purpose, since the script 'process_new_contacts.py' uses all facilities
from the Python standard library and on additional packages will have to be
installed, locally, for the script to work successfully.


A 'test-requirements.txt' has been included (as good practice).  These packages
are meant to be installed only in a local, testing environment, and not meant to
be part of the production stack requirements.  The are not necessary to run the
unittests, but thought I should inclue reference to nose, pep8, and pylint. All
code lines are no longer than 80 chars and any tabs have been replaces with
spaces.

OPERATING INSTRUCTIONS
----------------------
The 'process_new_contacts.py' script is designed to be executed at the command
line, but the feature which allows you to pass parameters at the command line
has been disabled.  It is commented out on the code ( It has one known bug. ),
please feel free to activate it an use it at will.

The 'input_file' and 'output_file' variables have been hard-coded as such:
    input_file = 'new_contacts.csv'
    output_file = 'new_contacts.json'

WHAT THE CODE DOES
------------------
The script takes and existing comma delimed file and iterates through its
records, applies various rules to determine if the record is valid, and converts
and dumps only valid records to a JSON object.

The resulting JSON object is then dumped to a file, and looks like this:

{
"errors": [
5,
7,
16,
31,
39,
40,
43,
45,
46,
47,
49,
50,
58,
59
],
"entries": [
     {
      "middle": " ",
      "firstname": "Noah",
      "color": "yellow",
      "lastname": "Moench",
      "telephone": "2326952394",
      "zipcode": "123123121"
     },
     {
      "middle": " ",
      "firstname": "Ria",
      "color": "aquamarine",
      "lastname": "Tillotson",
      "telephone": "1969105548",
      "zipcode": "97671"
     },
     ...
    ]
}

The generated JSON object can be validated via wwww.jsonlint.com

KNOWN BUGS
----------
In scritp 'processs_new_contacts.py' the breaks in the following code were
causign the script to not run.  The were commented out but not removed as they
should be there.

The reason why they should be there is that the current logic will not process a
record if one or more of the elements being passed fails the validation.  The
break here ensures the rest of the record isn't iterated through, because that
is a waste of CPU cycles.  Even though the breaks are commented out the record
will not be passed to the final JSON object, for comsumption by a client.

TESTING METHODOLOGY
-------------------
The bulk of the unittests focus on testing the functionality in 'get_clean_data'
and 'process_contacts'; these funcitons are called by the 'process_contacts'.
The major data transformation scenarios are handled and documented in the tests
themselves.

Normally when testing a scrip like this I would use Mock methods handle the
parts of the test which have to do with opening files for data processing,
but since it's the methods outside of the 'process_contacts' function, I saw
it save for this small example to ommit the mocking from testing.  However, in
practice, this part of the code should be properly mocked and tested.

WAYS TO IMPROVE ON THIS CODE
----------------------------


COPYRIGHT and LICENSING
-----------------------
N/A

TROUBLESHOOTING
---------------
All print statements were left commented out but still in the code, this was
doen to faciliate de-bugging (if needed) for anyone not using other tools like
pdb, iPython, etc...

Feel free to remove the print statements at will.

CREDITS and ACKNOWLEDGEMENTS
----------------------------
www.stackoverflow.com
https://docs.python.org
www.google.com
http://jsonlint.com/

Chad Lung - who even though he wasn't on-hand for this project, he was an
continues to be an incredible mentor on all things tech and I am forever
grateful.

CHANGELOG
---------
The majord difference between this project's version and what I sent out
previously is that the following have been implemented and/or updated:
      (1) requirements.txt
      (2) test-requirements.txt
      (3) README.md
      (4) process_new_contacts_unittest.py
      (5) Exception handling added in get_new_contacts in file
          process_new_contacts.py

AUTHORS
-------
Claudia Ventresca

CONTACT INFO
------------
