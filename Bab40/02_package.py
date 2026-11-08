import sys
import platform
import matplotlib
import pandas
import sklearn

print("Python:", sys.version.split()[0])
print("Platform:", platform.system())
print("Matplotlib:", matplotlib.__version__)
print("Pandas:", pandas.__version__)
print("scikit-learn:", sklearn.__version__)
