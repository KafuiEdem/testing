blogs = dict()

def menu():
    
    
    print_blog()


def print_blog():
    for key,value in blogs.items():
        print("-{}".format(value))