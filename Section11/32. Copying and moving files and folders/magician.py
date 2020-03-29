import os
import shutil
shutil.move(os.path.abspath(".\\inside hat\\rabbit.txt"), os.path.abspath(".\\outside hat\\rabbit.txt"))

os.system("pause")