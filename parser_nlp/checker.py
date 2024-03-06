import re

def is_special(string):
	pattern = re.compile(r"^[^\w\s]+$")
	return bool(re.match(pattern, string))

def is_int(param):
    try:
        int(param)
        return True
    except:
        return False


if __name__=="__main__":
    print(is_special("."))
