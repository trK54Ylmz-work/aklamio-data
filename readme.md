## Aklamio report example

Hi, This report example for the Aklami's Senior Python Engineer position created by Tarik Yilmaz (trk54ylmz @ Github)

This repository contains simple Pandas functions such as group by, join, filtering etc.

**Note** I haven't used Docker compose etc. because the was no any orchestration needs.

### Install

Please install dependencies by using `pip`,

```bash
$ pip install -r requirements.txt
```

### Usage

Please run `app.py` file to generated report,

```bash
$ python3 app.py default.ini
```

Expected output should be like,

```text
2022-06-19 16:04:50,065 INFO     util.log [parquet.py:14] The file downloading from https://nyc-tlc.s3.amazonaws.com/trip+data/yellow_tripdata_2022-01.parquet
2022-06-19 16:05:03,046 INFO     util.log [parquet.py:14] The file downloading from https://nyc-tlc.s3.amazonaws.com/trip+data/green_tripdata_2022-01.parquet

   VendorID  distance_first  distance_second
0         1        5.601086         4.359446
1         2        5.765933         8.883586
```

### Code quality

You can test the code by using `flake8` and `pylint`,

```bash
$ flake8 . --count --max-complexity=20 --max-line-length=100 --statistics
$ pylint_runner
```
