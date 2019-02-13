import { Component, OnInit } from '@angular/core';
import { HomeService } from '../../commons/services/home/home.service';
import { Title } from '@angular/platform-browser';
import { CategoryPipe } from '../../commons/pipes/category/category.pipe';
import { FormBuilder, FormGroup, FormControl, Validators } from '@angular/forms';

const categories = ['Angular JS','E-Commerce','General','Bootstrap 4'];

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
  domain_url = '192.168.2.30';
  baseUrl = "http://"+this.domain_url+":8000/media/";
  subscriber;

  constructor(
    private home: HomeService,
    private title: Title,
    private fb: FormBuilder) {}

  ngOnInit() {
    this.getThemesHome();
    this.title.setTitle('Home - Marketplace');
    this.subscriber = this.fb.group({
      email : new FormControl('', Validators.required)
    });

  }

  get email(){
    return this.subscriber.email;
  }

  getThemesHome(){
    this.home.getThemes()
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
        console.log(response);
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
