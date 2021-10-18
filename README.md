# korea-patent-parser
Parser for patent data by KIPO
Supports downloading patent data ZIP file from [here](http://ods.kipris.or.kr/) and transforming XML files to JSON files.

You may need git bash or WSL installed if you use windows.

### Script description

`get_files.py` : Download patent data ZIP file and unzip the file after download it.
`main.py` : Process XML files in a directory generated after running `get_files.py` and storing them into json files.

### Before use this script

1. Install `virtualenv` package - optional

2. Activate virtual environment - optional
```
source venv/bin/activate - for linux
source venv/Scripts/activate - for windows
```

3. Install packages
```
pip install -r requirements.txt
```
 
 ### How to use this script

1. Run `get_files.py`
```
python get_files.py -d 20210930 -t open
```
If you want to download open document published in 2021-09-30, you can run the above command.

Date argument need to be written in `YYYYMMDD`.

Because of the policy by KIPRIS, you can only download data published less than about a month ago from today. 
```
usage: get_files.py [-h] [-d date] [-c date] [-t type] [-u url]
                    [-o output_path]

Parser for patent by KIPO

optional arguments:
  -h, --help            show this help message and exit
  -d date, --date date
  -c date, --cycle date
  -t type, --type type
  -u url, --url url
  -o output_path, --output output_path
```
2. Run `main.py`
```
python main.py -o "C:\Users\admin\Desktop\projects\KRPUAPBU02_D_20210930"
```
You can extract JSON files from XML files in `-o` or `--output`.

`-o` or `--output` means where the directory of the unzipped data using `get_files.py` is. 

`-o` or `--output` has to be specified.
```
usage: main.py [-h] [-o output_path]

Parser for patent by KIPO

optional arguments:
  -h, --help            show this help message and exit
  -o output_path, --output output_path
```
Output json file will be like below.
```
{"title": "특히 불임 치료를 위한 노화 방지제로서의 니코틴아미드 모노뉴클레오타이드의 무기 염", "application_num": "10-2020-7036089", "application_date": "2019-05-15", "open_num": "-", "open_date": "2021-09-30", "reg_num": "-", "reg_date": "-", "applicant": ["점프스타트 퍼틸리티 피티와이 엘티디", "라이프 바이오사이언스 인코포레이티드"], "inventor": ["마르쿠치오, 세바스찬 마리오", "조이스, 로한 데이비드", "와티에, 마이클", "돌레, 롤랜드", "터커, 시몬"], "summary": "\n본 발명은 NAD+의 결핍과 관련된 장애 및 질환의 치료에 유용한 니코틴아미드 모노뉴클레오타이드의 무기 염 및 화학식 (I)의 조성물에 관한 것이다:\n\n상기 식에서, A, M1, k, R1 및 R2은 본원에서 기재된 바와 같다.\n"}
{"title": "볼 조인트 제조 방법 및 상기 방법에 따른 볼 조인트", "application_num": "10-2021-0002280", "application_date": "2021-01-08", "open_num": "-", "open_date": "2021-09-30", "reg_num": "-", "reg_date": "-", "applicant": ["젯트에프 프리드리히스하펜 아게"], "inventor": ["나흐바어 프랑크", "그루베 폴커", "팝스트 얀"], "summary": "\n본 발명은, 조인트 하우징(2)과; 조인트 볼(4)을 구비한 조인트 내측 부재(3);를 가진 볼 조인트(1, 20, 21)를 제조하는 방법에 관한 것으로, 이 방법에서는 삽입 단계에서 조인트 내측 부재(3)의 조인트 볼(4)이 조인트 하우징(2)의 볼 수용부(6) 내에 배치되고, 볼 수용부(6) 내에 조인트 볼(4)을 배치한 후에 조인트 볼(4)과 이 조인트 볼(4)의 방향으로 향해 있는 볼 수용부(6)의 내면(11) 사이에 자유 공간(22)이 잔존하며, 후속 충전 단계에서 자유 공간(22)이 플라스틱 재료로 충전되고, 그럼으로써 볼 수용부(6)의 내면(11)과 조인트 볼(4) 사이에 플라스틱층(8)이 형성된다.  이미 볼 조인트(1, 20, 21) 자체의 제조 시, 그리고 추가 조인트 수용 부품의 조인트 수용부 내로 볼 조인트(1, 20, 21)를 압입할 필요 없이 기설정된 조인트 예압의 조정을 가능하게 하기 위해, 상기 볼 조인트 제조 방법은, 후속 폐쇄 단계에서 폐쇄 부재(15)가 조인트 하우징(2)의 하우징 개구부(7) 내에 배치되며, 폐쇄 부재(15)에 의해 힘이 플라스틱층 내로 유도되는 것을 특징으로 한다.\n"}
{"title": "라벨링 모델을 구축하는 방법, 장치, 전자 기기, 프로그램 및 판독 가능 저장 매체", "application_num": "10-2021-0012424", "application_date": "2021-01-28", "open_num": "-", "open_date": "2021-09-30", "reg_num": "-", "reg_date": "-", "applicant": ["베이징 바이두 넷컴 사이언스 앤 테크놀로지 코., 엘티디."], "inventor": ["쉬, 씬차오", "왕, 하이펑", "우, 화", "리우, 짠이"], "summary": "\n본 출원은 라벨링 모델을 구축하는 방법, 장치, 전자 기기 및 판독 가능 저장 매체를 개시하는바, 자연 언어 처리의 기술 분야에 관한 것이다. 본 출원의 라벨링 모델을 구축할 때 사용하는 실현 방안은, 텍스트 데이터를 취득하고, 각 텍스트 데이터 중의 라벨링 대기 단어를 결정하며; 상기 라벨링 대기 단어에 기반하여 각 텍스트 데이터가 단어 교체 태스크에 대응하는 제1 트레이닝 샘플 및 라벨링 태스크에 대응하는 제2 트레이닝 샘플을 구성하고; 상기 단어 교체 태스크 및 상기 라벨링 태스크의 손실 함수가 미리 결정된 조건을 만족시킬 때까지, 상기 제1 트레이닝 샘플 및 상기 제2 트레이닝 샘플을 각각 사용하여 뉴럴 네트워크 모델을 트레이닝하여 라벨링 모델을 얻는 것이다. 본 출원은 라벨링 모델의 단어를 라벨링하는 정확성을 향상시킬 수 있고, 라벨링 모델이 다양한 라벨링 시나리오에 적응할 수 있도록 한다.\n"}
{"title": "성형 장치를 운용하기 위한 성형 방법", "application_num": "10-2021-0017025", "application_date": "2021-02-05", "open_num": "-", "open_date": "2021-09-30", "reg_num": "-", "reg_date": "-", "applicant": ["킹 스틸 머쉬너리 씨오., 엘티디."], "inventor": ["예 량-후이", "첸 칭-하오", "리 이-충"], "summary": "\n[과제] 성형 장치를 운용하기 위한 성형 방법의 제공.\n[해결수단] 본 발명의 성형 방법은, 제1 금형과, 상기 제1 금형에 대응하는 제2 금형을 포함하는 성형 장치를 제공하는 공정과, 상기 제1 금형을 상기 제2 금형을 향하여 이동시켜, 제1 금형 캐비티를 형성하는 공정과, 상기 제1 금형 캐비티에 기체를 공급하는 공정과, 상기 제1 금형 캐비티에 재료를 주입하는 공정과, 상기 제1 금형을 상기 제2 금형으로부터 이격되게 이동시켜, 제2 금형 캐비티를 형성하고, 상기 기체의 적어도 일부를 상기 성형 장치로부터 배출하는 공정을 포함하며, 그 중, 상기 제1 금형 캐비티의 제1 부피가, 상기 제2 금형 캐비티의 제2 부피보다 실질적으로 작다.\n"}

```
