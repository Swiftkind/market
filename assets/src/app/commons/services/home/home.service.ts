import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class HomeService {

  httpHeaders = new HttpHeaders({'Content-type': 'application/json'});
  public categories;
  constructor(private http: HttpClient) {
    this.categories = this.getCategory();
   }

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

  getCategory(){
    return this.http.get<any>("http://localhost:8000/home/theme/category/", {headers: this.httpHeaders})
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
