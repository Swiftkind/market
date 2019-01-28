import { Component, OnInit } from '@angular/core';
import { HomeService } from '../../commons/services/home/home.service';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent implements OnInit {
  themes;
  baseUrl = "http://localhost:8000/media/";
  constructor(private home: HomeService) {
  }

  ngOnInit() {
	this.getThemesHome();

  }

  getThemesHome(){
	this.home.getThemes()
	.then(
		response => {
			this.themes = response.data;
			console.log(this.themes);
			return response;
		}
	)
	.catch(
		error => {
			console.log(error);
			return error;
		}
	)
  }

}
