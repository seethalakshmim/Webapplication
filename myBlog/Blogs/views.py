from django.shortcuts import render,get_object_or_404
from .models import blogPost,comment_post
from .forms import commentform


#Global view of blog posts
def postblog(request):
    all_posts = blogPost.objects.all().order_by('-pub_date')
    template_data = {'all_posts': all_posts}
    return render ( request,'index.html', template_data)

#Detailed view of blog post
   #  Detailedview=blogPost.objects.get(pk=id)
   # return render(request,'detail.html',{'Detailedview':Detailedview})
#Displaying comments by visitors
#def comment_post(request,id):

#Function for displaying the detailed post and displaying comments
def detailblog(request, id):
    Detailedview=get_object_or_404(blogPost,pk=id)
    blogpost=get_object_or_404(blogPost,id=id)                  #assigning post object in blogpost variable
    comments=blogpost.comments.filter(status=True)              #We need only approved comments (by Admin)
    new_comm=None
    if request.method =='POST':
        Cform=commentform(data=request.POST)
        if Cform.is_valid():                                   #Checking whether post method and if valid, first saving but not in database i.e, commit=false
           new_comm=Cform.save(commit=False)
           new_comm.blogpost=blogpost                          #Assigning new comment object into the post
           new_comm.save()
    else:
        Cform=commentform()
    return render(request, 'detail.html',
                  {'Detailedview':Detailedview,'blogPost': blogPost, 'comments':comments,'new_comm': new_comm, 'Cform': Cform})
