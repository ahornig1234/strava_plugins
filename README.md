# Strava Plugins

This is an ongoing work which contains various python scripts that manipulates
strava (and other gpx) files. The following are currently running:

### gpx_combine.py

Given two filenames as arguments, appends the 2nd to the 1st.
Metadata and gpx info is taken from 1st file. Activity name is defaulted to
the name from 1st file but this can be specified as 3rd argument. Filename 
of output is default to 'combined.gpx' but this can be specified as a 4th
argument.

```python gpx_combine.py file1.gpx file2.gpx [activity name = name_from_file1] [output = "combined.gpx"]```

### gpx_stripper.py

Given a filename (.gpx), strips all cadence and heart rate data. Output defaults to "filename_stripped.gpx" but this can be specified as 2nd argument. Can change activity name by giving a 3rd argument. 

```python gpx_strip_HR.py file.gpx [output = "file_stripped.gpx"] [activity name = name_from_file]```
