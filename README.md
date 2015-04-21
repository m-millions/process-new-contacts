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

Sample data from the csv file looks like this:

    Julian, Fanning, 82820, 555 11111 11111111, red
    Earlene Merryman, blue, 86258, 305 987 8362
    Theodora Whipkey, red, 54450, 808 633 1734
    Butterfield, Kelsi, (967)-196-4953, yellow, 05644
    Mccaster, Fatimah, (854)-345-7518, gray, 57693
    Mirian, Hankey, 22172, 180 739 1295, aqua marine
    Reinaldo, Vandermeer, 76589, 751 665 5618, gray
    Theo Parrish, green, 60128, 423 334 3136
    0.429926275625
    c

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

    if len(clean_r) < 4 or len(clean_r) > 5:
        print('This record is not the valid length. It will not be processed.')
        print('Here is the value you passed: ' + str(len(clean_r)))
        #break  TODO: COME BACK TO THIS!!!

    *********

    if len(name) < 1 or len(name) > 3:
        #print(len(name))
        #print(name)
        print('This name is not the valid length. \
               It will not be processed.')
        print('Here is the name you passed: ' + str(name))
        # break

    *********

    elif len(clean_r[p]) == 10:
        one_r['telephone'] = clean_r[p]
        #print('telephone: ' + str(one_r['telephone']))
        #print(one_r)
    else:
        print('this record does not contain a valid phone number, \
               zip code, or color. It will not be processed.')
               print('Here is the value you passed: ' + str(clean_r[p]) + "\n")
        #break from processing the remaining positions on the list
        #when one of the values passed isn't valid
        #break

The reason why they should be there is that the current logic will not process a
record if one or more of the elements being passed fails the validation.  The
break here ensures the rest of the record isn't iterated through, because that
is a waste of CPU cycles.  Even though the breaks are commented out the record
will not be passed to the final JSON object for comsumption by a client.

Sample output to the console for each record that fails to process:

Sample errors printed to the console:

    Record is not a valid length.
    [5]
    Color, Telephone, or Zipcode not valid.
    Color, Telephone, or Zipcode not valid.
    [5, 7]
    Color, Telephone, or Zipcode not valid.
    [5, 7, 16]
    Color, Telephone, or Zipcode not valid.
    [5, 7, 16, 31]
    Record is not a valid length.
    [5, 7, 16, 31, 39]
    Color, Telephone, or Zipcode not valid.
    Record is not a valid length.
    [5, 7, 16, 31, 39, 40]
    Color, Telephone, or Zipcode not valid.
    Record is not a valid length.
    [5, 7, 16, 31, 39, 40, 43]
    Color, Telephone, or Zipcode not valid.
    Color, Telephone, or Zipcode not valid.
    [5, 7, 16, 31, 39, 40, 43, 45]
    Record is not a valid length.
    [5, 7, 16, 31, 39, 40, 43, 45, 46]
    Color, Telephone, or Zipcode not valid.
    Color, Telephone, or Zipcode not valid.
    [5, 7, 16, 31, 39, 40, 43, 45, 46, 47]
    Color, Telephone, or Zipcode not valid.
    [5, 7, 16, 31, 39, 40, 43, 45, 46, 47, 49]
    Color, Telephone, or Zipcode not valid.
    [5, 7, 16, 31, 39, 40, 43, 45, 46, 47, 49, 50]
    Record is not a valid length.
    [5, 7, 16, 31, 39, 40, 43, 45, 46, 47, 49, 50, 58]
    Color, Telephone, or Zipcode not valid.
    Color, Telephone, or Zipcode not valid.
    [5, 7, 16, 31, 39, 40, 43, 45, 46, 47, 49, 50, 58, 59]

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
(1) Currently the test coverage is at 72%.  I will be coming back to this
project shortly to get the coverage up to 100%.

(2) Fix known bugs deatiled above in the "Known Bugs" section.

(3) Update the "WHAT THE CODE DOES" section of this README file so that it
explains a little bit more about the limitations and expectations whe processing
the project's accompanying csv file.

(4) Spelling. Probably fix spelling in this README file.  The mote time I spend
coding the worse I seem to get at spelling. No matter how many times I proof, I
always miss something.

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

http://jsonlint.com

http://www.giantflyingsaucer.com/  - Chad Lung - who even though he wasn't
on-hand for this project, he was an continues to be an incredible mentor on
all things tech and I am forever grateful.


CHANGELOG
---------
N/A

AUTHORS
-------
Claudia Ventresca

CONTACT INFO
------------
