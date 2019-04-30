import { Component, OnInit } from '@angular/core';
import {Quote} from '../quote'




@Component({
  selector: 'app-quote',
  templateUrl: './quote.component.html',
  styleUrls: ['./quote.component.css']
})

export class QuoteComponent implements OnInit {

  Quotes=[
    
    new Quote(1,'Accept responsibility for your life. Know that it is you who will get you where you want to go, no one else.','~ Jacob pik',new Date(2019,10,14)),
    new Quote(2,'The best decisions aren’t made with your mind, but with your instinct.','~ Lionel Messi',new Date(2017,17,14)),
    new Quote(3,'If you don’t like something, change it. If you can’t change it, change your attitude.','~ Abraham Lincon',new Date(2015,12,14)), 
    new Quote(4,'The purpose of life is not to be happy. It is to be useful, to be honorable, to be compassionate, to have it make some difference that you have lived and lived well.','~ Ralph Waldo Emerson',new Date(2019,10,14)), 
    new Quote(5,'Almost all of the research strongly supports the benefits of using humor to maximize living.','~ Ralph Waldo Emerson',new Date(2016,10,14)), 
    new Quote(6,'Life is inherently risky. There is only one big risk you should avoid at all costs, and that is the risk of doing nothing.','~  Waldo Emer',new Date(2019,10,14)), 

 ]
 toogleDetails(index){
  this.Quotes[index].showDescription = !this.Quotes[index].showDescription;
}

addNewQuote(quote){
  let quoteLength = this.Quotes.length;
  quote.id=quoteLength+1;
  quote.completeDate = new Date(quote.completeDate)
  this.Quotes.push(quote)
}
  constructor() { }

  ngOnInit() {
  }

}

