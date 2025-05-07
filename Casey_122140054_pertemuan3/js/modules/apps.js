import NotesManager from './modules/NotesManager.js';

const notesManager = new NotesManager();

export class NotesManager {
    constructor() {
        this.notes = [];
        this.loadFromLocalStorage();
    }

    loadFromLocalStorage() {
        const storedNotes = JSON.parse(localStorage.getItem('notes')) || [];
        this.notes = storedNotes.map(note => new Note(
            note.id,
            note.title,
            note.content,
            note.category,
            new Date(note.createdAt)
        ));
    }

    saveToLocalStorage() {
        localStorage.setItem('notes', JSON.stringify(this.notes));
    }

    addNote(title, content, category) {
        const id = Date.now().toString();
        const newNote = new Note(id, title, content, category);
        this.notes.push(newNote);
        this.saveToLocalStorage();
        return newNote;
    }

    updateNote(id, title, content, category) {
        const index = this.notes.findIndex(note => note.id === id);
        if (index !== -1) {
            this.notes[index].title = title;
            this.notes[index].content = content;
            this.notes[index].category = category;
            this.saveToLocalStorage();
            return true;
        }
        return false;
    }

    deleteNote(id) {
        this.notes = this.notes.filter(note => note.id !== id);
        this.saveToLocalStorage();
    }

    searchNotes(query) {
        const lowerQuery = query.toLowerCase();
        return this.notes.filter(note => 
            note.title.toLowerCase().includes(lowerQuery) || 
            note.content.toLowerCase().includes(lowerQuery)
        );
    }

    getCategoryCounts() {
        const counts = {
            total: this.notes.length,
            personal: 0,
            work: 0,
            study: 0,
            idea: 0
        };

        this.notes.forEach(note => {
            if (counts[note.category] !== undefined) {
                counts[note.category]++;
            }
        });

        return counts;
    }
}

export const UI = {
    elements: {
        noteForm: document.getElementById('note-form'),
        noteId: document.getElementById('note-id'),
        noteTitle: document.getElementById('note-title'),
        noteContent: document.getElementById('note-content'),
        noteCategory: document.getElementById('note-category'),
        saveBtn: document.getElementById('save-btn'),
        resetBtn: document.getElementById('reset-btn'),
        notesContainer: document.getElementById('notes-container'),
        noNotes: document.getElementById('no-notes'),
        filterCategory: document.getElementById('filter-category'),
        searchNotes: document.getElementById('search-notes'),
        clock: document.getElementById('clock'),
        date: document.getElementById('date'),
        totalNotes: document.getElementById('total-notes'),
        personalCount: document.getElementById('personal-count'),
        workCount: document.getElementById('work-count'),
        studyCount: document.getElementById('study-count'),
    },
    
    init() {
        this.updateClock();
        setInterval(() => this.updateClock(), 1000);
        this.setupEventListeners();
    },

    setupEventListeners() {
        this.elements.noteForm.addEventListener('submit', e => {
            e.preventDefault();
            this.handleFormSubmit();
        });

        this.elements.resetBtn.addEventListener('click', () => {
            this.resetForm();
        });

        this.elements.filterCategory.addEventListener('change', () => {
            this.renderNotes();
        });

        this.elements.searchNotes.addEventListener('input', () => {
            this.renderNotes();
        });
    },

    handleFormSubmit() {
        const id = this.elements.noteId.value;
        const title = this.elements.noteTitle.value;
        const content = this.elements.noteContent.value;
        const category = this.elements.noteCategory.value;

        if (id) {
            notesManager.updateNote(id, title, content, category);
        } else {
            notesManager.addNote(title, content, category);
        }

        this.resetForm();
        this.renderNotes();
        this.updateStats();
    },

    resetForm() {
        this.elements.noteId.value = '';
        this.elements.noteTitle.value = '';
        this.elements.noteContent.value = '';
        this.elements.noteCategory.value = 'personal';
        this.elements.saveBtn.textContent = 'Simpan';
    },

    renderNotes() {
        const searchQuery = this.elements.searchNotes.value;
        const category = this.elements.filterCategory.value;
        const filteredNotes = notesManager.searchNotes(searchQuery);

        this.elements.notesContainer.innerHTML = '';
        if (filteredNotes.length === 0) {
            this.elements.noNotes.classList.remove('hidden');
        } else {
            this.elements.noNotes.classList.add('hidden');
            filteredNotes.forEach(note => {
                this.createNoteCard(note);
            });
        }
    },

    createNoteCard(note) {
        const noteCard = document.createElement('div');
        noteCard.className = 'note-card bg-white border rounded-lg shadow-sm hover:shadow-md transition-shadow p-4';
        noteCard.innerHTML = `
            <h3 class="font-semibold text-lg text-gray-800">${note.title}</h3>
            <p class="text-gray-600 mb-3">${note.content}</p>
            <div class="flex justify-between items-center text-sm text-gray-500">
                <button class="edit-btn text-blue-600 hover:text-blue-800">Edit</button>
                <button class="delete-btn text-red-600 hover:text-red-800">Hapus</button>
            </div>
        `;
        
        noteCard.querySelector('.edit-btn').addEventListener('click', () => {
            this.loadNoteToForm(note);
        });

        noteCard.querySelector('.delete-btn').addEventListener('click', () => {
            notesManager.deleteNote(note.id);
            this.renderNotes();
            this.updateStats();
        });

        this.elements.notesContainer.appendChild(noteCard);
    },

    updateStats() {
        const counts = notesManager.getCategoryCounts();
        this.elements.totalNotes.textContent = counts.total;
        this.elements.personalCount.textContent = counts.personal;
        this.elements.workCount.textContent = counts.work;
        this.elements.studyCount.textContent = counts.study;
    },

    updateClock() {
        const now = new Date();
        this.elements.clock.textContent = now.toLocaleTimeString();
        this.elements.date.textContent = now.toLocaleDateString('id-ID', { 
            weekday: 'long', 
            year: 'numeric', 
            month: 'long', 
            day: 'numeric' 
        });
    }
}
