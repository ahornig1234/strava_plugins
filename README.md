# Strava Plugins

This is an ongoing work which contains various python scripts that manipulates
strava (and other gpx) files. The following are currently running:

### gpx_combine.py

Given two filenames as arguments, merges the 2nd after the 1st.
Metadata is taken from 1st file. Activity name is defaulted to the name
1st file but this can be specified as 3rd argument. Filename of output  is 
default to 'combined_gpx' but this can be specified as a 4th argument.

```python gpx_combine.py file1.gpx file2.gpx [activity name = name_from_file1] [output = "combined.gpx"]```
