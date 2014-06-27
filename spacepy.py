import os
os.putenv("CDF_LIB", "~/CDF/lib") #this is location which installed cdf library
from spacepy import pycdf

def main():
	print "This is test code of SpacePy modules."
	if not args or len(args) != 1:
        return 0
    CDF = args[0]
    cdf=pycdf.CDF(CDF)
    print "Information CDF"
    ReadCDF(cdf)
    print "Global Attributes"
    OutGA(cdf)

def ReadCDF(cdf):
	print(cdf)
	cdf.close()
def OutGA(cdf):
	ga=cdf.attr
	print(ga)

if __name__=='__main__':
	main()
