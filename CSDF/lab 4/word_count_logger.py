import logging

def word_count(myfile):
    logging.basicConfig(
        level=logging.DEBUG, 
        filename='word_count_logger.log',
        format='%(asctime)s %(levelname)s:%(message)s',
        filemode='w'
    )

    try:
        with open(myfile, 'r') as f:
            file_data = f.read()
            words = file_data.split(" ")
            num_words = len(words)
            logging.debug("this file has %d words", num_words)
            return num_words
    except OSError as e:
        logging.error("error reading the file: %s", e)
        raise

if __name__ == "__main__":
    try:
        result = word_count("words.txt")
        print(f"Word count: {result}")
    except OSError as e:
        print(f"Failed to count words: {e}")