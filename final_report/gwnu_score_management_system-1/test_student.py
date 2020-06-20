import unittest
from student import Student

class TestStudent(unittest.TestCase):

    def setUp(self):
        self.my_student1 = Student("1,강호민,85,90,95")
        self.my_student2 = Student("2,김광호,80,70,60")

    def tearDown(self):
        del self.my_student1
        del self.my_student2

    def test_constructor(self):
        self.assertIsNotNone(self.my_student1)
        self.assertIsNotNone(self.my_student2)

    def test_sid(self):
        self.assertEqual("1", self.my_student1.sid)
        self.assertEqual("2", self.my_student2.sid)

    def test_sname(self):
        self.assertEqual("강호민", self.my_student1.sname)
        self.assertEqual("김광호", self.my_student2.sname)

    def test_skor(self):
        self.assertEqual(85, self.my_student1.skor)
        self.assertEqual(80, self.my_student2.skor)

    def test_seng(self):
        self.assertEqual(90, self.my_student1.seng)
        self.assertEqual(70, self.my_student2.seng)

    def test_smat(self):
        self.assertEqual(95, self.my_student1.smat)
        self.assertEqual(60, self.my_student2.smat)

    def test_stotal(self):
        self.assertEqual(270, self.my_student1.stotal)
        self.assertEqual(210, self.my_student2.stotal)

    def test_savg(self):
        self.assertEqual(90, self.my_student1.savg)
        self.assertEqual(70, self.my_student2.savg)


if __name__ == "__main__":
    unittest.main()