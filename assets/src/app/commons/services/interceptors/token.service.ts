import { Injectable, Injector } from '@angular/core';
import { HttpInterceptor, HttpRequest, HttpHandler, HttpEvent} from '@angular/common/http';
import { AuthService } from '../auth/auth.service';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class TokenService implements HttpInterceptor{
  token;
  constructor(private injector: Injector) { }

  intercept(req: HttpRequest<any>, next: HttpHandler): Observable <HttpEvent<any>>{
    let authService = this.injector.get(AuthService);
    this.token = authService.getToken();
    let request = req.clone({  
      setHeaders: {
        Authorization: 'Bearer '+this.token
      }
    });
    return next.handle(request);

  }

}
