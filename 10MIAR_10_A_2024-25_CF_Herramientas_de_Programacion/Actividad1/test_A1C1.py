from unittest import TestCase

from A1C1 import FirstChar


class Test(TestCase):

    def test_first_char(self):
        assert FirstChar('paciente001')
        assert FirstChar('P001')
        assert not FirstChar('1Pac')
        assert FirstChar('_001')
        assert not FirstChar(':p001')
