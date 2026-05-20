from datetime import datetime

class Todo:
    def __init__(self, id, title):
        self.id = id
        self.title = title
        self.completed = False
        self.created_at = datetime.now()
    
    def mark_completed(self):
        self.completed = True
    
    def get_display(self):
        status = "✓" if self.completed else "Not completed"
        return f"[{self.id}] {self.title} - {status}"

# Test it
todo1 = Todo(1, "Buy groceries")
print(todo1.get_display())

todo1.mark_completed()
print(todo1.get_display())

todo2 = Todo(2, "Learn Python")
print(todo2.get_display())


class TodoList:
    def __init__(self):
        self.todos = []
        self.next_id = 1
    
    def add_todo(self, title):
        todo = Todo(self.next_id, title)
        self.todos.append(todo)
        self.next_id += 1
    
    def get_all_todos(self):
        return self.todos
    
    def mark_todo_completed(self, todo_id):
        todo = self.get_todo_by_id(todo_id)
        if todo:
            todo.mark_completed()
            return True
        return False
    
    def delete_todo(self, todo_id):
        for i, todo in enumerate(self.todos):
            if todo.id == todo_id:
                self.todos.pop(i)
                return True
        return False
    
    def get_todo_by_id(self, todo_id):
        for todo in self.todos:
            if todo.id == todo_id:
                return todo
        return None
    
    def save_to_file(self, filename):
        """Save all todos to a JSON file"""
        import json
        todos_data = []
        for todo in self.todos:
            todos_data.append({
                "id": todo.id,
                "title": todo.title,
                "completed": todo.completed
            })
        
        with open(filename, "w") as f:
            json.dump(todos_data, f, indent=2)
        print(f"Todos saved to {filename}")
    
    def display_all_todos(self):
        """Print all todos"""
        if not self.todos:
            print("No todos yet!")
            return
        
        for todo in self.todos:
            print(todo.get_display())
        


# Test the TodoList class
print("=== Testing TodoList ===")
todo_list = TodoList()

# Add todos
todo_list.add_todo("Buy groceries")
todo_list.add_todo("Learn Python")
todo_list.add_todo("Build a project")

print(f"Total todos: {len(todo_list.get_all_todos())}")
print("\nAll todos:")
for todo in todo_list.get_all_todos():
    print(todo.get_display())

# Mark as completed
print("\n--- Marking todo 1 as completed ---")
todo_list.mark_todo_completed(1)
for todo in todo_list.get_all_todos():
    print(todo.get_display())

# Delete a todo
print("\n--- Deleting todo 2 ---")
todo_list.delete_todo(2)
print(f"Total todos: {len(todo_list.get_all_todos())}")
for todo in todo_list.get_all_todos():
    print(todo.get_display())

    