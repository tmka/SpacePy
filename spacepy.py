import os
os.putenv("CDF_LIB", "~/CDF/lib") #this is location which installed cdf library
from spacepy import pycdf

def main():
	print "This is test code of SpacePy modules."
	if not args or len(args) != 1:
        return 0
    CDF = args[0]
    print "Information CDF"
    ReadCDF(CDF)
    print "Global Attributes"
    OutGA(CDF)


def ReadCDF(CDF):
	cdf=pycdf.CDF(CDF)
	print(cdf)

def OutGA():
	continue




if __name__=='__main__':
	main()
