import stats
import sys

def get_book_text(filepath: str) -> str:
    with open(filepath) as file:
        return file.read()

if __name__ == '__main__':
    if len(sys.argv) <= 1:
        print('Usage: python3 main.py <path_to_book>')
        sys.exit(1)
    print('''
============ BOOKBOT ============
Analyzing book found at {url}...
----------- Word Count ----------'''.format(url=sys.argv[1]))
    book_text = get_book_text(sys.argv[1])
    print('Found {num_words} total words'.format(
        num_words=stats.get_num_words(book_text)))

    print('--------- Character Count -------')
    char_list = stats.get_list_of_char(book_text)
    for t in list(filter(lambda t: t[0].isalpha(), stats.organize(char_list))):
        print('{char}: {num}'.format(char=t[0], num=t[1]))
    print('============= END ===============')
