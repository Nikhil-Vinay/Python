import sys, os, re
from optparse import OptionParser

ver = '10/24/2018 v3'

def main(argv):
    global eye 

    # Parse and validate options
    (infile, indir) = parse_options(argv)
    file_path = indir + "/" + infile
    f = open(file_path, "w+")
    f.write("written successfully\n")
    f.close()


def parse_options(argv):
    usage_str = 'Usage: $prog -i FILE [options]'
    desc_str ='''This script is test script to read a file.'''

    parser = OptionParser(usage=usage_str, description=desc_str, version=ver)
    # we can add multiple options of arguments.
    # -i and --input are short and long options example: -i "vin.txt" or --input vin.txt
    parser.add_option('-i', '--input', dest="input_file", default="nik.txt", help="Must specified, your input file")
    parser.add_option('-d', '--dir', dest="input_dir", help="Must specified, your input directory")

    (options, args) = parser.parse_args(argv)

    infile = options.input_file
    indir = options.input_dir

    if not infile:
        parser.error("you must specify your input file\nyou may use -h to see available options.")
    if not os.path.isfile(infile) :  # to check directory, we use isdir
        parser.error("input file " + infile + " not found")
    
    try:
        os.makedirs(indir)
    except OSError:
        choice = raw_input("Output directory already exists, delete? (y/n): ")
        if choice == "y":
            os.system("rm -rf " + indir)
            os.makedirs(indir)
        else:
            print "Delete or specify new directory"

    return (infile, indir)

if __name__ == "__main__":
    main(sys.argv)
