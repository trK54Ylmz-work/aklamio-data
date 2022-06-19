from report import MeanReport
from source import ParquetSource
from util import config

if __name__ == '__main__':
    # create parquet data frame reader for yellow and green taxis
    ys = ParquetSource(config.source.yellow)
    gs = ParquetSource(config.source.green)

    report = MeanReport(ys, gs)

    # generate report
    result = report.generate()

    print(result)
