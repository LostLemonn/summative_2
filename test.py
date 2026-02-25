import unittest                         # testing framework, an alternative is also PyTest but we would have to use pip install to get it
from quiz_data import load_questions    # converts questions from CSV into dicts
from quiz_utils import clean_name       # cleans the name
from quiz_utils import presence_check   # checks the name is not empty
from quiz_utils import length_check     # checks the name is within length limits
from quiz_utils import character_check  # checks the name contains only valid characters


class TestSmoke(unittest.TestCase):

    def test_smoke(self):
        self.assertTrue(True)


class TestLoadQuestions(unittest.TestCase):

    def test_load_questions_is_not_empty(self):
        """
        The returned list should contain at least one question.
        """
        questions = load_questions()
        self.assertGreater(len(questions), 0)

    def test_each_question_has_four_options(self):
        """
        Each question should have exactly four answer options.
        """
        questions = load_questions()
        for q in questions:
            self.assertEqual(len(q["options"]), 4)


class TestCleanName(unittest.TestCase):

    def test_whitespace(self):
        """
        Random spaces should be removed
        """
        self.assertEqual(clean_name("  jill doe  "), "Jill Doe")

    def test_lowercase_input(self):
        """
        A fully lowercase name should be conveyed correctly
        """
        self.assertEqual(clean_name("john smith"), "John Smith")

    def test_title_cases_uppercase_input(self):
        """
        A fully uppercase name should be conveyed correctly
        """
        self.assertEqual(clean_name("BOB BOBSON"), "Bob Bobson")


class TestPresenceCheck(unittest.TestCase):

    def test_returns_false_for_empty_string(self):
        """
        Empty string should fail the presence check
        """
        self.assertFalse(presence_check(""))

    def test_returns_true_for_valid_name(self):
        """
        A non-empty string should pass the presence check
        """
        self.assertTrue(presence_check("Lucy"))


class TestLengthCheck(unittest.TestCase):

    def test_returns_false_for_single_character(self):
        """
        A single character is too short and should fail
        """
        self.assertFalse(length_check("A"))

    def test_returns_true_for_minimum_length(self):
        """
        Two characters is the minimum valid length hence should pass
        """
        self.assertTrue(length_check("Ed"))

    def test_returns_false_for_name_over_50_characters(self):
        """
        A name longer than 50 characters should fail
        """
        self.assertFalse(length_check("A" * 51))



class TestCharacterCheck(unittest.TestCase):

    def test_returns_false_for_numbered_name(self):
        """
        A name containing digits should fail
        """
        self.assertFalse(character_check("Billy1"))

    def test_returns_false_for_digits(self):
        """
        A string of only digits should fail
        """
        self.assertFalse(character_check("123"))


if __name__ == "__main__":
    unittest.main()
