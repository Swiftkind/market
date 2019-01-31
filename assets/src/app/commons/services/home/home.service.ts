import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class HomeService {

  httpHeaders = new HttpHeaders({'Content-type': 'application/json'});
  constructor(private http: HttpClient) { }

  getThemes(){
  	return this.http.get<any>("http://localhost:8000/home/theme/", {headers: this.httpHeaders})
  	.toPromise()
  	.then(
  		response => {
  			return response;  		
  		}
  	)
  	.catch(
  		error => {
  			return error;
  		}
  	)
  }

}
