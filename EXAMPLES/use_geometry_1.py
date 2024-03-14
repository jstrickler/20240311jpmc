import sys
#       pkg.pkg.module
import alpha.mathlib.geometry as geometry   # find and load geometry.py
#   find alpha/mathlib/geometry.py

# PYTHONPATH
#  folder;folder;folder    Windows
#  folder:folder:folder    Non-Windows   PATH 

# python module loading search algorithm
# 1. current folder
# 2. folders in PYTHONPATH
# 3. folders in sys.prefix/log  (installation folder of Python)
print(f"{sys.prefix = }\n")

for path in sys.path:
    print(path)
print('-' * 60)


a1 = geometry.circle_area(8)
a2 = geometry.rectangle_area(10, 12)
a3 = geometry.square_area(7.9)
print(a1, a2, a3)
