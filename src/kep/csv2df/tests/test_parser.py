﻿import itertools

import pandas as pd
import pytest

# testing
from kep.csv2df.parser import Table, split_to_tables, extract_tables, HeaderParsingProgress
from kep.csv2df.parser import timestamp_quarter, timestamp_month, timestamp_annual

# fixtures
from kep.csv2df.util.row_splitter import split_row_by_year_and_qtr
from kep.csv2df.specification import ParsingCommand, Definition
from kep.parsing_definition.units import UNITS

gdp_def = dict(var="GDP",
               header='Объем ВВП',
               unit=['bln_rub', 'rog'])

indpro_def = dict(var="INDPRO",
                  header='Индекс промышленного производства',
                  unit='yoy')

pc1 = ParsingCommand(**gdp_def)
pc2 = ParsingCommand(**indpro_def)

d1 = Definition(commands=[gdp_def, indpro_def], units=UNITS)

labels = {0: 'GDP_bln_rub',
          1: 'GDP_rog',
          2: 'INDPRO_yoy'}

parsed_varnames = {0: 'GDP',
                   1: 'GDP',
                   2: 'INDPRO'}

parsed_units = {0: 'bln_rub',
                1: 'rog',
                2: 'yoy'}

headers = {0: [['Объем ВВП', '', '', '', ''],
               ['млрд.рублей', '', '', '', '']],
           1: [['Индекс ВВП, в % к прошлому периоду/ GDP index, percent']],
           2: [['Индекс промышленного производства'],
               ['в % к соответствующему периоду предыдущего года']]
           }

data_items = {0: [["1991", "4823", "901", "1102", "1373", "1447"]],
              1: [['1999', '106,4', '98,1', '103,1', '111,4', '112,0']],
              2: [['1991', '102,7', '101,1', '102,2', '103,3', '104,4']]
              }


class Sample():

    def units():
        return {'млрд.рублей': 'bln_rub',
                'в % к прошлому периоду': 'rog',
                'в % к соответствующему периоду предыдущего года': 'yoy'}

    def indicator(name):
        return dict(GDP=pc1, INDPRO=pc2)[name]

    def pdef():
        return d1

    """Fixtures for testing"""

    def rows(i):
        return headers[i] + data_items[i]

    def headers(i):
        return headers[i]

    def data_items(i):
        return data_items[i]

    def table(i):
        return Table(headers[i], data_items[i])

    def table_parsed(i):
        t = Table(headers[i], data_items[i])
        t.varname = parsed_varnames[i]
        t.unit = parsed_units[i]
        t.set_splitter(funcname=None)
        return t

    def label(i):
        return labels[i]


@pytest.fixture
def mock_rows():
    gen = iter(Sample.rows(i) for i in [0, 1, 2])
    return itertools.chain.from_iterable(gen)


def test_mock_rows(mock_rows):
    assert list(mock_rows) == [['Объем ВВП', '', '', '', ''],
                               ['млрд.рублей', '', '', '', ''],
                               ['1991', '4823', '901', '1102', '1373', '1447'],
                               ['Индекс ВВП, в % к прошлому периоду/ GDP index, percent'],
                               ['1999', '106,4', '98,1', '103,1', '111,4', '112,0'],
                               ['Индекс промышленного производства'],
                               ['в % к соответствующему периоду предыдущего года'],
                               ['1991', '102,7', '101,1', '102,2', '103,3', '104,4']]


class Test_split_to_tables():

    def test_split_to_tables(self, mock_rows):
        tables = list(split_to_tables(mock_rows))
        assert len(tables) == 3
        assert tables[0] == Sample.table(0)
        assert tables[1] == Sample.table(1)
        assert tables[2] == Sample.table(2)


