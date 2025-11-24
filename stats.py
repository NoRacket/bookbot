def get_num_words(text: str) -> int:
    return len(text.split())

def get_list_of_char(text: str) -> dict[str, int]:
    num_of_char = {}
    text = text.lower()
    for c in text:
        if c in num_of_char:
            num_of_char[c] += 1
        else:
            num_of_char[c] = 1
    return num_of_char

def organize(char_list: dict[str, int]) -> list[tuple[str, int]]:
    tuple_list = []
    for c in char_list:
        tuple_list.append((c, char_list[c]))
    
    tuple_list.sort(key=lambda t: t[1], reverse=True) # access the num value of the char for sorting
    return tuple_list
