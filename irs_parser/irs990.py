import os

import pandas as pd
import requests
import wget

from .utils import get_logger

LOGGER = get_logger(__name__)


class IRS990:
    """Fetches IRS Form 990s and associated metadata from the IRS
    website and AWS account."""
    def __init__(self):
        self.path = os.path.dirname(os.path.realpath(__file__))

    def download_master_file(self, state):
        """Downloads the master file for the specified state to the master_file/
        folder

        Parameters
        ----------
        state : str
            the two letter state code for the BMF file you want to extract

        Returns
        -------
        None, saves the file to the data folder (and creates the master_file folder
            if it does not already exist.
        """
        master_file_directory = os.path.join(self.path, 'master_file')
        directories = os.listdir(self.path)
        if 'master_file' not in directories:
            os.mkdir(master_file_directory)
        download_master_file(state, master_file_directory)

    def download_index(self, year):
        """Downloads the index file for the specified year to the index_file/
        folder

        Parameters
        ----------
        year : int
            the year of the index to download

        Returns
        -------
        None, saves the file to the data folder (and creates the master_file folder
            if it does not already exist.
        """
        index_file_directory = os.path.join(self.path, 'index_file')
        directories = os.listdir(self.path)
        if 'index_file' not in directories:
            os.mkdir(index_file_directory)
        download_index(year, index_file_directory)


def download_master_file(state, directory):
    """Downloads the Exempt Organizations Business Master File (EO BMF) Extract
    for the specified state.

    Parameters
    ----------
    state : str
        the two letter state code for the BMF file you want to extract
    directory : str
        the directory where you would like to save the csv file

    Returns
    -------
    None, saves the file for requested state to the specified directory.
    """
    filename = 'eo_{}.csv'.format(state.lower())
    url = 'https://www.irs.gov/pub/irs-soi/{}'.format(filename)
    try:
        LOGGER.info('Downloading {} to {}'.format(filename, directory))
        df = pd.read_csv(url)
        df.to_csv(os.path.join(directory, filename), index=False)
    except requests.exceptions.HTTPError:
        raise ValueError('Could not file a file for the specified state.')


def download_index(year, directory):
    """Downloads the index of all IRS 990 files for a given year to
    the specified directory.

    Parameters
    ----------
    year : int
        the year of the index to download
    directory : str
        the directory where you would like to save the csv file

    Returns
    -------
    None, saves the file for requested state to the specified directory.
    """
    filename = 'index_{}.csv'.format(year)
    url = 'https://s3.amazonaws.com/irs-form-990/{}'.format(filename)
    LOGGER.info('Downloading {} to {}'.format(filename, directory))
    try:
        wget.download(url, directory)
    except requests.exceptions.HTTPError:
        raise ValueError('Could not file a file for the specified year.')
