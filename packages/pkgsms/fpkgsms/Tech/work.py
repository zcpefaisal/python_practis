#=====================
# import type 1
#=====================
# from User import request  # module import
# request.testRequest() 
from User.request import testRequest  # function import
testRequest()

# ModuleNotFoundError: No module named 'User' when run as python3 work.py
# Note: running then module python3 work.py not working here
# for running then need to back in upper level in terminal where booth package are as a sibling
# then use a flag -m for run library module as a script
# correct command is  "python -m Tech.work"  here .py not working

#================================
# import type 2 with hack style 
#================================
# import sys
# sys.path.append('/home/zcpe/python/jupyter_code/python_practis/packages/pkgsms/fpkgsms/User') 
# import request
# Note:  this calling type is not recommanded
# call as usual "python3 work.py" form then Tech folder


def testWork():
    print('Tech package -> work module')
    print('this is testWork function')
    print()
    testRequest()




