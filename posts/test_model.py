from posts.models import Post,Comment

def new():
    post = Post(title="test",content="test",author=1)
    post.save()
    print(post.id)
    
    comment = Comment(post=post,author=1,text='test')
    comment.save()
    print(comment.id)

def show():
    post = Post.objects.get(id=3)
    print(post)
    print(post.author)
    print(post.comments.all())
    print(post.comments.first().author)