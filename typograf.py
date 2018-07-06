import re


substitute_rules = [
    # replace quotes
    (r'([\'\"])(.*?)(\1)(?![^<]*>)', r'&laquo;\2&raquo;'),
    # del_extra_symbols
    (r'(\s+)', r' '),
    # replace_dash_in_phone_num
    (r'(\d+\b)(\-)', r'\1&ndash;'),
    # bind_number_and_word_by_space
    (r'(\b[\d]+\b)(\s+)(\b[А-Яа-яa-zA-Z]+\b)', r'\1&nbsp;\3'),
    # bind_short_word_and_words_by_space
    (r'(\b[А-Яа-яa-zA-Z]{1,2}\b)(\s+)(\b[А-Яа-яa-zA-Z]+\b)', r'\1&nbsp;\3'),
    # replace_dash_to_hyphen
    (r'(\s+-\s+)', r'&mdash;')
    ]


def apply_rule_to_test(pattern):
    for rule, subst in substitute_rules:
        pattern = re.sub(rule, subst, pattern)
    return pattern
