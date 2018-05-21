import glob
import os
import shutil
import sys

src = sys.argv[1]
dest = sys.argv[2]
start = int(sys.argv[3])
end = int(sys.argv[4])

path = os.path.join(src,'*')
files = glob.glob(path)

for i in range(start, end):
    if os.path.isfile(files[i]):
        shutil.copy(files[i],dest)
