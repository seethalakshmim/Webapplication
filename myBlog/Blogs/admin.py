from django.contrib import admin
from .models import blogPost,comment_post

# To display title and date for admin
class posttAdmin(admin.ModelAdmin):
  list_display = ('title','pub_date')
  search_fields =['title','content']
admin.site.register(blogPost, posttAdmin)

#To approve comments by visitors
class comment_admin(admin.ModelAdmin):
  list_display = ('name','blogpost','comments','posted_on','status')  #Display this fields to admin
  list_filter = ('posted_on','status')
  actions = ['approve']                                               #Admin can approve the comments
#@admin.action('description:Approve comments by visitors')

  def approve(self,request,queryset):
    queryset.update(status=True)                                     #When a new user enters a comment, status=False and then once admin approves, it gets updated

admin.site.register(comment_post,comment_admin)
