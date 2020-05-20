### nc_covid_by_zip
Utility to look up number of cases by zip code. 
 
This script performs the equivalent of going to https://covid19.ncdhhs.gov/dashboard#zip-code-map
zooming in, and then clicking on your zip code to retrieve the number of cases.
 
## Requirements
- Python requests module
 
```buildoutcfg
pip install requests
``` 
 
## Usage
```
bash-3.2$ python nc_covid_by_zip.py --h
usage: nc_covid_by_zip.py [-h] [-z ZIP]

optional arguments:
  -h, --help         show this help message and exit
  -z ZIP, --zip ZIP  NC ZIP CODE
```
## Output
```
bash-3.2$ python nc_covid_by_zip.py --zip 27502

*-------------------------------------------------------------------*
Number of cases on 2020-05-19 20:18:25 EDT in zip code 27502 is: 47
This is about 0.11% of the 43747 residents in Apex
*-------------------------------------------------------------------*


```
