# Onomastics
Resources used in project to identify targets doctors by last name

## What is onomastics?
Onomastics is the branch of linguistics concerned with studying the 
etymology, history, and use of proper names.

## Why is onomastics useful?
Identifying proper names that originate from similar areas of the world can
be useful in identifying people who speak similar languages or who may have 
shared cultural experiences. 

## How did this project come to be?
In my position as a Researcher, I was tasked to identify from a list of 
50k+ doctors those with last names originating in a specific area of the
world.  Rather than manually search through the entire database of doctors 
by hand, cross referencing a list of 374 common surnames, I created a 
python script to automatically filter a pandas dataframe (the original 
doctor list in csv format) by the 374 common surnames, saving a new csv 
file into the working directory containing only doctors with target names.

## Files in the Repository
- filtering_dataframe_by_list.py 
  - Simple python script to filter a dataframe by a provided text list
- ProviderList.csv
  - Fictional provider list to test script
- ChineseNames.txt
  - A list of 374 common Chinese surnames

### A Note on Name Lists
- Additional name lists will be added for other areas of the world
- The Chinese names are a collection of romanizations for the most common
  Mandarin and Cantonese names (multiple spellings).  This list has been
  curated for duplicates.
