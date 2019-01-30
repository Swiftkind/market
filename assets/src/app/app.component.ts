import { Component, OnInit } from '@angular/core';
import { AuthService} from './commons/services/auth/auth.service';
import { FormControl, FormBuilder, Validators } from '@angular/forms';
import { Router } from '@angular/router';
import { Location } from '@angular/common';
import { Title } from '@angular/platform-browser';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css'],
  providers: [AuthService]
})
export class AppComponent implements OnInit {
  usersForm;
  errors;
  rememberMe:boolean = false;
  constructor(
    private authService: AuthService,
    private fb: FormBuilder, 
    private router: Router,
    private location: Location,
    private title: Title,
  ){ }

  ngOnInit(){
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
    this.authService.loginAuth(this.usersForm.value,this.rememberMe)
    .then(
       response => {
          location.reload();
          this.router.navigate(['']);
      })
    .catch(
        error => {
          this.errors = error.error.non_field_errors;
          return this.errors;
      });
    
  }

}