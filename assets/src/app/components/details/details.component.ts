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
  currentRate:number = 0;
  maxRate:number = 5;
  theme_id:number;
  theme;
  discount;
  dis_price;
  reviews;
  content;
  token;
  subscribe;
  message;
  domain_url = '192.168.2.30';

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

    //forms for creating a review
    this.reviews = this.fb.group({
      review : new FormControl('', Validators.required),
      rating : new FormControl('')
    });

    this.subscribe = this.fb.group({
      email : new FormControl('', Validators.required),
    });

  }

  get review(){
    return this.reviews.get('review');
  }

  get rating(){
    return this.review.get('rating');
  }

  get email(){
    return this.subscribe.get('email');
  }

  // get details of the theme
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

  //create a review and rating for the theme
  createReview(review){
    this.token = JSON.parse(localStorage.getItem('token'));
    this.content = {
      theme_id : this.theme_id,
      token    : this.token.token,
      comment  : review,
      rating   : this.currentRate
    }
    
    console.log(this.content);
    this.detailsService.createReviewService(this.content)
    .then(
      response => {
        this.getThemeDetails();
        this.review.reset();
        this.currentRate =0
        return response;
      }
    )
    .catch(
      error => {
        return error;
      }
    )
  }

  // subscribe user (details page)
  subscribeMarket(){
    this.detailsService.subscribeService(this.subscribe.value)
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

}
