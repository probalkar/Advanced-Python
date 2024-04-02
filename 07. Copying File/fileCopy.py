# copyfile() : copies contents of a file
# copy() : copyfile() + permission mode + destination can be directory
# copy2() : copy() + copies metadata (file's creation and modification time)

import shutil
shutil.copyfile('07. Copying File\\sample.txt', '07. Copying File\\copy.txt')