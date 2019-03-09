import os
import re

# files and directories
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(ROOT_DIR, 'data')
LAWS_HTML_FILENAME = 'laws.html'
LAWS_HTML_PATH = os.path.join(DATA_DIR, LAWS_HTML_FILENAME)
LAWS_TEXT_FILENAME = 'text.pickle'
LAWS_TEXT_PATH = os.path.join(DATA_DIR, LAWS_TEXT_FILENAME)

# vars
RESULTS_DIV_ID = 'dnn_ctr71247_StateNetDB_linkList'
STATE_HEADER_CLASS_NAME = ['h2Headers1']
SPACER_DIV_STYLE = 'clear:  both'
STATUS_ANCHOR = 'Status:'
SUMMARY_ANCHOR = 'Summary:'
DATE_ANCHOR = 'Date of Last Action:'
AUTHOR_ANCHOR = 'Author:'
AUTHOR_ADD_ANCHOR = 'Additional Authors:'
TOPICS_ANCHOR = 'Topics:'

# regex matching
INDEX_1_PATTERN = re.compile('[A-Z]+')  # one or more UPPERCASE letters
INDEX_2_PATTERN = re.compile('[0-9]+')  # one or more numbers
STATES = {
    'AL': 'Alabama',
    'AK': 'Alaska',
    'AZ': 'Arizona',
    'AR': 'Arkansas',
    'CA': 'California',
    'CO': 'Colorado',
    'CT': 'Connecticut',
    'DE': 'Delaware',
    'FL': 'Florida',
    'GA': 'Georgia',
    'HI': 'Hawaii',
    'ID': 'Idaho',
    'IL': 'Illinois',
    'IN': 'Indiana',
    'IA': 'Iowa',
    'KS': 'Kansas',
    'KY': 'Kentucky',
    'LA': 'Louisiana',
    'ME': 'Maine',
    'MD': 'Maryland',
    'MA': 'Massachusetts',
    'MI': 'Michigan',
    'MN': 'Minnesota',
    'MS': 'Mississippi',
    'MO': 'Missouri',
    'MT': 'Montana',
    'NE': 'Nebraska',
    'NV': 'Nevada',
    'NH': 'New Hampshire',
    'NJ': 'New Jersey',
    'NM': 'New Mexico',
    'NY': 'New York',
    'NC': 'North Carolina',
    'ND': 'North Dakota',
    'OH': 'Ohio',
    'OK': 'Oklahoma',
    'OR': 'Oregon',
    'PA': 'Pennsylvania',
    'RI': 'Rhode Island',
    'SC': 'South Carolina',
    'SD': 'South Dakota',
    'TN': 'Tennessee',
    'TX': 'Texas',
    'UT': 'Utah',
    'VT': 'Vermont',
    'VA': 'Virginia',
    'WA': 'Washington',
    'WV': 'West Virginia',
    'WI': 'Wisconsin',
    'WY': 'Wyoming',
    'DC': 'District of Columbia',
    'PR': 'Puerto Rico',
}

