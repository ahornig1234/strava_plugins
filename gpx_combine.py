import sys

def main():
  '''Given two filenames as arguments, appends the 2nd to the 1st.
     Metadata and gpx info is taken from 1st file. Activity name is defaulted to
     the name from 1st file but this can be specified as 3rd argument. Filename 
     of output is default to 'combined_gpx' but this can be specified as a 4th
     argument.'''
  
  try:
    file1 = sys.argv[1]
    file2 = sys.argv[2]
  except:
    sys.exit("Error, needs 2-4 args of the form file1, file2,\
              activityname=" ", filename = 'combined.gpx'")

  #set default values
  assert len(sys.argv)<=5,"Too many args!"
  if len(sys.argv) ==5:
    filename = sys.argv[4]
  else:
    filename = 'combined.gpx'

  if len(sys.argv) >= 4:
    activityname  =sys.argv[3]
  else:
    activityname = " "

  #open file 1
  try:
    f1 = open(file1, 'r')
  except:
    sys.exit("Can not open " + file1)

  #open file 2
  try:
    f2 = open(file2, 'r')
  except:
    sys.exit("Can not open " + file2)

  #open output file
  f3 = open(filename, 'w')

#  #write generic header
#  f3.write('<?xml version="1.0" encoding="UTF-8"?>\n')
#  f3.write('<gpx creator="StravaGPX" version="1.1"'
#            ' xmlns="http://www.topografix.com/GPX/1/1"'
#            ' xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"'
#            ' xsi:schemaLocation="http://www.topografix.com/GPX/1/1'
#            ' http://www.topografix.com/GPX/1/1/gpx.xsd">\n')

  #go through file1 and get needed info
  get_metadata = True
  get_activityname = False
  findname = (activityname == " ")
  get_gpsdata = False
  for line in f1:
    #copy metadata from file1
    if '</metadata>' in line.strip():
      get_metadata = False
      f3.write(line)
      f3.write(' <trk>\n')
      #put in activityname after metadata if specified as arg
      if not findname:
        f3.write('  <name>'+activityname+'</name>\n')
        f3.write('  <trkseg>\n')
    elif get_metadata:
      f3.write(line)

    #get activityname from file1 if not specified as arg
    if findname:
      if '<name>' in line.strip():
        f3.write(line)
        if '</name>' not in line.strip():
          get_activityname = True
        else: f3.write('  <trkseg>\n')
      elif '</name>' in line.strip():
        get_activityname = False
        f3.write(line)
        f3.write('  <trkseg>\n')
      elif get_activityname:
        f3.write(line)

    #get the rest
    if  '<trkseg>' in line.strip() and not get_gpsdata:
      get_gpsdata = True
    elif '</trkseg>' in line.strip():
      get_gpsdata = False
    elif get_gpsdata:
      f3.write(line)
  
  #go through file2 and get needed info
  get_gpsdata = False
  for line in f2:
    if  '<trkseg>' in line.strip() and not get_gpsdata:
      get_gpsdata = True
    elif '</trkseg>' in line.strip():
      get_gpsdata = False
    elif get_gpsdata:
      f3.write(line)


  f3.write('  </trkseg>\n')
  f3.write(' </trk>\n')
  f3.write('</gpx>')


  f1.close()
  f2.close()
  f3.close()

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
if __name__ == "__main__":
  main()

