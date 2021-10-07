import argparse
import get_files


def main(args):
    print(args)
    if(args.download):
        get_files.download_file(args)
        get_files.unzip_file(args)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Parser for patent by KIPO')
    # Date patent data published
    parser.add_argument('-d', '--date', metavar='date', type=str)
    # Cycle type of patent data // A day is default
    parser.add_argument('-c', '--cycle', metavar='date',
                        type=str, default="d", nargs=1)
    # Document type of patent data // Either 'open' or 'reg' is allowed
    parser.add_argument('-t', '--type', metavar='type',
                        type=str, choices=['open', 'reg'])
    # Url of the site
    parser.add_argument('-u', '--url', metavar="url", type=str,
                        default="ods.kipris.or.kr/ods/KpodsFileDown.do")
    # Path of the downloaded compressed file
    parser.add_argument('-o', '--output', metavar="output_path", type=str)
    # If file is already downloaded and don't want to do it again, use this option.
    parser.add_argument('--no_download', dest="download",
                        action="store_false")

    args = parser.parse_args()
    main(args)
