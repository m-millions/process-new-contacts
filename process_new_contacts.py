from __future__ import print_function
from operator import itemgetter

import csv
import getopt
import io
import json
import os.path
import re
import sys


_RCOUNT = [] #keeps track of the total number of records that failed processing
_RNUM = '' #used to count number of records, record count will start at 0

def get_new_contacts(input_file, output_file):
    '''
    Opens the designated file for processing new contact data.
    Calls "get_clean_data" on each record to remove undesired characters.

    Then calls "process_contacts" to:
     (1) check that each record is the valid
     (2) convert all processed data to a valid JSON object
     (3) if valid data found and converted to JSON, dump the JSON
         object ( a list of dictionaries) to a properly encoded file.
    '''
    #check to see that the file to be process actually exists, if it doesn't
    #exist abort all code exectution and prompt the user to try again.
    #TODO: Raise exception if file exists but has no records
    all_rs = {}
    error_data = []
    file_path = './' + input_file
    final_json_data = {"entries":'', "errors":''}
    json_data = []
    name = ''
    if os.path.exists(file_path):
        #print('File exists!')
        #Open the file to start processing data
        with open(input_file, 'r') as f:
            data = csv.reader(f)
            _RNUM = 0
            #print(_RNUM)
            for r in data:
                name = r[0]
                name = name.split( )
                #print(name)
                #print(len(name))
                #clean up string before processing
                clean_r = get_clean_data(r)
                #print(r)
                #print(clean_r)
                all_rs = process_contacts(clean_r, name, _RNUM)
                #print(all_rs)
                _RNUM = _RNUM + 1
                #only append returned values is the dictionary IS NOT EMPTY
                if len(all_rs) != 0 and len(all_rs) == 6:
                    json_data.append(all_rs.copy())
                    #sort values by lastname, firstname
                    json_data = sorted(json_data, key=itemgetter('lastname',
                                                                 'firstname'))
                    #print(json_data)
            final_json_data['entries'] = json_data
            final_json_data['errors'] = _RCOUNT
        f.close()
        #print(final_json_data)
    else:
        print('The file you want to process is missing! Please try again.')
        exit()
    #Dump list of dictionaries as a JSON object to a file
    with io.open(output_file, 'w', encoding='utf-8') as of:
        of.write(unicode(json.dumps(final_json_data, ensure_ascii=False)))

def get_clean_data(r):
    '''
    Process data to clean up leading and trailing spaces and applies a regex to
    eliminate unwanted characters in this case ( ) { } - < > and empty spaces
    in-between words.  More characters can be added as needed.
    '''
    clean_r = []
    for i in r:
        i = re.sub('[\(\)\{\}<>\-\ ]', '', i)
        i = i.strip()
        clean_r.append(i)
    return clean_r

def process_contacts(clean_r, name, _RNUM):
    '''
    This function processes the data after the record has been cleaned by
    get_clean_data.
    '''
    colors = ['yellow', 'aquamarine', 'blue', 'gray', 'pink', 'red', 'green']
    one_r = {}
    p = 0
    ii = 0 # for tracking loop iterations
    e = 0
    #clear values for every iteration so not to pass in old values from
    #previous record by mistake
    one_r.clear()
    #PROCESS POSITION 0
    if len(clean_r) < 4 or len(clean_r) > 5: #ERROR
        print('Record is not a valid length.')
        #if e == 1: #encountered a record-level error already stop
            #break
        if e == 0:
            e = 1
            _RCOUNT.append(_RNUM)
            print(_RCOUNT)
    elif len(clean_r) == 4:
        #print(len(clean_r))
        if len(name) < 1 or len(name) > 3: #ERROR
            #print(len(name))
            #print(name)
            print('Name is not the valid length.')
            #if e == 1:  #encountered a record-level error already stop
                #break
            if e == 0:
                e = 1
                _RCOUNT.append(_RNUM)
                print(_RCOUNT)
        if len(name) == 2:
            #print(len(name))
            one_r['firstname'] = name[0]
            one_r['middle'] = ' '
            one_r['lastname'] = name[1]
            #print(one_r)
        elif len(name) == 3:
            #print(len(name))
            one_r['firstname'] = name[0]
            one_r['middle'] = name[1]
            one_r['lastname'] = name[2]
            #print(one_r)
    elif len(clean_r) == 5:
        one_r['firstname'] = clean_r[0]
        one_r['middle'] = ' '
        one_r['lastname'] = clean_r[1]
        #print(one_r)

    #Initialize p for processing correct position 1 through 3 or 4
    if len(clean_r) == 4:
        p = 1 #set to the actual start position
        ii = 3 #set to limit of iterations
        #print('prosessing starting at position: ' + str(p))
    if len(clean_r) == 5:
        p = 2
        ii = 4
        #print('prosessing starting at position: ' + str(p))
    #iterate through list object starting at initialize position
    #break when iteration count is greater than the last position
    #of the list to be processed
    for i in clean_r:
        if p <= ii:
            #check current position against current iteration number
            #print(str(p) + ' ' + str(ii))
            if clean_r[p] not in colors:
                if len(clean_r[p]) == 5 or len(clean_r[p]) == 9:
                    one_r['zipcode'] = clean_r[p]
                    #print('zip_code: ' + str(one_r['zipcode']))
                    #print(one_r)
                elif len(clean_r[p]) == 10:
                    one_r['telephone'] = clean_r[p]
                    #print('telephone: ' + str(one_r['telephone']))
                    #print(one_r)
                else:
                    print('Color, Telephone, or Zipcode not valid.')
                    #break from processing the remaining positions on the list
                    #when one of the values passed isn't valid
                    if e == 1: #encountered a record-level error already stop
                        break
                    elif e == 0:
                        e = 1
                        #print(_RNUM)
                        _RCOUNT.append(_RNUM)
                        print(_RCOUNT)
            else:
                if clean_r[p] in colors:
                    one_r['color'] = clean_r[p]
                    #print('color: ' + str(one_r['color']))
                    #print(one_r)
            p = p + 1
        else:
            break
    #print(one_r)
    return one_r

def main():
    '''
    o = command line option
    a = argument passed from the command line option

    Usage:
         python process_new_contacts.py -i [input-file-name].csv
                                        -o [output-file-name].JSON

    TO DO: Exception Handling for args is incomplete re-write to that is
    properly handles when one, both, or all args are missing. The "input_file"
    and "output_file" values have been hard-coded in this example,
    because passing the values at the command line has been turned off.
    '''
    input_file = 'new_contacts.csv'
    output_file = 'new_contacts.JSON'

    #try:
    #     myopts, args = getopt.getopt(sys.argv[1:],"i:o:")
    #except getopt.GetoptError as e:
    #    print(str(e))
    #    print("Usage: %s -i input -o output" % sys.argv[0])
    #    sys.exit(2)

    #for o, a in myopts:
    #    if o == '-i':
    #        input_file=a
    #    elif o == '-o':
    #        output_file=a
    # Uncomment to see value of args passed at the command line
    # print ("Input file : %s and output file: %s" % (input_file, output_file))

    get_new_contacts(input_file, output_file)

if __name__ == '__main__':
    main()
