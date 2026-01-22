from django import forms
from .models import *
from django.contrib.auth.models import User
class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        
        fields = ['customer_id', 'total_price', 'status']
        widgets = {
            'customer_id': forms.Select(attrs={'class': 'form-control'}),
            'total_price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '0.00'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
        }

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        
        fields = ['fname', 'mname', 'lname', 'phone', 'Email', 'Address']
        widgets = {
            'fname': forms.TextInput(attrs={'class': 'form-control'}),
            'mname': forms.TextInput(attrs={'class': 'form-control'}),
            'lname': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'Email': forms.EmailInput(attrs={'class': 'form-control'}),
            'Address': forms.TextInput(attrs={'class': 'form-control'}),
        }


class OrderItemForm(forms.ModelForm):
    class Meta:
        model = OrderItem
        fields = ['order', 'product', 'quantity', 'price']
        widgets = {
            'order': forms.Select(attrs={'class': 'form-control'}),
            'product': forms.Select(attrs={'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
        }


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields ='__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'Description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3,}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'Image': forms.FileInput(attrs={'class': 'form-control'}),
            'stock': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class SignForm(forms.ModelForm):
    confirmpass=forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class':'form-control',
                'placeholder':'Confirm Password'
            }
        )
    )
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control','placeholder':'First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control','placeholder':'Last Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control','placeholder':'Email'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control','placeholder':'Password'}),
        }
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirmpass = cleaned_data.get('confirmpass')

        if password != confirmpass:
            raise forms.ValidationError("كلمة السر غير متطابقة!")
        if password and len(password)<8:
            raise forms.ValidationError("يجب ان تكون كلمة السر 8 رموز على الاقل")
       
        return cleaned_data
    
    
    def save(self, commit=True):
        user = super().save(commit=False)
       
        user.username = self.cleaned_data.get('email')
        
        user.set_password(self.cleaned_data.get('password'))
       
        if commit:
            user.save()
        return user
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
       
        if User.objects.filter(username=email).exists():
            raise forms.ValidationError("هذا البريد الإلكتروني مسجل بالفعل، جرب تسجيل الدخول.")
        return email

class LoginForm(forms.Form):
    email = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Email or Username'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Password'
    }))