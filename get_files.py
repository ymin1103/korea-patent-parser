import subprocess
from typing import List


def unzip_file(args):
    folder_path = args.output[:-4]
    expression = args.output[-3:]
    if(expression.lower() == "zip"):
        command = f"unzip {args.output} -d {folder_path}"
    subprocess.run(command)


def get_product_code(args) -> str:
    codes = {
        "open": "KRPUAPBU02",
        "reg": "KRPUGDBU02"
    }
    return codes[args.type]


def get_attach_file_id(args) -> str:
    product_code = get_product_code(args)
    return f"{product_code}_{args.date}{args.cycle.upper()}"


def get_file_name(args) -> str:
    product_code = get_product_code(args)
    return f"{product_code}_{args.cycle.upper()}_{args.date}"


def download_file(args):
    product_code = get_product_code(args)
    attached_file_id = get_attach_file_id(args, product_code)
    file_name = get_file_name(args, product_code)
    params = {
        "atchFileId": attached_file_id,
        "productCd": product_code,
        "fileNm": file_name
    }
    flatized_params = "&".join([f"{k}={v}" for k, v in params.items()])
    command = f"curl -XGET {args.url}?{flatized_params} -o {args.output}"
    print(command)
    subprocess.run(command)
