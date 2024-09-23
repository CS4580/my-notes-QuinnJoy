"""Read file from web and do analysis of data
"""
from urllib.request import urlopen

def count_words_from_web_file(url_address):
    """Count the number of words in a file from a web address
    Args:
        url_address (str): URL of the file to read
    Returns:
        int: number of words in the file
    """
    words = 0
    # Read file from web
    with urlopen(url_address) as data:
        for line in data:
            print(line, type(line))
            print(line.decode('utf-8')) #convert bytes to string
            line_words = line.split()# space as separator
            for word in line_words:
                words += 1
    return words
    
def main():
    """Driver Function
    """
    #Read file from web
    file_address = 'http://icarus.cs.weber.edu/~hvalle/sample_data/poem.txt'
    total_words = count_words_from_web_file(file_address)
    print(f'There are a total of {total_words} words in ({file_address})')
    
if __name__ == "__main__":
    main()