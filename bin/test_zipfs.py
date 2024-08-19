from collections import Counter

import numpy as np
import pytest

import countwords
import plotcounts

import utilities as util


def test_word_count():
    """Test the counting of words.

    The example poem is Risk, by Anaïs Nin.
    """
    risk_poem_counts = {'the': 3, 'risk': 2, 'to': 2, 'and': 1,
      'then': 1, 'day': 1, 'came': 1, 'when': 1, 'remain': 1,
      'tight': 1, 'in': 1, 'a': 1, 'bud': 1, 'was': 1,
      'more': 1, 'painful': 1, 'than': 1, 'it': 1, 'took': 1,
      'blossom': 1}
    expected_result = Counter(risk_poem_counts)
    with open('test_data/risk.txt', 'r') as reader:
        actual_result = countwords.count_words(reader)
    assert actual_result == expected_result
    
def test_alpha():
    """Test the calculation of the alpha parameter.

    The test word counts satisfy the relationship,
      r = cf**(-1/alpha), where
      r is the rank,
      f the word count, and
      c is a constant of proportionality.

    To generate test word counts for an expected alpha of
      1.0, a maximum word frequency of 600 is used
      (i.e. c = 600 and r ranges from 1 to 600)
    """
    max_freq = 600
    counts = np.floor(max_freq / np.arange(1, max_freq + 1))
    actual_alpha = plotcounts.get_power_law_params(counts)
    assert actual_alpha == pytest.approx(1.0, abs=0.1)
    
def test_integration():
    """
    Generate 1000 files of random words with different known alpha values and compare against computed alpha value.
    
    uhhh this doesn't work. lol.
    """
    
    test_filename = "test_data/test_integration.txt"
    
    for _ in range(10):
        expected_alpha = 2 * np.random.random() + 1.0
        
        max_freq = np.random.randint(100, 300)
        word_counts = np.floor(max_freq / np.power(np.arange(1, max_freq + 1), expected_alpha))
        
        with open(test_filename, "w") as writer:
            for index in range(max_freq):
                writer.write("{} ".format(index) * int(word_counts[index]) + "\n")
        
        with open(test_filename, "r") as reader:
            word_counts = []
            for word, count in countwords.count_words(reader).items():
                word_counts.append(count)
            actual_alpha = plotcounts.get_power_law_params(np.array(word_counts))
            assert actual_alpha == pytest.approx(expected_alpha, abs=0.75)
