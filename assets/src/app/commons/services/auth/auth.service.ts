import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class AuthService {
  rememberMe:boolean;
  token;
  constructor(private http: HttpClient) { }
  
  // Generate token upon login
  loginAuth(user,remember){
    this.rememberMe = remember;
    return this.http.post<any>("http://localhost:8000/user/login/", user)
    .toPromise()
    .then(
      response => {
        this.setToken(response);
        return response;
    })
    .catch(error => {
      console.log(error);
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

  setToken(token){
    this.token = token;
    if(this.rememberMe == true){
      localStorage['token'] = JSON.stringify(token);
    }
    else{
      sessionStorage['token'] = JSON.stringify(token);
    }
  }

  getToken(){
    if(this.rememberMe == true){
      let token = localStorage.getItem('token');
      return JSON.parse(token);
    }
    this.getSessionToken();
  }

  getSessionToken(){
    if(sessionStorage['token'] == null){
      return JSON.parse(null);
    }
    
    sessionStorage['token'] = JSON.stringify(this.token);
    let token = sessionStorage.getItem('token');
    return JSON.parse(token);
  }

  removeToken(){
    localStorage.removeItem('token');
  }

  removeSessionToken(){
    sessionStorage.removeItem('token');
  }
}  