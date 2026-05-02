from django.shortcuts import render
from blog.models import Post

def post_list(request):
    post = Post.objects.all()
    context = {
        "post_list": post
    }
    return render(
        request,
        "blog/post_list.html",
        context=context,
    )



# def get_product_by_id(request, post_id):
#     post = Product.objects.get(id=product_id)
#     context = {
#         "product": product,
#     }
#     return render(
#         request,
#         "testapp/product_info.html",
#         context=context
#     )