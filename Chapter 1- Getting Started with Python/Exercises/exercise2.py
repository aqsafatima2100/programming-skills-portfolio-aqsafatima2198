import sys
print(sys.version)

def get_python_version():
     return sys.version

def main():
     python_version = get_python_version()
     print("python version:", python_version)

     if __name__ == "___main___" :
      main()