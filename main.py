from config import *
from modules import pickle_helpers, parse_helpers


def main():
    # save the text to a pickle file if we haven't already
    pickle_helpers.save_text_from_html_div(
        DATA_DIR,  # directory that we're operating in
        LAWS_HTML_FILENAME,  # filename for the html file we want to read
        LAWS_TEXT_FILENAME,  # filename for the text list we will save
        div_id=RESULTS_DIV_ID,  # optional, id of the div we want within the HTML
        force_update=False,  # optional, set to True if you want to force a new file to be made
    )

    # read the pickle back in
    text_list = pickle_helpers.read_pickle(LAWS_TEXT_PATH)

    # create a list of law lists, e.g.
    # [
    #     [law1_text1, law1_text2, law1_text3],  # law1
    #     [law2_text1, law2_text2, law2_text3],  # law2
    #     ...
    # ]
    last_law_start_index = 0
    law_list = []
    text_list_length = len(text_list)
    for index, text in enumerate(text_list):
        # the law header will be our anchor (i.e. 'AL HJR 298')
        # so we can use that to parse each law, using STATES and two patterns from the config file
        if index == text_list_length - 1:  # but first, if we're at the end of the list, append the last law
            next_law_start_index = index + 1
            law_list.append(text_list[last_law_start_index:next_law_start_index])

        text_split = text.split()  # split the text by whitespace
        # then see if we meet the conditions for a new law
        if len(text_split) == 3:  # there should be 3 elements to the law
            # the first element should be in our states list
            # the second element should be one or more UPPERCASE letters
            # the third element should be one or more numbers
            # if we meet those conditions, do things
            if text_split[0] in STATES.keys() \
                    and INDEX_1_PATTERN.match(text_split[1]) \
                    and INDEX_2_PATTERN.match(text_split[2]):
                next_law_start_index = index  # the next law will start at this index
                if last_law_start_index != 0:  # if this isn't the start of the list, append the new law
                    # we append a list from the last_law_start_index to the next_law_start_index
                    law_list.append(text_list[last_law_start_index:next_law_start_index])

                # set the next last law start index equal to the current next law start index.
                # and, no, that phrasing doesn't make any sense. Just read it a few times and you'll get it.
                last_law_start_index = next_law_start_index

    # now we have a list of law-text-lists (law_list) and we need to parse them
    parsed_laws = []
    for law_text_list in law_list:
        parsed_law = {
            'id': parse_helpers.parse_id(law_text_list),
            'status': parse_helpers.parse_status(law_text_list),
            'summary': parse_helpers.parse_summary(law_text_list),
            'date_of_last_action': parse_helpers.parse_date(law_text_list),
            'date_status': parse_helpers.parse_date_status(law_text_list),
            'author': parse_helpers.parse_author(law_text_list),
            'party': parse_helpers.parse_party(law_text_list),
            'add_authors': parse_helpers.parse_authors_add(law_text_list),
            'add_author_party_count': parse_helpers.count_add_author_party(law_text_list),
            'topics': parse_helpers.parse_topics(law_text_list),
        }
        parsed_laws.append(parsed_law)

    for law in law_list:
        if law[0] == 'IL H 5006':
            print(law)

    for law in parsed_laws:
        if law['id'] == 'IL H 5006':
            print(law)


if __name__ == '__main__':
    main()
