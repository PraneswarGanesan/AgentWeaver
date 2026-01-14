from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.write_file import write_file
from functions.run_da import run_python_file


def tests():
    working_directory = "calculator"
    # print("---- main.py (usage) ----")
    # print(run_python_file("calculator", "main.py"))

    # print("---- main.py (expression) ----")
    # print(run_python_file("calculator", "main.py", ["3 + 5"]))

    # print("---- tests.py ----")
    # print(run_python_file("calculator", "tests.py"))

    # print("---- outside working dir ----")
    # print(run_python_file("calculator", "../main.py"))

    # print("---- nonexistent file ----")
    # print(run_python_file("calculator", "nonexistent.py"))

    # print("---- not a python file ----")
    # print(run_python_file("calculator", "lorem.txt"))



    # print(write_file (working_directory,"lorem.txt", "Mother fucker this is not the lorem.txt"))
    # print(write_file (working_directory,"pkg/morelorem.txt", "Mother fucker this is not the lorem.txt"))
    # print(write_file (working_directory,"/tmp/temp.txt", "Mother fucker this is not the lorem.txt"))

    # print("============lorem text==================")
    # print(get_file_content(working_directory, "lorem.txt"))
    # print("===============main=====================")
    # print(get_file_content(working_directory, "main.py"))
    # print("==================pkg==========================")
    # print(get_file_content(working_directory, "pkg/calculator.py"))
    # print("===================bin/cat/============================")
    # print(get_file_content(working_directory, "/bin/cat"))

    # print("---- Root directory ----")
    # root_contents = get_files_info(working_directory)
    # print(root_contents)

    # print("---- pkg directory ----")
    # pkg_contents = get_files_info(working_directory, "pkg")
    # print(pkg_contents)

    # print("---- /bin (should fail) ----")
    # no_contents = get_files_info(working_directory, "/bin")
    # print(no_contents)

    # print("---- ../ (should fail) ----")
    # random_contents = get_files_info(working_directory, "../")
    # print(random_contents)


if __name__ == "__main__":
    tests()
