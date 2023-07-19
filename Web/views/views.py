from django.shortcuts import render, redirect, HttpResponse
from django import forms
from Web import models
from utils.encrypt import md5


class LoginForm(forms.Form):
    """
    表单数据验证
    """
    # 身份验证, 可选字段使用
    role = forms.ChoiceField(
        required=True,
        choices=(("1", "管理员"), ("2", "用户")),
        # 下拉框使用select
        widget=forms.Select(attrs={"class": "form-control"})
    )
    # 用户名验证
    username = forms.CharField(
        # 提交数据时，必须提交非空值
        required=True,
        # 普通文本数据，使用TextInput即可， attrs添加属性
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "用户名"})
    )
    password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "密码"},
                                   render_value=True)  # 密码输错时，也将密码返回给html页面
    )


class SmsLoginForm(forms.Form):
    role = forms.ChoiceField(
        required=True,
        choices=(("1", "管理员"), ("2", "用户")),
        # 下拉框使用select
        widget=forms.Select(attrs={"class": "form-control"})
    )
    mobile = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "手机号"})
    )
    code = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "验证码"})
    )


# 1 管理员 2客户
mapping = {"1": "ADMIN", "2": "CUSTOMER"}


def login(request):
    # 如果请求方法是POST，则返回渲染的HTML模板，即LoginForm表单会生成html代码，供用户输入数据并提交
    if request.method == "GET":
        form = LoginForm()  # 创建一个空的LoginForm表单对象，此时用户还未输入任何数据，所以它的字段当前都为空
        return render(request, "login.html", {"form": form})

    # data=request.POST将从请求中获取POST数据，并将其用于填充表单对象
    form = LoginForm(data=request.POST)

    # LoginForm校验用户输入的数据是否有效
    if not form.is_valid():
        return render(request, "login.html", {"form": form, "error": "请输入账号与密码！"})

    # 校验通过后获取数据
    role = form.cleaned_data.get("role")
    username = form.cleaned_data.get("username")
    password = form.cleaned_data.get("password")
    md5_password = md5(password)  # 密码加密

    # 去数据库校验数据
    if role not in mapping:
        return render(request, "login.html", {"form": form, "error": "角色不存在"})

    if role == "1":
        user_object = models.Administrator.objects.filter(active=1, username=username, password=md5_password).first()
    else:
        user_object = models.Customer.objects.filter(active=1, username=username, password=md5_password).first()

    if not user_object:
        return render(request, "login.html", {"form": form, "error": "用户名或密码错误"})

    # request.session["user_info"] = {"role": mapping[role], "name": user_object.username, "id": user_object.id}

    return HttpResponse(request, "登录成功")


def sms_login(request):
    if request.method == "GET":
        form = SmsLoginForm()
        return render(request, "sms_login.html", {"form1": form})

    form = SmsLoginForm(data=request.POST)

    if not form.is_valid():
        return render(request, "sms_login.html", {"form1": form, "error": "请输入手机号或验证码！"})

    role = form.cleaned_data.get("role")
    mobile = form.cleaned_data.get("mobile")
    code = form.cleaned_data.get("code")

    if role not in mapping:
        return render(request, "sms_login.html", {"form1": form, "error": "角色不存在"})

        # 去数据库校验数据
    if role not in mapping:
        return render(request, "sms_login.html", {"form1": form, "error": "角色不存在"})

    if role == "1":
        user_object = models.Administrator.objects.filter(active=1, mobile=mobile).first()
    else:
        user_object = models.Customer.objects.filter(active=1, mobile=mobile).first()

    if not user_object:
        return render(request, "sms_login.html", {"form1": form, "error": "当前号码未注册！"})

    if code == "1111":
        # request.session["user_info"] = {"role": mapping[role], "name": user_object.mobile}
        return HttpResponse(request, "登录成功")
        # return redirect("/首页/")
