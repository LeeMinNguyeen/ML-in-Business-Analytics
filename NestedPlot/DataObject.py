import json

class Courses:
    def __init__(self, course_name, course_code, course_category, course_language, course_semester):
        self.course_name = course_name
        self.course_code = course_code
        self.course_category = course_category
        self.course_language = course_language
        self.course_semester = course_semester
        
    def jsonify(self):
        data = json.dumps(self.__dict__)
        return data
        
if __name__ == "__main__":
    course = Courses("Python", "PY101", "Programming", "English", "First")
    course.jsonify()