import re
from config import *


def parse_law_text_list_by_index(law_text_list, index):
    return law_text_list[index]


def parse_by_value(law_text_list, value, index_increment):
    for index, text in enumerate(law_text_list):
        if text == value:
            return law_text_list[index + index_increment]


def parse_author_party_text(author_party_text, get_author=False, get_party=False):
    split = author_party_text.split(' (')
    if get_author:
        return split[0]
    if get_party:
        try:
            return split[1].replace(')', '')
        except IndexError:
            return


def parse_id(law_text_list):
    return parse_law_text_list_by_index(law_text_list, index=0)


def parse_status(law_text_list):
    return parse_by_value(law_text_list, STATUS_ANCHOR, index_increment=1)


def parse_summary(law_text_list):
    return parse_by_value(law_text_list, SUMMARY_ANCHOR, index_increment=1)


def parse_date_list(law_text_list):
    return parse_by_value(law_text_list, DATE_ANCHOR, index_increment=2).split(' - ')


def parse_date(law_text_list):
    return parse_date_list(law_text_list)[0]


def parse_date_status(law_text_list):
    try:
        return parse_date_list(law_text_list)[1]
    except IndexError:
        return


def get_author_party_text(law_text_list):
    return parse_by_value(law_text_list, AUTHOR_ANCHOR, index_increment=1)


def parse_author(law_text_list):
    return parse_author_party_text(get_author_party_text(law_text_list), get_author=True)


def parse_party(law_text_list):
    try:
        return parse_author_party_text(get_author_party_text(law_text_list), get_party=True)
    except IndexError:
        return


def parse_authors_add(law_text_list):
    try:
        authors_list = parse_by_value(law_text_list, AUTHOR_ADD_ANCHOR, index_increment=1).split(';')
        ret = []
        for author_party_text in authors_list:
            author_dict = {
                'name': parse_author_party_text(author_party_text, get_author=True),
                'party': parse_author_party_text(author_party_text, get_party=True),
            }
            ret.append(author_dict)
        return ret
    except AttributeError:
        return


def parse_topics(law_text_list):
    return parse_by_value(law_text_list, TOPICS_ANCHOR, index_increment=1)





