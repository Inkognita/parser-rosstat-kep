"""Extract dataframes by year and month."""

from kep import FREQUENCIES, PARSING_DEFINITION
from kep.csv2df.dataframe_maker import Datapoints
from kep.df2xl.to_excel import save_xls
from kep.helper.date import Date
from kep.helper.path import InterimCSV, ProcessedCSV
from kep.validation.checkpoints import CHECKPOINTS, validate


class Vintage:
    """Represents dataset release for a given year and month.
        Performs interim CSV file parsing on construction and obtains 
        resulting dataframes.
    """
    def __init__(self, year: int, month: int, parsing_definition=PARSING_DEFINITION):
        self.year, self.month = year, month
        csv_text = InterimCSV(year, month).text()
        parsing_definition.attach_data(csv_text)
        self.emitter = Datapoints(parsing_definition.tables)
        self.dfs = {freq: self.emitter.get_dataframe(freq) for freq in FREQUENCIES}

    @property
    def datapoints(self):        
        return self.emitter.datapoints

    def save(self, folder=None):
        csv_processed = ProcessedCSV(self.year, self.month, folder)
        for freq, df in self.dfs.items():
            path = csv_processed.path(freq)
            # Convert 1524.3999999999996 back to 1524.4
            # Deaccumulation procedure in parser.py responsible  
            # for float number generation. 
            # WONTFIX: the risk is loss of data for exchange rate, 
            #          may need fomatter by column. annual values can be
            #          a guidance for a number of decimal positions.
            df.to_csv(path, float_format='%.2f')
            print("Saved dataframe to", path)

    def validate(self):
        for freq in FREQUENCIES:
            df = self.dfs[freq]
            checkpoints = CHECKPOINTS[freq]
            validate(df, checkpoints)
        print("Test values parsed OK for", self)

    def __repr__(self):
        return "Vintage({}, {})".format(self.year, self.month)


class Latest(Vintage):
    """Operations on most recent data release."""

    def __init__(self, year: int, month: int):
        # protect from using old releases of data
        Date(year, month).assert_latest()
        super().__init__(year, month)

    def upload(self):
        from parsers.mover.uploader import Uploader
        self.validate()        
        # FIXME: possible risk - *self.datapoints* may have different serialisation 
        #        format compared to what Uploader() expects
        #           (a) date format   
        #           (b) extra keys in dictionary
        Uploader(self.datapoints).post()

    def save(self, folder=None):
        ProcessedCSV(self.year, self.month).to_latest()

    def to_excel(self):
        save_xls()


if __name__ == "__main__": # pragma: no cover
    v = Vintage(2017, 12)
    v.validate()
    v.save()
    # Expected output:
    # Test values parsed OK for Vintage(2016, 10)

    import pandas as pd
    # TODO: convert to test for to_csv(), hitting deaccumulation procedure
    assert pd.DataFrame([{'a': 1}]).to_csv(float_format='%.2f') == ',a\n0,1\n'
    assert pd.DataFrame([{'a': 1.0005}]).to_csv(float_format='%.2f') == ',a\n0,1.00\n'