class Test_Table_on_creation:

    def setup_method(self):
        self.table = Sample.table(0)

    def test_on_creation_varname_and_unit_and_splitter_are_none(self):
        assert self.table.varname is None
        assert self.table.unit is None
        assert self.table.splitter_func is None

    def test_on_creation_coln(self):
        assert self.table.coln == 5

    def test_on_creation_header_and_datarows(self):
        self.table.headers = Sample.headers(0)
        self.table.datarows = Sample.data_items(0)

    def test_on_creation_lines_is_unknown(self):
        assert self.table.progress.is_line_parsed('Объем ВВП') is False
        assert self.table.progress.is_line_parsed('млрд.рублей') is False

    def test_on_creation_has_unknown_lines(self):
        assert self.table.has_unknown_lines() is True

    def test_str_repr(self):
        assert str(self.table)
        assert repr(self.table)


class Test_Table_after_parsing:

    def setup_method(self):
        t = Sample.table(0)
        t.set_label(varnames_dict={'Объем ВВП': 'GDP'},
                    units_dict={'млрд.рублей': 'bln_rub'})
        t.set_splitter(reader=None)
        self.table_after_parsing = t

    def test_set_label(self):
        table = Sample.table(0)
        table.set_label({'Объем ВВП': 'GDP'}, {'млрд.рублей': 'bln_rub'})
        assert table.varname == 'GDP'
        assert table.progress.is_line_parsed('Объем ВВП') is True
        assert table.unit == 'bln_rub'
        assert table.progress.is_line_parsed('млрд.рублей') is True

    def test_set_splitter(self):
        table = Sample.table(0)
        table.set_splitter(None)
        assert table.splitter_func == split_row_by_year_and_qtr

    def test_has_unknown_lines(self):
        assert self.table_after_parsing.has_unknown_lines() is False

    def test_str_and_repr(self):
        assert str(self.table_after_parsing)
        assert repr(self.table_after_parsing)


class Test_Table_extract_values_wrapper:
    def setup(self):
        test_headers = [['Объем ВВП', '', '', '', ''],
                        ['млрд.рублей', '', '', '', '']]
        self.t = Table(test_headers, [["" for _ in range(6)]])
        self.t.set_label(varnames_dict={'Объем ВВП': 'GDP'},
                         units_dict={'млрд.рублей': 'bln_rub'})
        self.t.set_splitter(reader=None)

    def test_datarow_is_correct(self):
        self.t.datarows = [["1991", "125", "901", "1102", "1373", "1447"]]
        assert len(list(self.t.extract_values())) == 5

    def test_datarow_with_missing_last_value(self):
        self.t.datarows = [["1991", "125", "901", "1102", "1373", ""]]
        assert len(list(self.t.extract_values())) == 4


class Test_extract_tables_function:
    tables = extract_tables(csv_segment=mock_rows(), pdef=Sample.pdef())

    def test_returns_list(self):
        assert isinstance(self.tables, list)

    def test_table0_is_table_instance(self):
        t0 = self.tables[0]
        assert isinstance(t0, Table)
        assert t0 == Sample.table(0)

    def test_table0_can_be_parsed_with_label_GDP_bln_rub(self):
        t0 = self.tables[0]
        t0.set_label(varnames_dict={'Объем ВВП': 'GDP'},
                     units_dict={'млрд.рублей': 'bln_rub'})
        assert t0.label == 'GDP_bln_rub'


def test_timestamp_quarter():
    assert timestamp_quarter(1999, 1) == pd.Timestamp('1999-03-31')


def test_timestamp_month():
    assert timestamp_month(1999, 1) == pd.Timestamp('1999-01-31')


def test_timestamp_annual():
    assert timestamp_annual(1999) == pd.Timestamp('1999-12-31')


class Test_HeaderParsingProgress:
    def setup(self):
        self.progress = HeaderParsingProgress([['abc', 'zzz'], ['def', '...']])

    def test_is_parsed_return_false(self):
        assert self.progress.is_parsed() is False

    def test_str_abc_not_in_return(self):
        assert "- <abc>" in str(self.progress)

    def test_str_abc_in_return(self):
        self.progress.set_as_known('abc')
        assert "+ <abc>" in str(self.progress)

    def test_is_parsed_return_true(self):
        self.progress.set_as_known('abc')
        self.progress.set_as_known('def')
        assert self.progress.is_parsed() is True

    def test_str(self):
        assert '<abc>' in str(self.progress) and '<def>' in str(self.progress)


if __name__ == "__main__":
    pytest.main([__file__])
