from testings.blog.post import Post


class Blog:
    def __init__(self,title,author) -> None:
        self.title= title
        self.author= author
        self.post =[]


    def __repr__(self) -> str:
        return "{} by {} ({} post{})".format(self.title,self.author,len(self.post),"s" if len(self.post) !=1 else "")


    def create_post(self,title,content):
        self.post.append(Post(title,content))

    def json(self):
        return {
            "title":self.title,
            "author":self.author,
            "post":[post.json() for post in self.post],
        }