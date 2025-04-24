

def assert_text_in_list(text, text_list):
    assert text in text_list, f"'{text}' not found in {text_list}"

def assert_list_length(expected, actual):
    assert len(actual) == expected, f"Expected {expected} items, but found {len(actual)}"

