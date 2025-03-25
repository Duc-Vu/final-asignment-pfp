import unittest, json
from unittest.mock import patch
from src.employees_management.employees_management import EmployeeManagement

class TestEmployeeManagement(unittest.TestCase):
    def setUp(self):
        self.file_path = "tests/data.json"

        # Đọc dữ liệu từ file JSON
        try:
            with open(self.file_path, "r") as file:
                data = json.load(file)
        except FileNotFoundError:
            data = {}  # Nếu file không tồn tại, dùng dict rỗng
        
        # Tạo instance EmployeeManagement với data từ JSON
        self.emp_manager = EmployeeManagement(data, self.file_path)

    # TC01: Không nhập tên khi thêm mới
    @patch('builtins.input', side_effect=[""])
    def test_missing_name_add(self, mock_input):
        result = self.emp_manager.update_information_employee("developer", "003", func="Add")
        self.assertIsNone(result)

    # TC02: Không nhập tên khi cập nhật
    @patch('builtins.input', side_effect=[""])
    def test_missing_name_update(self, mock_input):
        result = self.emp_manager.update_information_employee("developer", "001", func="Update")
        self.assertTrue(result)

    # TC03: Nhập lương cơ bản không hợp lệ
    @patch('builtins.input', side_effect=["abc", ""])
    def test_invalid_base_salary(self, mock_input):
        result = self.emp_manager.update_information_employee("developer", "001", func="Update")
        self.assertIsNone(result)

    # TC04: Nhập số năm kinh nghiệm không hợp lệ
    @patch('builtins.input', side_effect=["xyz", ""])
    def test_invalid_exp_year(self, mock_input):
        result = self.emp_manager.update_information_employee("developer", "001", func="Update")
        self.assertIsNone(result)

    # TC05: Không nhập team name cho team leader
    @patch('builtins.input', side_effect=[""])
    def test_teamleader_without_team(self, mock_input):
        result = self.emp_manager.update_information_employee("teamleader", "003", func="Add")
        self.assertIsNone(result)

    # TC06: Thêm team leader khi team đã có leader
    @patch('builtins.input', side_effect=["beta", ""])
    def test_teamleader_duplicate_team(self, mock_input):
        result = self.emp_manager.update_information_employee("teamleader", "003", func="Add")
        self.assertIsNone(result)

    # TC07: Nhập Bonus Rate không hợp lệ
    @patch('builtins.input', side_effect=["xx", ""])
    def test_invalid_bonus_rate(self, mock_input):
        result = self.emp_manager.update_information_employee("tester", "004", func="Add")
        self.assertIsNone(result)

    # TC08: Nhập Type Tester sai
    @patch('builtins.input', side_effect=["automation", ""])
    def test_invalid_tester_type(self, mock_input):
        result = self.emp_manager.update_information_employee("tester", "004", func="Add")
        self.assertIsNone(result)

    # TC09: Nhập team name trống khi cập nhật
    @patch('builtins.input', side_effect=[""])
    def test_empty_team_name_update(self, mock_input):
        result = self.emp_manager.update_information_employee("developer", "001", func="Update")
        self.assertTrue(result)

    # TC10: Nhập programming languages trống khi cập nhật
    @patch('builtins.input', side_effect=[""])
    def test_empty_prog_lang_update(self, mock_input):
        result = self.emp_manager.update_information_employee("developer", "001", func="Update")
        self.assertTrue(result)

    # TC11: Nhập Bonus Rate trống khi cập nhật
    @patch('builtins.input', side_effect=[""])
    def test_empty_bonus_rate_update(self, mock_input):
        result = self.emp_manager.update_information_employee("tester", "002", func="Update")
        self.assertTrue(result)

    # TC12: Cập nhật thành công Developer
    @patch('builtins.input', side_effect=["new name", "5500"])
    def test_successful_update_developer(self, mock_input):
        result = self.emp_manager.update_information_employee("developer", "001", func="Update")
        self.assertTrue(result)

    # TC13: Cập nhật thành công Tester
    @patch('builtins.input', side_effect=["new name", "6000", "1.2", "am"])
    def test_successful_update_tester(self, mock_input):
        result = self.emp_manager.update_information_employee("tester", "002", func="Update")
        self.assertTrue(result)

    # TC14: Cập nhật thành công Team Leader
    @patch('builtins.input', side_effect=["new name", "7000", "beta", "c++, python", "5", "2.0"])
    def test_successful_update_teamleader(self, mock_input):
        result = self.emp_manager.update_information_employee("teamleader", "002", func="Update")
        self.assertTrue(result)

    # TC15: Thêm mới Developer thành công
    @patch('builtins.input', side_effect=["alex", "5000", "alpha", "python, java", "3"])
    def test_add_new_developer(self, mock_input):
        result = self.emp_manager.update_information_employee("developer", "003", func="Add")
        self.assertTrue(result)

    # TC16: Thêm mới Tester thành công
    @patch('builtins.input', side_effect=["mike", "5500", "1.1", "mt"])
    def test_add_new_tester(self, mock_input):
        result = self.emp_manager.update_information_employee("tester", "004", func="Add")
        self.assertTrue(result)

    # TC17: Thêm mới Team Leader thành công
    @patch('builtins.input', side_effect=["lisa", "7000", "gamma", "java, c#", "6", "2.5"])
    def test_add_new_teamleader(self, mock_input):
        result = self.emp_manager.update_information_employee("teamleader", "005", func="Add")
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()
