import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class AuthService {
  rememberMe:boolean;
  token;
  user;
  domain_url = '192.168.2.30';
  constructor(private http: HttpClient) { }
  
  // Generate token upon login
  loginAuth(user,remember){
    this.rememberMe = remember;
    this.user = user;
    return this.http.post<any>("http://"+this.domain_url+":8000/user/login/", user)
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
    return this.http.post<any>("http://"+this.domain_url+"/user/register/", user)
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

  refreshToken(user){
    return this.http.get<any>("http://"+this.domain_url+"localhost:8000/user/refresh/", user)
    .toPromise()
    .then(
      response => {
        return response;
      }
    )
    .catch(
      error =>{
        return Promise.reject(error);
      }
    )
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
    if(sessionStorage['token'] == null ||
       sessionStorage['token'] == undefined){
      return JSON.parse(null);
    }
    this.token = this.refreshToken(this.user);
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

