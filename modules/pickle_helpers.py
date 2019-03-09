import os
import re
import pickle
from bs4 import BeautifulSoup


def save_text_from_html_div(directory, html_filename, text_filename, div_id=None, force_update=False):
    # let's see if we already saved the file
    check = os.path.isfile(os.path.join(directory, text_filename))
    # if we already have the file and don't want to force the update, there's nothing for us to do
    if check and not force_update:
        return

    # make a soup out of the html file
    soup = BeautifulSoup(open(os.path.join(directory, html_filename)), 'html.parser')

    # if we want a specific div, use it
    if div_id:
        results_div = soup.find_all('div', {'id': div_id})[0]  # grab the specific div by the id
    else:
        results_div = soup  # otherwise, just use the soup

    # get a list of all the text within the div
    all_unwrapped_strings_list = [re.sub('\s+', ' ', text).strip() for text in results_div.stripped_strings]

    # save the list to pickle
    with open(os.path.join(directory, text_filename), 'wb') as fp:
        pickle.dump(all_unwrapped_strings_list, fp)
        fp.close()

    return


def read_pickle(file_path):
    with open(file_path, 'rb') as fp:
        ret = pickle.load(fp)
        fp.close()

    return ret
