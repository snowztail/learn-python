from typing import List, Text, Tuple, Mapping
from copy import copy


def modify_definition(
    dictionary: Mapping[Text, Text],
    objective_word: Text,
    new_definition: Text,
) -> Mapping[Text, Text]:
    # no need to retrieve index
    result_dictionary = copy(dictionary)
    result_dictionary[objective_word] = new_definition
    return result_dictionary


def find_rhyme(
    dictionary: Mapping[Text, Text],
    objective_rhyme: Text,
) -> Tuple[List[Text], List[Text]]:
    return {
        word: definition
        for (word, definition) in dictionary.items()
        if word.endswith(objective_rhyme)
    }


def test_dictionary():
    dictionary = {
        "barf": "(verb) eject the contents of the stomach through the mouth",
        "morph": "(verb) change shape as via computer animation",
        "scarf": (
            "(noun) a garment worn around the head or neck or shoulders for"
            "warmth or decoration"
        ),
        "snarf": "(verb) make off with belongings of others",
        "sound": (
            "(verb) emit or cause to emit sound."
            "(noun) vibrations that travel through the air or another medium"
        ),
        "surf": (
            "(verb) switch channels, on television" "(noun) waves breaking on the shore"
        ),
    }

    new_dictionary = modify_definition(dictionary, "morph", "aaa")
    assert new_dictionary["morph"] == "aaa"

    rhymers = find_rhyme(dictionary, "arf")
    assert set(rhymers) == {"barf", "scarf", "snarf"}
    for word in {"barf", "scarf", "snarf"}:
        assert rhymers[word] == dictionary[word]


if __name__ == "__main__":
    test_dictionary()
