#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Created by : Billz @ 11/1/2017
'''

import subprocess
import re


def main():
    ''' funciton to test and replace shell script '''

    print("Please key in the file name you wanna save data to")
    file_name = input()
    print("What is the name of program with search function?")
    prog_name = input()
    print("What is the name of program with NO search function?")
    prog_name2 = input()

    dict_name = 'dict'

    with open(file_name, 'w') as fh:
        pass

    for dict_index in range(6):
        for bal_stra in range(6):

            # setup
            case = dict_name + str(dict_index) + ' ' + str(bal_stra)
            command = 'time ./' + prog_name + ' ' + case
            command2 = 'time ./' + prog_name2 + ' ' + case

            print('running \"', command, '\"')

            # get output from shell
            raw_res_stderr = subprocess.check_output(
                command, stderr=subprocess.STDOUT, shell=True).decode('unicode-escape')

            # for the no search
            raw_res_ns_stderr = subprocess.check_output(
                command2, stderr=subprocess.STDOUT, shell=True).decode('unicode-escape')

            res_stderr = refine(raw_res_stderr)
            res_stdout = find_height(raw_res_stderr)
            res_ns_stderr = refine(raw_res_ns_stderr)

            # write into the file
            if res_stderr != None and res_stdout != None:
                with open(file_name, 'a') as fh:
                    fh.write(case + '\n')
                    fh.write('\t' + 'time with search:\t' + res_stderr + '\n')
                    fh.write('\t' + 'time w/o search:\t' + res_ns_stderr + '\n')
                    fh.write('\theight of tree :\t{}\n'.format(
                        res_stdout) + '\n')


def find_height(raw):
    """find height for tree"""
    res = re.findall(r'height = (\d+)', raw, re.M)

    if res == None:
        return None

    return res[0]


def refine(raw_res):
    '''find time and return'''

    #  res = re.findall(r'(\d+\..*?)user', raw_res)
    res = re.findall(r'user.*?(\d+.*?s)', raw_res, re.M)
    print(raw_res)

    if res == None:
        return None

    return res[0]


if __name__ == "__main__":
    main()
