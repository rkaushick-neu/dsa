# Question 1
# A class records the attendance of students (e.g., 8 people).
# Construct an 8 bits array, and map students (ID) to the 8
# positions. If the normal attendance of the day, the
# corresponding position will be set to 1, otherwise set to 0.
# 
# Find the students who have not shown up for the last two days.
class Attendance:

    def __init__(self, attendance_day_1=0b10110101, attendance_day_2=0b10100101) -> None:
        self.attendance_day_1 = attendance_day_1
        self.attendance_day_2 = attendance_day_2

    def finding_absent_students(self) -> list[int]:
        # first taking bitwise OR operation & then taking the ~ operation
        # global attendance_day_1, attendance_day_2
        not_attended_students = ~(self.attendance_day_1 | self.attendance_day_2) & 0b11111111
        not_attended_student_ids = []
        for student_id in range(0, 8):
            if(not_attended_students & (1 << student_id)):
                not_attended_student_ids.append(student_id+1)
        return not_attended_student_ids


# How many unique users use an app per day?
# Generate a Bitmap everyday w.r.t. the user access log. Each
# user corresponds to a location in the Bitmap, and the location
# is set to 1 if it is accessed on that day, otherwise it is 0.
# 
# Find the users who used the app yesterday are also using it
# today?

class AppUsers:
    def __init__(self, users_day_1=0b10101010111, users_day_2=0b11111010111) -> None:
        self.users_day_1 = users_day_1
        self.users_day_2 = users_day_2

    def findActiveUsers(self) -> list[int]:
        active_users_bitmap = self.users_day_1 & self.users_day_2
        # now finding which of those users viewed on both days
        user_id_list = []
        # for user_id in range(0, 11):
        #     if(active_users_bitmap & (1 << user_id)):
        #         user_id_list.append(user_id)
        # writing the same as the above in a more pythonic way
        user_id_list = [(user_id+1) for user_id in range(0, 11) if(active_users_bitmap & (1 << user_id))]
        return user_id_list

# Finding if a number is odd or even using bitmaps
class Odd_Or_Even:
    def isOdd(num) -> bool:
        return bool(num & (1 << 0))

if __name__ == "__main__":
    a = Attendance()
    print(a.finding_absent_students())

    b = AppUsers()
    print(b.findActiveUsers())

    print(Odd_Or_Even.isOdd(11))
    print(Odd_Or_Even.isOdd(10))
    print(Odd_Or_Even.isOdd(2))
    print(Odd_Or_Even.isOdd(0))