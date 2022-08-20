import { Component, OnInit } from '@angular/core';
import { MachineLearningService } from '../service/machine-learning.service';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.scss']
})
export class HomeComponent implements OnInit {
  imageLoaded = false
  imageSrc: any
  loadApp  = false;
  imageFile: any
  numberExtracted = ''
  loader = false
  resultbar = false
  constructor(private machineLearningService: MachineLearningService) {
   }

  ngOnInit(): void {
    
  }
  onImageUpload(event :any): void{
    if (event.target.files && event.target.files[0]) {

      this.imageFile = event.target.files[0];
      const fileReader = new FileReader();
      fileReader.onload = () => {
        this.imageLoaded = true
        return this.imageSrc = fileReader.result;
      };
  
      fileReader.readAsDataURL(this.imageFile);
      
    }
  }
  onSubmit(){
    this.loader = true
    this.resultbar = true
    this.machineLearningService.machineLearningResult(this.imageFile).subscribe((res: any) => {
      console.log(res);
      this.numberExtracted = res.license
    })
  }
  goToApp=()=>{
    this.loadApp = true
  }
}
