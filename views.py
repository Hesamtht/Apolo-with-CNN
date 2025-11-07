from django.shortcuts import render , redirect , get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login , authenticate , logout
from menu.views import food_detail

def register(request):

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password != confirm_password:
            messages.error(request , 'Password and Confirm Password do not match')
            return redirect('profiles')

        # Check if email is already registered
        if User.objects.filter(email = email).exists():
            messages.error(request , 'This email is already registered')
            return redirect('profiles')

        # Create the user
        user = User.objects.create_user(username = email, email = email, password = password)
        user.first_name = name
        user.save()
        messages.success(request , 'Registration successful')
        return redirect('home:home')

        # Optionally, you may want to log in the user automatically after registration
        user = authenticate(request , username = email , password = password)
        if user is not None:
            login(request , user)
            return redirect('home:home')

    return render(request, 'register_form.html')


def comment(request, slug):
    food_detail = get_object_or_404(Food, slug=slug)
    comments = Comment.objects.filter(food=food_detail, active=True)
    new_comment = None

    if request.method == 'POST':
        commenter_name = request.POST.get('commenter_name')
        comment_text = request.POST.get('comment_text')
        if commenter_name and comment_text:  # You can add more validation if needed
            new_comment = Comment.objects.create(food=food_detail, commenter_name=commenter_name, comment_text=comment_text)
            new_comment.save()
    else:
        comment_form = None

    context = {
        'food_detail': food_detail,
        'comments': comments,
        'new_comment': new_comment,
    }

    return render(request, 'menu/templates/detail.html', context)