from student_management_system import StudentManagementSystem

if __name__ == "__main__":
    sms = StudentManagementSystem()
    sms.read('score.csv')
    sms.write('pre_result.csv',"stotal","des")
    sms2 = StudentManagementSystem()
    sms2.read_2('pre_result.csv')
    print(sms2.sort_2("stotal","des"))
    sms2.write_2('result.csv',"stotal","des")