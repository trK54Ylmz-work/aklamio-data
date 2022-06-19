import requests as r
from pandas import DataFrame


class Source:
    def __init__(self, url: str) -> None:
        """
        Remote file source

        :param str url: remote file url
        """
        self.url = url

    def read(self) -> DataFrame:
        """
        Read parquet data frame from remote url

        :return: pandas data frame
        :rtype: pandas.DataFrame
        """
        raise NotImplementedError

    def download(self) -> str:
        """
        Download file from remote url

        :return: local file path
        :rtype: str
        """
        name = self.url.split('/')[-1]
        path = '/tmp/' + name

        f = open(path, 'wb')

        # send request to remote url
        res = r.get(self.url, stream=True)

        # iterate over content for 1 mb
        for c in res.iter_content(chunk_size=1024 * 1024):
            # write downloaded bytes into the file
            f.write(c)

        f.close()

        return path
