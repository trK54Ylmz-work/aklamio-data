import numpy as np
import pandas as pd
from .report import Report
from source import Source


class MeanReport(Report):
    def __init__(self, first: Source, second: Source) -> None:
        """
        Create mean report based on two taxi types

        :param source.Source first: the first data frame source
        :param source.Source second: the second data frame source
        """
        self.first = first
        self.second = second

    def clean(self, df: pd.DataFrame, new_name: str) -> pd.DataFrame:
        """
        Prepare data frame by using cleaning

        :param pandas.DataFrame df: raw data frame
        :param str new_column: new column name for aggregated column
        :return: cleaned data frame
        :rtype: pandas.DataFrame
        """
        # filter out if passenger count is null and trip distance is greater and equals to 2 kms
        fltr = (~pd.isna(df.passenger_count)) & (df.trip_distance >= 2)

        # apply filtering on data frame
        fdf = df[fltr]

        # group data frame by vendor ID and aggregate by trip distance
        grp = fdf.groupby(fdf.VendorID).agg(trip=('trip_distance', np.mean))

        rdf = grp.reset_index()
        rdf.columns = ['VendorID', 'distance_' + new_name]

        return rdf

    def generate(self) -> pd.DataFrame:
        """
        Generate mean report

        :return: report as data frame
        :rtype: pandas.DataFrame
        """
        # read data frames
        first = self.first.read()
        second = self.second.read()

        # clean data frames
        fdf = self.clean(first, 'first')
        sdf = self.clean(second, 'second')

        # merge (join) two data frames for report by vendor ID
        df = fdf.merge(sdf, on='VendorID')

        return df
