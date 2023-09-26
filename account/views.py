from django.shortcuts import redirect,render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User



# Login
def login_request(request):
    if request.user.is_authenticated:
        return redirect("index")
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("blog")
        else:
            return render(request, "account/login.html", {
                "error": "Kullanıcı Adı ya da Parola Yanlış"
            })

    return render(request, "account/login.html")

# Register
def register_request(request):
    if request.user.is_authenticated:
        return redirect("index")
     
    if request.method=="POST":
        username = request.POST["username"]
        email = request.POST["email"]
        firstname = request.POST["firstname"]
        lastname = request.POST["lastname"]
        password = request.POST["password"]
        repassword = request.POST["repassword"]

        if password == repassword :
            if User.objects.filter(username=username).exists():
                return render(request,"account/register.html",
                              {
                                "error":"Kullanıcı Adı Başka Biri Tarafından Alındı",
                                "username":username,
                                "email":email,
                                "firstname":firstname,
                                "lastname":lastname
                                })
            else:
                if User.objects.filter(email=email).exists():
                    return render(request,"account/register.html",
                                  {
                                    "error":"Email Kullanılıyor",
                                    "username":username,
                                    "email":email,
                                    "firstname":firstname,
                                    "lastname":lastname
                                  })
                else:
                    user = User.objects.create_user(username=username,email=email,first_name=firstname,last_name=lastname,password=password)
                    user.save()
                    return redirect("login")
        else:
            return render(request,"account/register.html",{"error":"Parola Eşleşmiyor"})

    return render(request,"account/register.html")

#Logout
def logout_request(request):
    logout(request)
    return render(request,"blog.html")


