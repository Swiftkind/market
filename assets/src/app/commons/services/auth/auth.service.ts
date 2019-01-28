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
