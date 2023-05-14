
import sys, re
import os, glob
import csv

def compute_attn(path, pattern, max_duration, rowskip = 0, print_dates = 0):
    
    att_dict = {};
    date_list = [];
    
    for filename in glob.glob(os.path.join(path, pattern)):
        with open(os.path.join(os.getcwd(), filename), 'r') as file:
            
            dict = parse_zoomattn(date_list, file, max_duration, rowskip)
            
            merge_dicts(att_dict, dict)
            
            file.close()
    
    if print_dates:
        date_list.sort()
        for date in date_list:
            print(date[:10])
    
    return att_dict
            
def parse_zoomattn(date_list, file, max_duration, rowskip = 0):
    
    # For zoom attendance CSVs, the following happens:
    # row[0] = Name of person
    # row[4] = Duration as a float
    
    dict = {}
    i = -1
    reader = csv.reader(file)
    
    for row in reader:
        i += 1
        
        if (i < rowskip): # skips rowskip many rows
            continue
        else:
            if (i == 1): date_list.append(row[3]) # debug statement to check dates of classes
        
            if row[0] in dict: # If key exists, add new value
                dict[row[0]] += int(float(row[4]))
            else:
                dict[row[0]] = int(float(row[4])) #otherwise add the key
    
    for key, val in dict.items(): # sets values to max possible duration if they exceed it
        if val > max_duration:
            dict[key] = max_duration
    
    return dict
    
def merge_dicts(primary, secondary):

    # No need for return as dictionaries are pass by reference
    
    for key, val in secondary.items(): # adds/updates values in primary based on those in secondary
        if key in primary:
            primary[key] += val
        
        else:
            primary[key] = val
            
def print_dict(dict):
    
    for key, value in sorted(dict.items(), key=lambda x: x[0]):
        print("{} : {}".format(key, value))
    

def main():
    
    path = "zoom_attn/"
    pattern = "*.csv"
    max_duration = 75 # maximum duration per class
    rowskip = 1 # first row in zoom csv files has column header data
    
    att_dict = compute_attn(path, pattern, max_duration, rowskip, 0)
    
    print_dict(att_dict)

main()
