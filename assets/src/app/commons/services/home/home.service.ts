import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';
import { domain_url, home_theme, home_category, home_subscribe} from '../../constants/global.constants';

@Injectable({
  providedIn: 'root'
})
export class HomeService {

  httpHeaders = new HttpHeaders({'Content-type': 'application/json'});
  public categories;
  constructor(private http: HttpClient) {}

  getThemes(auth){
  	return this.http.get<any>("http://"+domain_url+":8000"+home_theme+auth+"/", {headers: this.httpHeaders})
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
    return this.http.get<any>("http://"+domain_url+":8000"+home_category, {headers: this.httpHeaders})
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
    return this.http.post<any>("http://"+domain_url+":8000"+home_subscribe, data)
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
