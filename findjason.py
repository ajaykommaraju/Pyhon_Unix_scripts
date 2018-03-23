#this program is to recersively traverse to directories and find jason files
import os
#motive is to search "path" in the file and get the line if found
phrase = '"path"'
for root, dirs, files in os.walk("."):
    for file in files:
        if file.endswith(".json"):
            fname = (os.path.join(root, file))
            searchfile = open(fname, "r")
            for line in searchfile:
                if phrase in line:
                    path = fname.split(os.sep)
                    u1 = path[1]
                    # strips of  double quotes
                    u2 = line.split()[1].strip('",')
                    dsep = '/'
                    #below lines strips leading and trailing/ with everything behind it
                    u3 = u2.strip('/').split(dsep, 1)[0]
                    print " Name of the service:", u3
                    url = 'https://'
                    print ( url + u1 + u2 )
            searchfile.close()
