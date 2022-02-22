#!/usr/bin/python3
import pandas as pd

"""

:param file: a textlist of names to filter by, saved in current directory
:type file: textfile
:param Doctors: a dataframe created from a csv file
:type Doctors: pandas dataframe
:param matches: a series containing only items that match filter list
:type matches: pandas series
:param newDF: dataframe containing only items that match the filter
:type newDF: pandas dataframe

Filters a dataframe by a target list of last names:
Opens and reads a target list of last names; opens a csv as a dataframe;
compares column 'Last' in dataframe to list of target names; pulls out any
rows in which the last name matches a target last name; creates a new
dataframe of only the rows containing target last names; writes the new
dataframe to a .csv file

"""

file = open('ChineseNames.txt', 'r').read().split()
Doctors = pd.read_csv('ProviderList.csv')
matches = Doctors['Last'].isin(file)
Doctors[matches]
newDF = Doctors[matches]
newDF.to_csv('TargetDoctors.csv')
