import util

def generate_testcase(testcase):
    """Create everything needed to run a testcase

    Takes testcase name and creates compiled exe and new bash script
    """
    testcase = testcase.upper()
    src_path = os.path.join(util.get_testcases_path(), testcase)
    


