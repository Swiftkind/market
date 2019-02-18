# users/views.py
from .models import User
from rest_framework import viewsets
from django.db import IntegrityError
from django.views.decorators.http import require_http_methods
from django.contrib.auth import authenticate, login
from .serializers import UserSerializer, LoginSerializer, RegisterSerializer
from .managers import UserManager
from rest_framework.exceptions import ValidationError
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import parsers, renderers
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token

class UserViewSet(viewsets.ModelViewSet):
	"""user view set end point 
	"""
	queryset = User.objects.all()
	serializer_class = UserSerializer
	permission_classes = IsAuthenticated
	

class Login(APIView):
	"""login
	"""
	serializer_class = LoginSerializer
	permission_classes = (AllowAny,)

	def post(self,*args,**kwargs):
		serializer = self.serializer_class(
			data=self.request.data, request=self.request)

		serializer.is_valid(raise_exception=True)
		token, _ = Token.objects.get_or_create(user=serializer.user)

		return Response({
			'token': token.key,
		}, status=200, headers={'Authorization': 'Token {}'.format(token.key)})


class Register(APIView):
	"""register
	"""

	serializer_class = RegisterSerializer
	permission_classes = (AllowAny,)

	def post(self,request,*args,**kwargs):
		serializer = self.serializer_class(
			data=self.request.data)
		
		serializer.is_valid(raise_exception=True)
	
		user = serializer.save()
		user.set_password(serializer.data['password'])	
		user.save()

		token, _ = Token.objects.get_or_create(user=user)
		
		return Response({
			'token': token.key,
		}, status=200, headers={'Authorization': 'Token {}'.format(token.key)})


########################

# users/serializers.py
from rest_framework import serializers
from .models import User
from django.contrib.auth import authenticate, login
from rest_framework.authtoken.models import Token
from django.utils.translation import ugettext_lazy as _

class UserSerializer(serializers.ModelSerializer):
    """user serializer
    """
    class Meta:
        model = User

        fields = (
            'id',   
            'email',
            'first_name',
            'last_name',
        )

class LoginSerializer(serializers.Serializer):
    """login serializer
    """

    user = None

    email = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True)

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        return super(LoginSerializer, self).__init__(*args, **kwargs)

    def validate(self, data):
        """ validate email credentials
        """
        email, password = data.values()

        if not email or not password:
            msg = _('Must include "email" and "password".')
            raise serializers.ValidationError(msg, code='authorization')

        self.user = authenticate(request=self.request,
            email=email, password=password)
        
        if not self.user:
            msg = _('Invalid email or password')
            raise serializers.ValidationError(msg, code='authorization')

        
        return data


class RegisterSerializer(serializers.ModelSerializer):
    """login serializer
    """
    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'email',
            'password',
        )

    def validate(self,data):
        first_name, last_name, email, password = data.values()

        if not first_name or not last_name or not email or not password:
            msg = _('Must include all fields!')
            raise serializersl.ValidationError(msg, code='authorization')

        self.user = authenticate(
            email=email)

        if self.user:
            msg = _('Email already existed!')
            raise serializers.ValidationError(msg, code='authorization')
        
        return data
    
    def get_token(self):
        if not self.user:
            msg = _('Unable to login with provided credentials.')
            raise serializers.ValidationError(msg, code="authorization")

        token, created = Token.objects.get_or_create(user=self.user)
        return token
    
##################

# users/urls.py
from django.urls import path, include
from . import views
from rest_framework import routers
# from rest_framework.authtoken.views import ObtainAuthToken

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
# router.register(r'register', views.RegisterViewSet)
# router.register(r'login', views.Login)

urlpatterns = [
    path('', include(router.urls)),
    path('login/', views.Login.as_view()),
    path('register/', views.Register.as_view()),
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),

]


####################################
# ASSETS
# assets/src/app/commons/services/auth/authservice.ts
import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class AuthService {

  constructor(private http: HttpClient) { }

  // Generate token upon login
  loginAuth(user){
  	return this.http.post<any>("http://localhost:8000/user/login/", user)
    .toPromise()
    .then(
      response => {
        this.setToken(response);
        return response;
    })
    .catch(error => {
      return Promise.reject(error);
    });
  } 

  // Generate token upon register
  registerAuth(user){
  	return this.http.post<any>("http://localhost:8000/user/register/", user)
    .toPromise()
    .then(
      response => {
        this.setToken(response);
        return response;
    })
    .catch(error => {
      return Promise.reject(error);
    });
  }

  logout(){

  }

  setToken(token){
    localStorage['token'] = JSON.stringify(token);
  }

  getToken(){
  	let token = localStorage.getItem('token');
    return JSON.parse(token);
  }

  removeToken(){
    localStorage.removeItem('token');
  }
}

#######################
# assets/src/app/app.module.ts
import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { HttpClientModule,HTTP_INTERCEPTORS } from '@angular/common/http';
import { RouterModule, Routes } from "@angular/router";
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { AppRoutingModule } from './app-routing.module';

//Service
import { TokenService } from './commons/services/interceptors/token.service';

//Modules
import { AccountModule } from './components/account/account.module';

//Components
import { AppComponent } from './app.component';
import { HomeComponent } from './components/home/home.component';
import { CartComponent } from './components/cart/cart.component';
import { DetailsComponent } from './components/details/details.component';
import { AccountComponent } from './components/account/account.component';

//Routes
const routes: Routes = [
	{ path: '', component: HomeComponent },
	{ path: 'details', component: DetailsComponent },
	{ path: 'cart', component: CartComponent },
	{ path: 'account', component: AccountComponent }
]

@NgModule({
  declarations: [
    AppComponent,
    HomeComponent,
    CartComponent,
    DetailsComponent,
    AccountComponent,

  ],
  imports: [
  	AccountModule,
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    FormsModule,
    ReactiveFormsModule,
    RouterModule.forRoot(routes, {onSameUrlNavigation: 'reload'}),
  ],
  providers: [
  {
    provide: HTTP_INTERCEPTORS,
    useClass: TokenService,
    multi: true
  }
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }


########################
# assets/src/app/app.component.ts
import { Component } from '@angular/core';
import { AuthService} from './commons/services/auth/auth.service';
import { FormControl, FormBuilder, Validators } from '@angular/forms';
import { Router } from '@angular/router';
import { Location } from '@angular/common';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css'],
  providers: [AuthService]
})
export class AppComponent {
  title = 'angular';
  usersForm;
  errors;
  constructor(
    private authService: AuthService,
    private fb: FormBuilder, 
    private router: Router,
    private location: Location
  ){ 
    this.usersForm = this.fb.group({
      email : new FormControl('', [Validators.required, Validators.email]),
      password : new FormControl('', Validators.required)
    });
  }

  get username(){
    return this.usersForm.get('username');
  }

  get password(){
    return this.usersForm.get('password');
  }

  
  login(){
    this.authService.loginAuth(this.usersForm.value)
    .then(
       response => {
          console.log(response); 
          location.reload();
          this.router.navigate(['']);
      })
    .catch(
        error => {
          this.errors = error.error.non_field_errors;
          console.log(error);
          return this.errors;
      });
    
  }

}






