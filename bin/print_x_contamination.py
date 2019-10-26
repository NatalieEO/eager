#!/usr/bin/env python3
import sys, re, json
from collections import OrderedDict

data=OrderedDict()

Input_files=sys.argv[1:]

output = open("nuclear_contamination.txt", 'w')
print ("Individual", "Method1_MOM_estimate", "Method1_MOM_SE", "Method1_ML_estimate", "Method1_ML_SE", "Method2_MOM_estimate", "Method2_MOM_SE", "Method2_ML_estimate", "Method2_ML_SE", sep="\t", file=output)
for fn in Input_files:
    with open(fn, 'r') as f:
        Estimates={}
        Ind=re.sub('\.X.contamination.out$', '', fn)
        for line in f:
            fields=line.strip().split()
            if line.strip()[0:19] == "We have nSNP sites:":
                nSNPs=fields[4][:-1]
            elif line.strip()[0:7] == "Method1" and line.strip()[9:16] == 'new_llh':
                mom1=fields[3].split(":")[1]
                err_mom1=fields[4].split(":")[1]
                ml1=fields[5].split(":")[1]
                err_ml1=fields[6].split(":")[1]
            elif line.strip()[0:7] == "Method2" and line.strip()[9:16] == 'new_llh':
                mom2=fields[3].split(":")[1]
                err_mom2=fields[4].split(":")[1]
                ml2=fields[5].split(":")[1]
                err_ml2=fields[6].split(":")[1]
        data[Ind]={ "Method1_MOM_estimate" : mom1, "Method1_MOM_SE" : err_mom1, "Method1_ML_estimate" : ml1, "Method1_ML_SE" : err_ml1, "Method2_MOM_estimate" : mom2, "Method2_MOM_SE" : err_mom2, "Method2_ML_estimate" : ml2, "Method2_ML_SE" : err_ml2 }
        print (Ind, mom1, err_mom1, ml1, err_ml1, mom2, err_mom2, ml2, err_ml2, sep="\t", file=output)

with open('nuclear_contamination.json', 'w') as outfile:
    json.dump(data, outfile)