#import the module directy
# import constants

# import variables from constants
from constants import CURRENT_MENTOR_COUNT, CURRENT_STUDENT_COUNT

# printing using module
# print("There are currently " + str(constants.CURRENT_STUDENT_COUNT) + " number of participants.")
# print("There are currently " + str(constants.CURRENT_MENTOR_COUNT) + " number of mentors.")

# printing by directly import variable from module
# print("There are currently " + str(CURRENT_STUDENT_COUNT) + " number of participants.")
# print("There are currently " + str(CURRENT_MENTOR_COUNT) + " number of mentors.")

print("There are currently",CURRENT_STUDENT_COUNT,"number of participants.")
print("There are currently",CURRENT_MENTOR_COUNT,"number of mentors.")