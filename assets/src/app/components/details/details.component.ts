import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { DetailsService } from '../../commons/services/details/details.service';
import { Title } from '@angular/platform-browser';
import { FormBuilder, FormGroup, FormControl, Validators } from '@angular/forms';  

@Component({
  selector: 'app-details',
  templateUrl: './details.component.html',
  styleUrls: ['./details.component.css']
})
export class DetailsComponent implements OnInit {
  theme_id:number;
  theme;
  discount;
  dis_price;
  reviews;
  currentRate:number = 0;
  maxRate:number = 5;

  constructor(
  	private route: ActivatedRoute,
  	private detailsService: DetailsService,
  	private title: Title,
    private fb: FormBuilder) {}

  ngOnInit() {
  	this.route.paramMap.subscribe(
  		params => {
  			this.theme_id = +params.get('id');
  		}
  	);
  	this.getThemeDetails();

    this.reviews = this.fb.group({
      review : new FormControl('', Validators.required)
    });

  }

  get review(){
    return this.reviews.get('review');
  }

  getThemeDetails(){
  	this.detailsService.getThemeDetailsService(this.theme_id)
  	.then(
  		response => {
  			this.theme = response
        this.theme.price = this.theme.price.toFixed(2);
  			this.title.setTitle('Details - '+this.theme.name);
        
        if(this.theme.discount != null){
          this.dis_price = this.theme.price * this.theme.discount;
          this.dis_price = this.theme.price - this.dis_price;
          this.dis_price = this.dis_price.toFixed(2);
        }


  		}
  	)
  	.catch(
  		error => {
  			return error;
  		}
  	)
  }


  
}
