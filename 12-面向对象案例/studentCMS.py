"""
用于完成学生管理系统的具体业务操作
"""
from student import Student

# 1. 创建学生管理系统类


class StudentManager(object):
    """学生管理系统类"""

    def __init__(self):
        """用于初始化学生管理系统"""
        self.students = []

    # 添加学生信息
    def add_student(self):
        """添加学生"""
        student_name = input('请输入学生姓名：')
        student_gender = input('请输入学生性别：')
        student_age = input('请输入学生年龄：')
        student_phone = input('请输入学生手机号：')
        student_desc = input('请输入学生描述信息：')
        student = Student(student_name, student_gender,
                          student_age, student_phone, student_desc)
        self.students.append(student)
        print(f'学生{student_name}添加成功\n')

    # 删除学生信息
    def delete_student(self):
        """删除学生"""
        student_name = input('请输入要删除的学生姓名：')
        for student in self.students:
            if student.name == student_name:
                self.students.remove(student)
                print(f'学生{student_name}删除成功\n')
                break
        print(f'学生{student_name}不存在\n')

    def update_student(self):
        """修改学生"""
        student_name = input('请输入要修改的学生姓名：')
        for student in self.students:
            if student.name == student_name:
                student.gender = input('请输入学生性别：')
                student.age = input('请输入学生年龄：')
                student.phone = input('请输入学生手机号：')
                student.desc = input('请输入学生描述信息：')
                print(f'学生{student_name}修改成功\n')
                break
        print(f'学生{student_name}不存在\n')

    def query_student(self):
        """查询学生"""
        student_name = input('请输入要查询的学生姓名：')
        for student in self.students:
            if student.name == student_name:
                print(student)
                print('\n')
                break
        print(f'学生{student_name}不存在\n')

    def show_all_students(self):
        """显示所有学生信息"""
        # 判断长度是否为0
        if len(self.students) == 0:
            print('暂无学生信息\n')
            return
        for student in self.students:
            print(student)  # 因为Student类中定义了__str__方法，所以可以直接打印学生信息
        print('\n')

    def save_students(self):
        """保存学生信息"""
        with open('./students.txt', 'w', encoding='utf-8') as f:
            stu_dict = [student.__dict__ for student in self.students]
            f.write(str(stu_dict))  # 转成字符串保存

    def load_students(self):
        """加载学生信息"""
        try:
            with open('./students.txt', 'r', encoding='utf-8') as f:
                stu_data = f.read()  # 字符串
                student_dict = eval(stu_data)  # 字符串转为列表
                if len(student_dict) > 0:
                    self.students = [Student(**student)
                                     for student in student_dict]
                else:
                    print('暂无学生信息，请先添加学生信息\n')
        except:
            with open('./students.txt', 'w', encoding='utf-8') as f:
                pass

    def start(self):
        """启动学生管理系统"""
        self.load_students()
        while True:
            self.show_view()
            choice = input('请输入对应的功能编号：')
            if choice == '1':
                self.add_student()
            elif choice == '2':
                self.delete_student()
            elif choice == '3':
                self.update_student()
            elif choice == '4':
                self.query_student()
            elif choice == '5':
                self.show_all_students()
            elif choice == '6':
                self.save_students()
                print('学生信息保存成功\n')
            elif choice == '7':
                num = input('确定要推出么？（y/n）：')
                if num.lower() == 'y':
                    # 推出前自动保存
                    self.save_students()
                    print('学生信息保存成功\n')
                    break
                elif num.lower() == 'n':
                    continue
                else:
                    print('输入的选项不正确，请重新输入')
                    continue
            else:
                print('输入的功能编号不正确，请重新输入')
                continue

    def show_view(self):
        print('*' * 23)
        print('学生管理系统v2.0版')
        print('\t1. 添加学生信息')
        print('\t2. 删除学生信息')
        print('\t3. 修改学生信息')
        print('\t4. 查询学生信息')
        print('\t5. 显示所有学生信息')
        print('\t6. 保存学生信息')
        print('\t7. 退出系统')
        print('*' * 23)
        print()


if __name__ == '__main__':
    cms = StudentManager()
    cms.show_view()
