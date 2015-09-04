# Your task is to read the input DATAFILE line by line, and for the first 10 lines (not including the header)
# split each line on "," and then for each line, create a dictionary
# where the key is the header title of the field, and the value is the value of that field in the row.
# The function parse_file should return a list of dictionaries,
# each data line in the file being a single list entry.
# Field names and values should not contain extra whitespace, like spaces or newline characters.
# You can use the Python string method strip() to remove the extra whitespace.
# You have to parse only the first 10 data lines in this exercise,
# so the returned list should have 10 entries!
import os

DATADIR = ""
DATAFILE = "beatles-diskography.csv"


def parse_file(datafile):
    data = [ ]
    counter=0
    counter1=0
    with open(datafile, "r") as f:
        for line in f:
            #print line.split(',')
            line=line.strip('\n')
            list_ele = line.split(',')
            counter+=1
            counter1+=1
            if(counter==1):
               title=list_ele[0]
               ukchartp=list_ele[1]
               label= list_ele[2]
               released=list_ele[3]
               us_chartp=list_ele[4]
               riacerti=list_ele[5]
               bpa_certification=list_ele[6]
            else:
               data.append({title:list_ele[0],ukchartp:list_ele[1], label:list_ele[2],released:list_ele[3],
                            us_chartp:list_ele[4],riacerti:list_ele[5],bpa_certification:list_ele[6]})
            if(counter1==10):
                break
        print data
            
    return data

parse_file(DATAFILE);
