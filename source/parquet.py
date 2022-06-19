import pandas as pd
from .source import Source
from util import logger


class ParquetSource(Source):
    def read(self) -> pd.DataFrame:
        """
        Read parquet data frame from remote url

        :return: pandas data frame
        :rtype: pandas.DataFrame
        """
        logger.info('The file downloading from ' + self.url)

        # download file from selected remote url
        path = self.download()

        # read parquet file from local path
        return pd.read_parquet(path)
