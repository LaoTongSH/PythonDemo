#慕课网 廖雪峰教程 B05.2 任務
class Person(object):                   # 定義父類
    def __init__(self, name, gender):   # 調用特殊方法，設定屬性
        self.name = name
        self.gender = gender

class Teacher(Person):                  # 定義一個新的類，繼承 Person 類

    def __init__(self, name, gender, course):       # 在子類中調用特殊方法，添加新的屬性
        super(Teacher, self).__init__(name,gender)  # 調用 super 方法，繼承父類的屬性。
        self.course = course                        # 添加新的屬性。

t = Teacher('Alice', 'Female', 'English')           # 創建子類中的實例；
print(t.name)       # 輸出子類實例中的繼承下來的屬性。
print(t.course)     # 輸出子類實例中新增加的屬性。
