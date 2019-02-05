import { Component, OnInit } from '@angular/core';
import { HomeService } from '../../commons/services/home/home.service';
import { Title } from '@angular/platform-browser';
import { CategoryPipe } from '../../commons/pipes/category/category.pipe';
import { FormBuilder, FormGroup } from '@angular/forms';

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
  categories
  searchCategory;
  promise;
  baseUrl = "http://localhost:8000/media/";


  constructor(
  	private home: HomeService,
  	private title: Title,
  	private fb: FormBuilder) {}

  ngOnInit() {
	this.getThemesHome();
	this.title.setTitle('Home - Marketplace');
	console.log(this.home.categories);
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
			console.log(category);
  			return category.toLowerCase().includes(search.toLowerCase());
  		}

  	);
  }

  getChoice(choice: string){
  	return `${choice}`;	
  }

}
