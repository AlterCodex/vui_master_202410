from unittest import TestCase
from A1C1 import FirstChar, porcentVocal, nuevo_string, notas_al_pie, codigo, contar_hidrogenos, mediaTempRang, \
    detect2ndNdB, primoPitagoric2, contar_pos, mas_denso, jugComKm


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

    def test_detect2nd_nd_b(self):
        assert detect2ndNdB([90, 590, 750, 632, 650, 900, 2000, 789, 545], 30) == 650
        assert detect2ndNdB([90, 590, 750, 632, 650, 900, 2000, 789, 545], 33) == 2000
        assert detect2ndNdB([90, 590, 750, 632, 630, 600, 200, 589, 545], 30) == -1
        assert detect2ndNdB([9e3, 1e4, 1.1e5, 2.2e5, 1.3e6, 2.5e6, 3.2e6], 83) == 2500000.0
        assert detect2ndNdB([2000, 2450.5, 2500, 456.7, 1567.8], 42) == -1

    def test_primo_pitagoric2(self):
        assert primoPitagoric2([3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]) == [5, 13]
        assert primoPitagoric2([5, 9, 13, 17, 21, 25, 29, 33, 37, 41]) == [5, 13]
        assert primoPitagoric2([41, 45, 49, 53, 57, 61, 65, 69, 73, 77, 81]) == [41, 53]
        assert primoPitagoric2([3, 4, 5, 6, 7, 8, 9, 10]) == -1
        lista = [81, 85, 89, 93, 97, 101, 105, 109, 113, 117, 121]
        assert primoPitagoric2(lista) == [89, 97]

    def test_contar_pos(self):
        assert contar_pos([[1, -2, 3], [-4, 5, 6], [7, 8, -9]]) == 6

    def test_mas_denso(self):
        assert mas_denso([['Marte', 1, 2], ['Tierra', 2, 3], ['Venus', 1, 3]]) == 'Tierra'

    def test_jug_com_km(self):
        lst_equipo = [[3, 'Pique', True, 33, 10.2, 9.0],
                      [4, 'Ramos', True, 34, 11.0, 11.1, 9.8, 8.5],
                      [6, 'Koke', True, 27, 7.5, 9.6, 10.3, 6.5, 5.6],
                      [7, 'Joao', True, 25, 10.5, 8.4, 9.0, 8.6],
                      [8, 'Saul', True, 24, 9.5, 8.9, 10.0, 9.6],
                      [9, 'Suarez', False, 33, 8.6, 7.5],
                      [10, 'Lionel', False, 33, 10.0, 11.1, 9.8, 8.5,10.1],
                      [19, 'Odriozola', True, 25, 9.5],
                      [14, 'Araujo', False, 21, 8.9, 9.5],
                      [15, 'Valverde', False, 22, 9.9, 10.2],
                      [16, 'Pedri', True, 18, 10.5, 11, 9.5, 10.6],
                      [22, 'Hermoso', False, 23, 10, 7.5, 6.6],
                      [23, 'Iago', True, 33, 11.1, 9.0, 9.3, 8.8]]
        assert jugComKm(lst_equipo, 10) == ['Pedri', 'Ramos']
        assert jugComKm(lst_equipo, 10.2) == ['Pedri']
        assert jugComKm(lst_equipo, 10.5) == []
        assert jugComKm(lst_equipo, 9.5) == ['Iago', 'Pedri', 'Pique', 'Ramos']
        assert jugComKm(lst_equipo, 9.4) == ['Iago', 'Odriozola', 'Pedri', 'Pique', 'Ramos', 'Saul']
