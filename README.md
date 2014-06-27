##About SpacePy


SpacePy is useful SpaceScience Library which written by Python.

You can download SpacePy following the URL.
http://spacepy.lanl.gov/download.shtml


##How to use
###First

You should be install these software and lib.

* python2.7(or later)
* distribute
* gcc-gfortran
* blas-devel
* lapack-devel
* numpy
* scipy
* matplotlib

if you want a procedure, following the URL can help you.
http://memo.yomukaku.net/entries/jbRkQkq

Also if you want to use CDF format, you should be install to the CDF Library from ISTP/NASA Homepage.
[NASA/ISTP CDF](http://cdf.gsfc.nasa.gov/ "NASA/ISTP CDF")

###Second

if you have already installed NASA cdf library, then you can use pycdf function.
pycdf function will surely bring about a good result for you.
The following code is declarations for pyCDF.

```
os.putenv("CDF_LIB", "~/CDF/lib") 
from spacepy import pycdf
```

note:"~CDF/lib" is location for CDF library, so you should be change your location.

After that, you can use the pycdf function.

###Third 

SpacePy also can use other format, for example HDF5.
But you need to use h5py like pycdf.

##What's contains this repository

This repository contains sample code of SpacePy.

* spacepy.py...This program contains usage for SpacePy, and sample code.
* README.md...readme

















