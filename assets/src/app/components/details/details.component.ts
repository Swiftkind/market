import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { DetailsService } from '../../commons/services/details/details.service';


@Component({
  selector: 'app-details',
  templateUrl: './details.component.html',
  styleUrls: ['./details.component.css']
})
export class DetailsComponent implements OnInit {
  theme_id:number;
  theme;
  constructor(
  	private route: ActivatedRoute,
  	private router: Router,
  	private detailsService: DetailsService) {}

  ngOnInit() {
  	this.route.paramMap.subscribe(
  		params => {
  			this.theme_id = +params.get('id');
  		}
  	);

  	this.getThemeDetails();

  }

  getThemeDetails(){
  	this.detailsService.getThemeDetailsService(this.theme_id)
  	.then(
  		response => {
  			this.theme = response
  			console.log(this.theme);
  		}
  	)
  	.catch(
  		error => {
  			return error;
  		}
  	)
  }

}
