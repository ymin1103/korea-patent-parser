import subprocess
import argparse
import os
from typing import List

delemeter = "\\" if os.name == "nt" else "/"


def unzip_file(zip_file_path):
    """
    Unzip the zip file.

    absolute path of the zip file is needed.
    """
    folder_path = f"\"{zip_file_path[1:-5]}\""
    command = f"unzip {zip_file_path} -d {folder_path}"
    subprocess.run(command)
    print(f"Unzipped file in {folder_path}")


def get_product_code(args) -> str:
    """
    Return the product code of the file to be downloaded
    """
    codes = {
        "open": "KRPUAPBU02",
        "reg": "KRPUGDBU02"
    }
    return codes[args.type]


def get_attach_file_id(args) -> str:
    """
    Return the file id to be downloaded
    """
    product_code = get_product_code(args)
    return f"{product_code}_{args.date}{args.cycle.upper()}"


def get_file_name(args) -> str:
    """
    Return the file name to be downloaded
    """
    product_code = get_product_code(args)
    return f"{product_code}_{args.cycle.upper()}_{args.date}"


def download_file(args) -> str:
    """
    Download patent data ZIP file with options in argument

    Return absolute path of the downloaded ZIP file.
    """
    product_code = get_product_code(args)
    attached_file_id = get_attach_file_id(args)
    file_name = get_file_name(args)
    params = {
        "atchFileId": attached_file_id,
        "productCd": product_code,
        "fileNm": file_name
    }
    flatized_params = "&".join([f"{k}={v}" for k, v in params.items()])
    command = f"curl -XGET {args.url}?{flatized_params} -o \"{args.output}{delemeter}{file_name}.zip\""
    subprocess.run(command)
    return f"\"{args.output}{delemeter}{file_name}.zip\""


def main(args):
    print(args)
    zip_file_path = download_file(args)
    unzip_file(zip_file_path)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Parser for patent by KIPO')
    # Date patent data published
    parser.add_argument('-d', '--date', metavar='date', type=str)
    # Cycle type of patent data // A day is only available now
    parser.add_argument('-c', '--cycle', metavar='date',
                        type=str, default="d", choices=["d"])
    # Document type of patent data // Either 'open' or 'reg' is allowed
    parser.add_argument('-t', '--type', metavar='type',
                        type=str, choices=['open', 'reg'])
    # Url of the site
    parser.add_argument('-u', '--url', metavar="url", type=str,
                        default="ods.kipris.or.kr/ods/KpodsFileDown.do")
    # Path of the downloaded compressed file
    parser.add_argument('-o', '--output', metavar="output_path",
                        type=str, default=delemeter.join(
                            os.path.abspath(__file__).split(delemeter)[:-2])
                        )
    args = parser.parse_args()
    main(args)
