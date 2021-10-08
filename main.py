import argparse
import parse.parser
import os

delemeter = "\\" if os.name == "nt" else "/"


def main(args):
    print(args)
    koreanParser = parse.parser.KoreanPatentParser(
        id=args.output.split(delemeter)[-1], path=args.output)
    koreanParser.add_xml_strings_to_wating_queue()
    while(koreanParser.waiting_queue):
        koreanParser.publish_to_processed_queue()
        koreanParser.consume_processed_queue()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Parser for patent by KIPO')
    # Path of the uncompressed folder with patent data
    parser.add_argument('-o', '--output', metavar="output_path", type=str)
    args = parser.parse_args()
    main(args)
