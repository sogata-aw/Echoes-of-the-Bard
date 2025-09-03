import unittest
import src.model.ennemi as ennemi

class TestEnnemi(unittest.TestCase):
    def test_vie(self):
        ennemi1 = ennemi.Ennemi()
        ennemi1.setPv(100)
        ennemi1.setDifficulte(0)
        self.assertEqual(ennemi1.getPv(), 100)
        self.assertEqual(ennemi1.getDifficulte(), 0)
        ennemi1.setDifficulte(3)
        self.assertEqual(ennemi1.getDifficulte(), 3)


if __name__ == '__main__':
    unittest.main()
