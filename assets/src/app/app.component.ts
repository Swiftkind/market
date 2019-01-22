import { Component } from '@angular/core';
import { AuthService} from './commons/services/auth/auth.service';
import { FormControl, FormBuilder, Validators } from '@angular/forms';
import { Router } from '@angular/router';
import { Location } from '@angular/common';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css'],
  providers: [AuthService]
})
export class AppComponent {
  title = 'angular';
  usersForm;
  errors;
  constructor(
    private authService: AuthService,
    private fb: FormBuilder, 
    private router: Router,
    private location: Location
  ){ 
    this.usersForm = this.fb.group({
      email : new FormControl('', [Validators.required, Validators.email]),
      password : new FormControl('', Validators.required)
    });
  }

  get username(){
    return this.usersForm.get('username');
  }

  get password(){
    return this.usersForm.get('password');
  }

  
  login(){
    this.authService.loginAuth(this.usersForm.value)
    .then(
       response => {
          console.log(response); 
          location.reload();
          this.router.navigate(['']);
      })
    .catch(
        error => {
          this.errors = error.error.non_field_errors;
          console.log(error);
          return this.errors;
      });
    
  }

}
