import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { domain_url } from '../../constants/global.constants';

@Injectable({
  providedIn: 'root'
})
export class CartService {

  httpHeaders = new HttpHeaders({'Content-type':'application/json'});
  edit;

  constructor(
  	private http: HttpClient) { }

  getThemeCart(id){
  	return this.http.get<any>('http://'+domain_url+':8000/home/theme/cart/'+id+'/', {headers: this.httpHeaders})
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

  buyThemeService(id){
    return this.http.get<any>('http://'+domain_url+':8000/details/download/'+id+'/', {headers: this.httpHeaders})
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

  editLicenseService(id,license_id){
    this.edit = {'id': id, 'license_id': license_id}
    return this.http.post<any>('http://'+domain_url+':8000/home/theme/edit_license/', this.edit)
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
