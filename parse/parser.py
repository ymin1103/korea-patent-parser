import glob
import os
import json
from collections import deque
from typing import Deque, List
from typing import Dict
import bs4

delemeter = "\\" if os.name == "nt" else "/"


class KoreanPatentParser():
    """
    ## Parser for free-access korean patent data by KIPO formatted in ST36
    It can only process the data from `ods.kipris.or.kr` right now.
    ### Attributes
    - `id`: Id of the `KoreanPatentParser` instance is from `path`.
        - For example, if `path` is `/c/Users/admin/Desktop/My Projects/KRPUAPBU02_D_20210930`, `id` will be like `KRPUAPBU02_D_20210930`
    - `path`: Name of the directory to be processed.
        - For example, it can be like `/c/Users/admin/Desktop/My Projects/KRPUAPBU02_D_20210930`
    - `json_path`: Path of processed json file stored. Same with `path`.
    - `encoding`: Encoding system of the xml file to be processed. It should be `euc-kr`
    - `capacity`: Max capacity of the waiting queue. Default value is 100
    - `waiting_queue`: Store xml file paths to be processed
    - `processed_queue`: Store processed json file to be comsumed
    - `xml_list_path`:
        - We need txt file with the xml file paths to be processed.
        - And KIPRIS will provide the txt file named like `KR_OPN_20210930_XMLLIST.txt`
        - Its absolute path will be stored in `xml_list_path`.
    """

    def __init__(self, id, path, capacity=100):
        self.id = id
        self.path = path
        self.json_path = path
        self.encoding = "euc-kr"
        self.capacity = capacity
        self.waiting_queue = deque([])
        self.processed_queue = deque([])
        self.xml_list_path = glob.glob(f"{self.path}/**/*_XMLLIST.txt")[0]

        if not os.path.isdir(self.json_path):
            os.mkdir(self.json_path)

    def add_xml_strings_to_wating_queue(self):
        """
        Add xml path strings in `self.xml_list_path` to `self.waiting_queue`.
        """
        with open(self.xml_list_path, encoding=self.encoding) as xml_list_path:
            while True:
                d = self.path.split(delemeter)[-1].split("_")[-1]
                xml_file_name = xml_list_path.readline().rstrip()[2:].replace(
                    "/", delemeter).replace("\\", delemeter)
                xml_file_path = f"{self.path}{delemeter}{d}{delemeter}{xml_file_name}"
                if xml_file_name == "":
                    break
                self.waiting_queue.append(xml_file_path)

    def publish_to_processed_queue(self):
        """
        Consume the `self.waiting_queue` and publish to the `self.processed_queue` until the `self.waiting_queue` get empty.
        """
        while self.waiting_queue:
            if len(self.processed_queue) >= self.capacity:
                print("Exceeded Capacity of Queue. Please consume the processed queue")
                return

            xml_file_path = self.waiting_queue.popleft()
            parsed_json = self.process_xml_string(xml_file_path)
            self.processed_queue.append(parsed_json)

    def consume_processed_queue(self):
        """
        Consume the `self.processed_queue`.

        Following operation may be executed.
        - Writing in json file
        - Publish to Message Queue
        - And other operations
        """
        if not self.processed_queue:
            return
        processed_jsons = deque([])
        for _ in range(len(self.processed_queue)):
            processed_jsons.append(self.processed_queue.popleft())
        json_file_path = f"{self.json_path}{delemeter}{self.id}_{processed_jsons[0]['application_num']}.json"
        self.write_to_json_file(json_file_path, processed_jsons)

    def process_xml_string(self, xml_file_path: str) -> Dict[str, any]:
        parsed_json = {}
        with open(xml_file_path, encoding=self.encoding, errors="ignore") as file_string:
            s = file_string.read()
            soup = bs4.BeautifulSoup(s, "lxml")
            parsed_json['title'] = self.get_title(soup)

            parsed_json["application_num"] = self.get_number(
                soup, "kr_applicationnumber")
            parsed_json["application_date"] = self.get_date(
                soup, "kr_applicationdate")

            parsed_json["open_num"] = self.get_number(soup, "kr_opennum")
            parsed_json["open_date"] = self.get_date(soup, "kr_opendate")

            parsed_json["reg_num"] = self.get_number(soup, "kr_regnum")
            parsed_json["reg_date"] = self.get_date(soup, "kr_regdate")

            parsed_json["applicant"] = self.get_names(
                soup, "kr_applicantinformation")

            parsed_json["inventor"] = self.get_names(
                soup, "kr_inventorinformation")

            parsed_json['summary'] = self.get_summary(soup)
        return parsed_json

    def write_to_json_file(self, file_path: str, processed_jsons: Deque):
        with open(file_path, "w", encoding="utf-8") as json_fp:
            while processed_jsons:
                processed_json = processed_jsons.popleft()
                json_fp.write(json.dumps(processed_json,
                                         ensure_ascii=False) + "\n")

    def get_title(self, soup: bs4.BeautifulSoup) -> str:
        return soup.find("kr_inventiontitle").text

    def get_number(self, soup: bs4.BeautifulSoup, tag_name: str) -> str:
        application_number_soup = soup.find(tag_name)
        if application_number_soup:
            return application_number_soup.text
        else:
            return "-"

    def get_date(self, soup: bs4.BeautifulSoup, tag_name: str) -> str:
        application_date_soup = soup.find(tag_name)
        if application_date_soup:
            return application_date_soup.text.replace("년", "-").replace("월", "-").replace("일", "")
        else:
            return "-"

    def get_names(self, soup: bs4.BeautifulSoup, tag_name: str) -> List[str]:
        names = []
        applicant_soups = soup.find_all(tag_name)
        for applicant_soup in applicant_soups:
            applicant_name_soup = applicant_soup.find(
                "kr_orgname") or applicant_soup.find("kr_name")
            if applicant_name_soup:
                names.append(applicant_name_soup.text)
        return names

    def get_summary(self, soup: bs4.BeautifulSoup) -> str:
        summary = ""
        summary_soup = soup.find('summary')
        if summary_soup:
            return summary_soup.text
        else:
            return summary

    def get_claims(self, soup: bs4.BeautifulSoup) -> List[str]:
        claim_text_soup = soup.find_all("claim-text")
        if claim_text_soup:
            return [e.text for e in claim_text_soup]
        else:
            return []
