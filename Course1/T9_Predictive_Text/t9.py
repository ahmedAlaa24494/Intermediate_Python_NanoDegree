import helper
import gold

def parse_content(content):
    data = content.split('\n')
    dataset = {}
    for line in data : 
        word , number = tuple(line.split())
        dataset[word]  =number 
    return dataset


def make_tree(words):
    #In this function we must create tree for each word , 
    return {}

def predict(tree, numbers):
    return {}


if __name__ == '__main__':

    content = helper.read_content(filename='Data/ngrams_10k.txt')

    # When you've finished implementing a part, remove the `gold.` prefix to check your own code.

    # PART 1: Parsing a string into a dictionary.
    words = gold.parse_content(content)

    # PART 2: Building a trie from a collection of words.
    tree = gold.make_tree(words)

    # while True:
    #     # PART 3: Predict words that could follow
    #     numbers = helper.ask_for_numbers()
    #     predictions = gold.predict(tree, numbers)

    #     if not predictions:
    #         print('No words were found that match those numbers. :(')
    #     else:
    #         for prediction, frequency in predictions[:10]:
    #             print(prediction, frequency)

    #     response = input('Want to go again? [y/N] ')
    #     again = response and response[0] in ('y', 'Y')
    #     if not again:
    #         break
    print(words)