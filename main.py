import argparse
import parse.parser
import os
import re

delemeter = r'\'' if os.name == "nt" else r'/'


def main(args):
    """
    Process the xml files in directory in argument

    1. Add xml file paths to waiting queue
    2. Consume the waiting queue and publish to the processed queue 
    3. Comsume the processed queue
    """
    print(args)
    koreanParser = parse.parser.KoreanPatentParser(
        id=re.sub('[\\/]', delemeter, args.directory).split(delemeter)[-1],
        path=args.directory)
    koreanParser.add_xml_strings_to_wating_queue()
    while(koreanParser.waiting_queue):
        koreanParser.publish_to_processed_queue()
        koreanParser.consume_processed_queue()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Parser for patent by KIPO')
    # Path of the uncompressed folder with patent data
    parser.add_argument('-d', '--directory',
                        metavar="directory_path", type=str)
    args = parser.parse_args()
    main(args)
