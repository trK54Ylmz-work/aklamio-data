from pandas import DataFrame


class Report:
    def generate(self) -> DataFrame:
        """
        Generate report from pandas data frame(s)

        :return: report as pandas data frame
        :rtype: pandas.DataFrame
        """
        raise NotImplementedError
