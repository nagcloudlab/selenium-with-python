import { CommonModule } from '@angular/common';
import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { RouterOutlet } from '@angular/router';

@Component({
  selector: 'app-root',
  imports: [RouterOutlet,CommonModule,FormsModule],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css'
})
export class AppComponent {
  title = 'front-end';

  newTodo: string = '';

  todos: any[] = [];

  addTodo() {
    if (this.newTodo.trim()) {
      this.todos.push({ text: this.newTodo, completed: false, id: Date.now() });
      this.newTodo = ''; // Clear the input field after adding
    }
  }

  clearInput() {
    this.newTodo = ''; // Clear the input field
  }

  deleteTodo(todo: any) {
    this.todos = this.todos.filter(t => t.id !== todo.id); // Remove the todo from the list
  }

  toggleTodoCompletion(todo: any) {
    todo.completed = !todo.completed; // Toggle the completion status
  }

}
