from unittest import TestCase
from A1C1 import FirstChar, porcentVocal, nuevo_string, notas_al_pie, codigo, contar_hidrogenos, mediaTempRang


class Test(TestCase):

    def test_first_char(self):
        assert FirstChar('paciente001')
        assert FirstChar('P001')
        assert not FirstChar('1Pac')
        assert FirstChar('_001')
        assert not FirstChar(':p001')

    def test_porcent_vocal(self):
        assert porcentVocal('Hola') == 50.0
        assert porcentVocal('Acacia') == 66.7
        assert porcentVocal('Brrrrrrr') == 0.0
        assert porcentVocal('aAe') == 100.0

    def test_nuevo_string(self):
        assert nuevo_string('Charleston', 2) == 'Chaarleestoon'
        assert nuevo_string('RDT11', 1) == 'RDT11'
        assert nuevo_string('H2O', 3) == 'H2OOO'

    def test_notas_al_pie(self):
        assert notas_al_pie(
            'Esta es la primera nota*; y esta la segunda*.') == 'Esta es la primera nota(1); y esta la segunda(2).'
        assert notas_al_pie(
            'Esta frase no tiene notas. Esta otra tampoco.') == 'Esta frase no tiene notas. Esta otra tampoco.'
        assert notas_al_pie('*,*. *.') == '(1),(2). (3).'
        assert notas_al_pie('*') == '(1)'
        assert notas_al_pie('') == ''

    def test_codigo(self):
        assert codigo('Mireia Belmonte García') == 'MBG20'
        assert codigo('Bruce Frederick Joseph Springsteen') == 'BFJS31'
        assert codigo('') == ''
        assert codigo('Gerard Piqué Bernabéu') == 'GPB19'
        assert codigo('Sergio Ramos García') == 'SRG17'

    def test_contar_hidrogenos(self):
        assert contar_hidrogenos('HIO') == 1
        assert contar_hidrogenos('H2O') == 2
        assert contar_hidrogenos('C2H5O') == 5
        assert contar_hidrogenos('Fe3O4') == 0
        assert contar_hidrogenos('C2OH') == 1

    def test_media_temp_rang(self):
        lst1 = [34.5, 12.9, 15, 43, 51.4, 23.4]
        assert mediaTempRang(lst1) == 28.98
        assert mediaTempRang([45.5, 12.9, 15, 32.5, 51.4, 21.2]) == 22.9
        assert mediaTempRang([14.5, 12.6, 47.8]) == -1
        assert mediaTempRang([15, 16, 14, 50, 17]) == 16.0
