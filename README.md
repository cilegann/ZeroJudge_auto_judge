[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[![MIT Licence](https://badges.frapsoft.com/os/mit/mit.svg?v=103)](https://opensource.org/licenses/mit-license.php)
# ZeroJudge_auto_judge
:100:zerojudge自動評分
抓取特定ID在特定題目上的AC情形


## Getting Started


### Prerequisites

```
python 3.5 or above
requests 2.18 or above
beautifulsoup4 4.6.0 or above
```

### Usage

#### Files to be prepared
```
3 files to modify:

* accout
the accouts to be judged. Delimiters = ','

* todo
the id of problems to be judged. Delimiters = ','

* login
A valid account and its password of Zerojudge. Delimiters = ','
```
#### Run program
```
python3 judge.py account todo <outputfile.csv>
```

## Authors

* **Yu-Hsuan Chiu (Sean)** - [cilegann](https://github.com/cilegann)

## License

This project is licensed under the MIT License
