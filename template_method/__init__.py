
from template_method.complex_template_method import GeekTravel
from template_method.template_method import Android_Compiler, IOS_Compiler, Client

def template_method_project_1():
    ios = IOS_Compiler()
    ios.compile_execute()

    android = Android_Compiler()
    android.compile_execute()

def template_method_project_2():
    client = Client()
    client.main()

def template_method_project_3():
    advisor = GeekTravel()
    advisor.prepare_trip()
