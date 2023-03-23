from posts.models import Post,Comment

post = Post(title="test",content="test",author="test")
post.save()
print(post.id)

comment = Comment(post=post,author="test",text="test")
comment.save()
print(comment.id)