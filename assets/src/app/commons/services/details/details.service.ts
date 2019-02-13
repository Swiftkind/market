import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class DetailsService {
  
  domain_url = '192.168.2.30';
  httpHeaders = new HttpHeaders({'Content-type': 'application/json'});
  constructor(
  	private http: HttpClient) { }

  getThemeDetailsService(id){
  	return this.http.get<any>('http://'+this.domain_url+':8000/home/theme/details/'+id+'/', {headers: this.httpHeaders})
  	.toPromise()
  	.then(
  		response =>{
  			return response;
  		}
  	)
  	.catch(
  		error => {
  			return error;
  		}
  	);
  }

  createReviewService(comment){
    return this.http.post<any>("http://"+this.domain_url+":8000/details/createReview/",comment)
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
    );
  }

  subscribeService(data){
    return this.http.post<any>("http://"+this.domain_url+":8000/home/theme/subscribe/",data)
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
