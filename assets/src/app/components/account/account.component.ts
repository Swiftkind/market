import { Component, OnInit } from '@angular/core';

import { AuthService } from '../../commons/services/auth/auth.service';
import { Router } from '@angular/router';
import { Location } from '@angular/common'; 
import { Title } from '@angular/platform-browser';
import { FormBuilder, FormsModule, FormGroup, FormControl, Validators } from '@angular/forms';


@Component({
  selector: 'app-account',
  templateUrl: './account.component.html',
  styleUrls: ['./account.component.css'],
  providers: [AuthService]
})

export class AccountComponent implements OnInit {
  account;
  registrationForm;
  errors;
  
  constructor(
  	private authService: AuthService,
  	private router: Router,
  	private fb: FormBuilder,
  	private location: Location,
    private title: Title
  ) { }

  ngOnInit() {
  	this.account = {
  		email: "",
  		first_name: "",
  		last_name: "",
  		password: "",

	  };

  	this.registrationForm = this.fb.group({
  		first_name : new FormControl('', Validators.required),
  		last_name  : new FormControl('', Validators.required),
  		email      : new FormControl('', [Validators.required, Validators.email]),
  		password   : new FormControl('', Validators.required),
  	});

    this.title.setTitle('Sign up - Marketplace')
  }

  get first_name(){
  	return this.registrationForm.get('first_name');
  }

  get last_name(){
  	return this.registrationForm.get('last_name');
  }

  get email(){
  	return this.registrationForm.get('email');
  }

  get password(){
  	return this.registrationForm.get('password');
  }
  
	  

  register() {
    this.authService.removeToken();
    this.authService.removeSessionToken();
  	this.authService.registerAuth(this.registrationForm.value).then(
  		response => {
  			location.reload();
  			this.router.navigate(['']);
  		})
  		.catch(error => {
  			this.errors = error;
  		});
  	
  }

}
