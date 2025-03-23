// Mengambil referensi elemen DOM
const todoInput = document.getElementById('todo-input');
const addButton = document.getElementById('add-btn');
const todoList = document.getElementById('todo-list');

// Array untuk menyimpan todos
let todos = [];

// Fungsi untuk menampilkan todos
function renderTodos() {
    // Membersihkan container
    todoList.innerHTML = '';
    
    // Menampilkan setiap todo
    for(let i = 0; i < todos.length; i++) {
        const todo = todos[i];
        
        // Membuat elemen untuk item todo
        const todoItem = document.createElement('div');
        
        // Menambahkan teks todo
        const todoText = document.createElement('span');
        if(todo.completed) {
            todoText.style.textDecoration = "line-through";
        }
        todoText.textContent = todo.text;
        todoItem.appendChild(todoText);
        
        // Menambahkan spasi
        todoItem.appendChild(document.createTextNode(" "));
        
        // Membuat tombol selesai
        const toggleButton = document.createElement('button');
        toggleButton.textContent = todo.completed ? 'Batal Selesai' : 'Selesai';
        toggleButton.onclick = function() {
            toggleTodo(i);
        };
        todoItem.appendChild(toggleButton);
        
        // Menambahkan spasi
        todoItem.appendChild(document.createTextNode(" "));
        
        // Membuat tombol hapus
        const deleteButton = document.createElement('button');
        deleteButton.textContent = 'Hapus';
        deleteButton.onclick = function() {
            deleteTodo(i);
        };
        todoItem.appendChild(deleteButton);
        
        // Menambahkan baris baru
        todoItem.appendChild(document.createElement('br'));
        todoItem.appendChild(document.createElement('br'));
        
        // Menambahkan item ke daftar
        todoList.appendChild(todoItem);
    }
    
    // Menyimpan ke localStorage
    saveTodos();
}

// Fungsi untuk toggle status todo
function toggleTodo(index) {
    todos[index].completed = !todos[index].completed;
    renderTodos();
}

// Fungsi untuk menghapus todo
function deleteTodo(index) {
    todos.splice(index, 1);
    renderTodos();
}

// Fungsi untuk menyimpan todos ke localStorage
function saveTodos() {
    localStorage.setItem('todos', JSON.stringify(todos));
}

// Fungsi untuk memuat todos dari localStorage
function loadTodos() {
    const storedTodos = localStorage.getItem('todos');
    if (storedTodos) {
        todos = JSON.parse(storedTodos);
        renderTodos();
    }
}

// Fungsi untuk menambah todo baru
function addTodo() {
    const text = todoInput.value.trim();
    if (text) {
        todos.push({
            text: text,
            completed: false
        });
        
        todoInput.value = '';
        renderTodos();
    }
}

// Event listener untuk tombol tambah
addButton.addEventListener('click', addTodo);

// Event listener untuk tombol enter pada input
todoInput.addEventListener('keyup', function(event) {
    if (event.key === 'Enter') {
        addTodo();
    }
});

// Memuat todos saat halaman dimuat
document.addEventListener('DOMContentLoaded', loadTodos);