# How to use package 
# -------------------

# ==============================================================
# -------------------call syntax type 1 start-------------------
# ==============================================================
# import packageName.moduleName
# import packageName.subPackageName.moduleName
# Ex:-
import Admin.service # here Admin is package, service is module
import Admin.Common.header # here Admin is package, Common is subPackage, header is module

# How to access variable, function, class etc 
# ===============================================
# packageName.moduleName.functionName()
# packageName.subPackageName.moduleName.functionName()
# Ex:-
Admin.service.testService()
Admin.Common.header.testHeader()
# ==============================================================
# -------------------call syntax type 1 end-------------------
# ==============================================================














# ==============================================================
# -------------------call syntax type 2 start-------------------
# ==============================================================
# from packageName import moduleName
# from packageName.subPackageName import moduleName
# Ex:-
from Admin import product
from Admin.Common import content

# How to access variable, function, class etc 
# ===============================================
# moduleName.functionName()
# subPackageName.moduleName.functionName()
# Ex:-
product.testProduct()
content.testContent()
# ==============================================================
# -------------------call syntax type 2 end-------------------
# ==============================================================













# ==============================================================
# -------------------call syntax type 3 start-------------------
# ==============================================================
# from packageName.moduleName import function_name()
# from packageName.subPackageName.moduleName import function_name()
# Ex:-
from Admin.dashboard import testDashboard
from Admin.dashboard import testDashboard_second, testDashboard_third # same module multiple function import
from Admin.Common.footer import testFooter

# How to access variable, function, class etc 
# ===============================================
# moduleName.functionName()
# subPackageName.moduleName.functionName()
# Ex:-
testDashboard()
testDashboard_second()
testDashboard_third()
testFooter()
# ==============================================================
# -------------------call syntax type 3 end-------------------
# ==============================================================

















# ==============================================================
# -------------------call syntax type 4 (with *) start----------
# ==============================================================
# from packageName import *
# from packageName.subPackageName import *
# Ex:-
from User import *
from Admin.Common import *
# Note: if in package -> __init__.py defines a list named __all__, it is taken to be the list of module names that should be imported when call "from package import *"
# other wise encountered error

# How to access variable, function, class etc 
# ===============================================
# moduleName.functionName()
# Ex:-
profile.testProfile()
header.testHeader()
footer.testFooter()
# content.testContent() # NameError: name 'content' is not defined  becose in __all__ list not added content module in __init__.py file

# ==============================================================
# -------------------call syntax type 4 (with *) end----------
# ==============================================================

















# ===========================================================================
# -----call syntax type 5 siblings (same level package call) start-----------
# ===========================================================================
# we want to call User package request module into Tech package work module


####### see the code in User/request.py and Tech/work.py files ########
from Tech import work
work.testWork()

# ===========================================================================
# -----call syntax type 5 siblings (same level package call) end-----------
# ===========================================================================