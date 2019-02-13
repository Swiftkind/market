import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class HomeService {

  domain_url = '192.168.2.30';
  httpHeaders = new HttpHeaders({'Content-type': 'application/json'});
  public categories;
  constructor(private http: HttpClient) {
    this.categories = this.getCategory();
   }

  getThemes(){
  	return this.http.get<any>("http://"+this.domain_url+":8000/home/theme/", {headers: this.httpHeaders})
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
    return this.http.get<any>("http://"+this.domain_url+":8000/home/theme/category/", {headers: this.httpHeaders})
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

  subscribeService(data){
    console.log('clicked');
    return this.http.post<any>("http://"+this.domain_url+":8000/home/theme/subscribe/", data)
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
