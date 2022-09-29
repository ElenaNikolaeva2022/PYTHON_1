from sort import get_da, sort
from viev import get_data, get_number_operasion
from write_read_file import read_file, write_file
from main import sort_data


def button():
    return sort_data(get_number_operasion, read_file, write_file, sort, get_da, get_data)
