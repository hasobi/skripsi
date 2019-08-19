# -*- coding: utf-8 -*-
"""tugas-akhir-v3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1S6vb819hlTKmBo3sIpBChY3imkl1huac

**Import library yang dibutuhkan**
"""

#import Library
import sklearn
import numpy as np
import pandas as pd
# import tensorflow as tf

#import MLPClassifier
from sklearn.neural_network import MLPClassifier

"""**Untuk import file dari google drive**"""

from google.colab import drive
drive.mount('/content/drive')

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

dataset = pd.read_csv("/content/drive/My Drive/Tugas Akhir a.k.a SKRIPSI/dataset/gabungan_train_test-original.csv")
# dataset

protocol_dict ={
    "udp" : 0,
    "tcp" : 1,
    "icmp": 2
}

service_dict={
    "Z39_50" : 0,
    "X11" : 1,
    "whois" : 2,
    "vmnet" : 3,
    "uucp_path" : 4,
    "uucp" : 5,
    "urp_i" : 6,
    "urh_i" : 7,
    "time" : 8,
    "tim_i" : 9,
    "tftp_u" : 10,
    "telnet" : 11,
    "systat" : 12,
    "supdup" : 13,
    "sunrpc" : 14,
    "ssh" : 15,
    "sql_net" : 16,
    "smtp" : 17,
    "shell" : 18,
    "rje" : 19,
    "remote_job" : 20,
    "red_i" : 21,
    "private" : 22,
    "printer" : 23,
    "pop_3" : 24,
    "pop_2" : 25,
    "pm_dump" : 26,
    "other" : 27,
    "ntp_u" : 28,
    "nntp" : 29,
    "nnsp" : 30,
    "netstat" : 31,
    "netbios_ssn" : 32,
    "netbios_ns" : 33,
    "netbios_dgm" : 34,
    "name" : 35,
    "mtp" : 36,
    "login" : 37,
    "link" : 38,
    "ldap" : 39,
    "kshell" : 40,
    "klogin" : 41,
    "iso_tsap" : 42,
    "IRC" : 43,
    "imap4" : 44,
    "http_8001" : 45,
    "http_443" : 46,
    "http_2784" : 47,
    "http" : 48,
    "hostnames" : 49,
    "harvest" : 50,
    "gopher" : 51,
    "ftp_data" : 52,
    "ftp" : 53,
    "finger" :  54,
    "exec" : 55,
    "efs" : 56,
    "ecr_i" : 57,
    "eco_i" : 58,
    "echo" : 59,
    "domain_u" : 60,
    "domain" : 61,
    "discard" : 62,
    "daytime" : 63,
    "ctf" : 64,
    "csnet_ns" : 65,
    "courier" : 66,
    "bgp" : 67,
    "auth" : 68,
    "aol" : 69

}

target_dict ={ "xterm" : 0,
              "xsnoop" : 1,
              "xlock" : 2,
              "worm" : 3,
              "warezmaster" : 4,
              "warezclient" : 5,
              "udpstorm" : 6,
              "teardrop" : 7,
              "sqlattack" : 8,
              "spy" : 9, 
              "snmpguess" : 10,
              "snmpgetattack" : 11,
              "smurf" : 12,
              "sendmail" : 13,
              "satan" : 14,
              "saint" : 15,
              "rootkit" : 16,
              "ps" : 17,
              "processtable" : 18,
              "portsweep" : 19,
              "pod" : 20,
              "phf" : 21,
              "perl" : 22,
              "normal" : 23,
              "nmap" : 24,
              "neptune" : 25,
              "named" : 26,
              "multihop" : 27,
              "mscan" : 28,
              "mailbomb" : 29,
              "loadmodule" : 30,
              "land" : 31,
              "ipsweep" : 32,
              "imap" : 33,
              "httptunnel" : 34,
              "guess_passwd" : 35,
              "ftp_write" : 36,
              "buffer_overflow" : 37,
              "back" : 38,
              "apache2" : 39
             }

flag_dict={
    "SH" : 0,
    "SF" : 1,
    "S3" : 2,
    "S2" : 3,
    "S1" : 4,
    "S0" : 5,
    "RSTR" : 6,
    "RSTOS0" : 7,
    "RSTO" : 8,
    "REJ" : 9,
    "OTH" : 10

}

dataset.replace(protocol_dict, inplace = True)
dataset.replace(service_dict, inplace = True)
dataset.replace(target_dict, inplace = True)
dataset.replace(flag_dict, inplace = True)

dataset

X = dataset.loc[:, :'num_packet']
y = dataset.loc[:, 'type_attack']

y = y.astype(str)

temp = set(y)
# temp

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)

clf = MLPClassifier(random_state = 5)

clf.fit(X_train, y_train)

pred = clf.predict(X_test)

accuracy_score(y_test,pred)

from sklearn.model_selection import cross_validate

from sklearn.metrics import accuracy_score, make_scorer
from sklearn.model_selection import cross_validate, ShuffleSplit

clf = MLPClassifier(random_state = 5, max_iter=300)

scoring = {'accuracy': make_scorer(accuracy_score)}

cv = ShuffleSplit(n_splits=3, test_size=0.33, random_state=2)
scores = cross_validate(clf, X, y, cv=cv, scoring=scoring, return_train_score=True)

print(scores)