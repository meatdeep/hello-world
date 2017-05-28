import json
import pickle
import ast
import re
import csv
from cStringIO import StringIO
import sys
import random
#print 'Number of arguments:', len(sys.argv), 'arguments.'
#print 'Argument List:', str(sys.argv)
ifile=sys.argv[1]
sfile=sys.argv[2]
ofile=sys.argv[3]
edwpid=sys.argv[4]
edwpid=str(edwpid)
num_lines = sum(1 for line in open(ifile,'r'))
#print num_lines
my_list = list(xrange(1,num_lines+1))
#print my_list
#ipfile =open(ifile,'r')
with open(sfile) as schfile:
        schList = schfile.read().split()
        #print schList
#total_columns = len(schList)
#print total_columns

s = "\x01"
s1=""
idx=0
selected_column_values=[]
with open(ifile,'r') as fin:
        with open(ofile, "w") as fout:
                for line in fin.readlines():
                        selected_column_values=[]
                        selected_column_values.append(edwpid+'-'+'0'+str(my_list[idx]))
			last= line.strip().split("|")[-1]
			last_name, last_value =last.strip().split(":")
                        for schema in schList:
                                #print schema
                                for column in line.strip().split("|")[1:]:
                                        if len(column.strip().split(":")) == 2:
                                                column_name, column_value = column.strip().split(":")
                                        else:
                                                column_name, column_value = column.strip().split(":")[0], ":".join(column.strip().split(":")[1:])
					if schema == column_name:
						print ('if',schema,column_name,last_name,column_value)
                                               	selected_column_values.append(column_value)
						break	
					elif column_name == last_name:
						selected_column_values.append("")
						print ('schema',schema,'column_name',column_name,'last_name',last_name)
					
                        selected_column_values.append(edwpid)
                        fout.write(s.join(selected_column_values))
                        fout.write("\n")
                        idx=idx+1
