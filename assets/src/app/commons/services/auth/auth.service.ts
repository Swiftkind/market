import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { domain_url } from '../../constants/global.constants';

@Injectable({
  providedIn: 'root'
})
export class AuthService {
  rememberMe:boolean;
  token;
  user;

  constructor(private http: HttpClient) { }
  
  // Generate token upon login
  loginAuth(user,remember){
    localStorage['remember'] = JSON.stringify(remember);
    return this.http.post<any>("http://"+domain_url+":8000/user/login/", user)
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
    return this.http.post<any>("http://"+domain_url+":8000/user/register/", user)
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
    return this.http.get<any>("http://"+domain_url+":8000/user/refresh/", user)
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
    localStorage['token'] = JSON.stringify(token);
  }

  getToken(){
      let token = localStorage.getItem('token');
      return JSON.parse(token);

  }


  removeToken(){
    localStorage.removeItem('token');
  }

  removeSessionToken(){
    sessionStorage.removeItem('token');
  }
}  

