from typing import List, Text, Tuple
from copy import copy


def modify_definition(
    words: List[Text],
    definitions: List[Text],
    objective_word: Text,
    new_definition: Text,
) -> List[Text]:
    index = words.index(objective_word)
    # use copy to avoid modify over inputs
    result_definitions = copy(definitions)
    result_definitions[index] = new_definition
    return result_definitions


def find_rhyme(
    words: List[Text],
    definitions: List[Text],
    objective_rhyme: Text,
) -> Tuple[List[Text], List[Text]]:
    result_words = []
    result_definitions = []
    for (word, definition) in zip(words, definitions):
        if word.endswith(objective_rhyme):
            result_words.append(word)
            result_definitions.append(definition)
    return (result_words, result_definitions)


def test_list():
    words = ["barf", "morph", "scarf", "snarf", "sound", "surf"]
    definitions = [
        "(verb) eject the contents of the stomach through the mouth",
        "(verb) change shape as via computer animation",
        (
            "(noun) a garment worn around the head or neck or shoulders for"
            "warmth or decoration"
        ),
        "(verb) make off with belongings of others",
        (
            "(verb) emit or cause to emit sound."
            "(noun) vibrations that travel through the air or another medium"
        ),
        ("(verb) switch channels, on television" "(noun) waves breaking on the shore"),
    ]

    new_definitions = modify_definition(words, definitions, "morph", "aaa")
    assert new_definitions[1] == "aaa"

    rhymers = find_rhyme(words, definitions, "arf")
    assert set(rhymers[0]) == {"barf", "scarf", "snarf"}
    assert rhymers[1][0] == definitions[0]
    assert rhymers[1][1] == definitions[2]
    assert rhymers[1][2] == definitions[3]


if __name__ == "__main__":
    test_list()
