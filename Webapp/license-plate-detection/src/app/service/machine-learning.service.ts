import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class MachineLearningService {

  constructor(private http: HttpClient) { }

  machineLearningResult(file: any): any{
    const formData: FormData = new FormData();
    formData.append('file', file, file.name);
    return this.http.post('http://127.0.0.1:5000/',formData)
  }
}
