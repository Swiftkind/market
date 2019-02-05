import { Pipe, PipeTransform } from '@angular/core';

@Pipe({
  name: 'category'
})
export class CategoryPipe implements PipeTransform {

  transform(category:any, args?: any): any {
    if(args === undefined) return category;

    return category.filter(
    	cat => {
    		console.log(cat.category__category.toLowerCase());
    		return cat.category__category.toLowerCase().includes(args.toLowerCase());   	
    	}
    )
  }

}
