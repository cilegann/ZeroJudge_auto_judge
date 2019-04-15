# ZeroJudge_auto_judge

[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[![MIT Licence](https://badges.frapsoft.com/os/mit/mit.svg?v=103)](https://opensource.org/licenses/mit-license.php)

自動抓取[zerojudge](https://zerojudge.tw)中，特定使用者在特定題目上的AC情形

## Attention please
目前網站新增了 google recaptcha v3 機制，尚未解決此問題

## Getting Started


### Prerequisites

```
python 3.5 or above
requests 2.18 or above
```
You can simply run ```pip3 install -r requirements.txt``` to install these required packages

### Usage

#### Files to be prepared
```
2 files to modify:

* accouts file (Put it in src/data/)
the accouts to be judged. Delimiters = ','

* problemIDs file (Put it i src/data/)
the id of problems to be judged. Delimiters = ','

```
#### Run program
```
cd src
python3 judge.py <your_accounts_file_name_in_data_folder> <your_problemIDs_file_name_in_data_folder> <path_to_output_file>
```

## Author

* **Yu-Hsuan Chiu (Sean)** - [cilegann](https://seanchiu.cf)

## License

This project is licensed under the MIT License
