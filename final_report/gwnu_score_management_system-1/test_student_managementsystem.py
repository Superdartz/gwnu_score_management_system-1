import unittest
from student_management_system import StudentManagementSystem
from unittest.mock import Mock
from unittest.mock import patch
from unittest.mock import mock_open

class Test(unittest.TestCase):

    def setUp(self):
        self.m_open1 = mock_open(read_data="1,강호민,85,90,95\n")
        self.m_open2 = mock_open(read_data="1,강호민,85,90,95\n2,김광호,80,70,60\n")
        self.m_open3 = mock_open(read_data="1,강호민,85,90,95\n2,김광호,80,70,60\n3,김민식,75,85,80\n")

        self.m_write_open_1 = mock_open()
        self.m_w = mock_open().return_value
        self.m_write_open_1.side_effect = [self.m_open3.return_value, self.m_w]

    def test_constructor(self):
        sms = StudentManagementSystem()
        self.assertIsNotNone(sms)

    def test_read(self):
        
        with patch('student_management_system.open', self.m_open1):
            sms = StudentManagementSystem()
            self.assertEqual(1, sms.read('score.csv'))

        self.m_open1.assert_called_with('score.csv', 'rt', encoding="utf-8")

    def test_read_2(self):
        
        with patch('student_management_system.open', self.m_open2):
            sms = StudentManagementSystem()
            self.assertEqual(2, sms.read('score.csv'))

        self.m_open2.assert_called_with('score.csv', 'rt', encoding="utf-8")

    def test_sort_1(self):
        with patch('student_management_system.open', self.m_open1):
            sms = StudentManagementSystem()
            sms.read('score.csv')

            result = sms.sort(order_key="register", order_way="asc")
            self.assertEqual('1,강호민,85,90,95,270,90', result)

    def test_sort_2(self):
        with patch('student_management_system.open', self.m_open2):
            sms = StudentManagementSystem()
            sms.read('score.csv')

            result = sms.sort(order_key="register", order_way="asc")
            self.assertEqual('1,강호민,85,90,95,270,90\n2,김광호,80,70,60,210,70', result)

    def test_sort_3(self):
        with patch('student_management_system.open', self.m_open2):
            sms = StudentManagementSystem()
            sms.read('score.csv')

            result = sms.sort(order_key="register", order_way="des")
            self.assertEqual('2,김광호,80,70,60,210,70\n1,강호민,85,90,95,270,90', result)

    def test_sort_4(self):
        with patch('student_management_system.open', self.m_open2):
            sms = StudentManagementSystem()
            sms.read('score.csv')

            result = sms.sort("stotal","asc")
            self.assertEqual('2,김광호,80,70,60,210,70\n1,강호민,85,90,95,270,90', result)
    
    def test_sort_5(self):
        with patch('student_management_system.open', self.m_open2):
            sms = StudentManagementSystem()
            sms.read('score.csv')

            result = sms.sort("stotal","des")
            self.assertEqual('1,강호민,85,90,95,270,90\n2,김광호,80,70,60,210,70', result)

    def test_write_1(self):
        with patch('student_management_system.open', self.m_write_open_1):
            sms = StudentManagementSystem()
            sms.read('score.csv')
            sms.write('result.csv')
        
        self.m_w.write.assert_called_with('1,강호민,85,90,95,270,90\n2,김광호,80,70,60,210,70\n3,김민식,75,85,80,240,80')

    def test_write_2(self):
        with patch('student_management_system.open', self.m_write_open_1):
            sms = StudentManagementSystem()
            sms.read('score.csv')
            sms.write('result.csv', 'register', 'des')

        self.m_w.write.assert_called_with("3,김민식,75,85,80,240,80\n2,김광호,80,70,60,210,70\n1,강호민,85,90,95,270,90")

    def test_write_3(self):
        with patch('student_management_system.open', self.m_write_open_1):
            sms = StudentManagementSystem()
            sms.read('score.csv')
            sms.write('result.csv', 'stotal', 'asc')

        self.m_w.write.assert_called_with('2,김광호,80,70,60,210,70\n3,김민식,75,85,80,240,80\n1,강호민,85,90,95,270,90')

    def test_write_4(self):
        with patch('student_management_system.open', self.m_write_open_1):
            sms = StudentManagementSystem()
            sms.read('score.csv')
            sms.write('result.csv', 'stotal', 'des')

        self.m_w.write.assert_called_with('1,강호민,85,90,95,270,90\n3,김민식,75,85,80,240,80\n2,김광호,80,70,60,210,70')


if __name__ == "__main__":
    unittest.main()