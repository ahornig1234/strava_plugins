import sys, re

def main():
  '''Given a filename (.gpx), strips all cadence and heart rate data. Output defaults to "filename_stripped.gpx" but this can be specified as 2nd argument. Can change activity name by giving a 3rd argument. '''
  
  try:
    input = sys.argv[1]
  except:
    sys.exit("Error, needs 1-2 args of the form file-input, \
file-output = 'file-input_stripped.gpx'")

  #set default values
  assert len(sys.argv) <=4,"Too many args!"
  if len(sys.argv) == 2:
    output = input.rsplit(".", 1 )[0] + '_stripped.gpx'
  if len(sys.argv) >= 3:
    output = sys.argv[2]
  if len(sys.argv) == 4:
    activityname = sys.argv[3]
    replace_activityname = True
  else:
    replace_activityname = False



  #open input file
  try:
    f_in = open(input, 'r')
  except:
    sys.exit("Can not open " + input)

  #open output file
  f_out = open(output, 'w')


  #go through input and strip
  get_activityname = False
  for line in f_in:
    #remove HR and Cadence
    if not '<gpxtpx:hr>' in line.strip() and not '<gpxtpx:cad>' in line.strip():
    #replace activityname if user gives a replacement
      if replace_activityname:
        f_out.write(re.sub(r'.*<name>.*</name>',
          '  <name>'+activityname+'</name>', line))
      else:
        f_out.write(line)

  f_in.close()
  f_out.close()

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
if __name__ == "__main__":
  main()

