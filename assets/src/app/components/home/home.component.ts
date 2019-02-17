import { Component, OnInit } from '@angular/core';
import { HomeService } from '../../commons/services/home/home.service';
import { Title } from '@angular/platform-browser';
import { CategoryPipe } from '../../commons/pipes/category/category.pipe';
import { FormBuilder, FormGroup, FormControl, Validators } from '@angular/forms';
import { domain_url,categories } from '../../commons/constants/global.constants';
import { AuthService } from '../../commons/services/auth/auth.service';
import { AppComponent } from '../../app.component';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css'],
  providers: [CategoryPipe,HomeService]

})
export class HomeComponent implements OnInit {
  themes;
  category;
  searchCategory;
  baseUrl = "http://"+domain_url+":8000/media/";
  subscriber;
  message;
  authenticate;
  authenticated;
  login;

  constructor(
    private home: HomeService,
    private title: Title,
    private fb: FormBuilder,
    private app: AppComponent) {}

  ngOnInit() {
    this.authenticated = this.isAuthenticated();
    this.getThemesHome(this.authenticated);
    this.title.setTitle('Home - Marketplace');

    this.subscriber = this.fb.group({
      email : new FormControl('', Validators.required)
    });

    this.login = this.app.usersForm;
    

  }

  get email(){
    return this.subscriber.email;
  }

  getThemesHome(auth){
    this.home.getThemes(auth)
    .then(
        response => {
            this.themes = response.data;
            this.category = response.category
            return response;
        }
    )
    .catch(
        error => {
            return error;
        }
    )
  }

  findCategory(search: string){ 
    return categories.filter(
        category => {
            return category.toLowerCase().includes(search.toLowerCase());
        }

    );
  }

  getChoice(choice: string){
    return `${choice}`; 
  }

  subscribeMarket(){
    console.log('clicked');
    this.home.subscribeService(this.subscriber.value)
    .then(
      response => {
        this.message = response.message;
        return response;
      }
    )
    .catch(
      error => {
        return error;
      }
    )
  }

  isAuthenticated(){
    this.authenticate = localStorage.getItem('token');
    if(this.authenticate === null || this.authenticate === undefined){
      return false;
    }
    return true;
  }

}
