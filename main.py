import argparse
import get_files


def main(args):
    print(args)
    if(args.download):
        get_files.download_file(args)
        get_files.unzip_file(args)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Parser for patent by KIPO')
    # Path of the uncompressed folder with patent data
    parser.add_argument('-o', '--output', metavar="output_path", type=str)
    args = parser.parse_args()
    main(args)
