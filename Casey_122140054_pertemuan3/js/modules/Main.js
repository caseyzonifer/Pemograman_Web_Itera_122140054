import { Note } from './components/Note.js';
import { NotesManager } from './components/NotesManager.js';

// Initialize notes manager
const notesManager = new NotesManager();

// UI Controller
const UI = {
 // DOM Elements
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
   confirmModal: document.getElementById('confirm-modal'),
   confirmDelete: document.getElementById('confirm-delete'),
   cancelDelete: document.getElementById('cancel-delete'),
   clock: document.getElementById('clock'),
   date: document.getElementById('date'),
   totalNotes: document.getElementById('total-notes'),
   personalCount: document.getElementById('personal-count'),
   workCount: document.getElementById('work-count'),
   studyCount: document.getElementById('study-count')
 },

 // Initialize UI
 init() {
   this.updateClock();
   setInterval(() => this.updateClock(), 1000);
   this.setupEventListeners();
 },

 // Setup event listeners, handle submit, reset, etc...
 setupEventListeners() {
   this.elements.noteForm.addEventListener('submit', e => {
     e.preventDefault();
     this.handleFormSubmit();
   });
   this.elements.resetBtn.addEventListener('click', this.resetForm.bind(this));
   this.elements.filterCategory.addEventListener('change', this.renderNotes.bind(this));
   this.elements.searchNotes.addEventListener('input', this.renderNotes.bind(this));
   this.elements.cancelDelete.addEventListener('click', this.closeModal.bind(this));
 },

 handleFormSubmit() {
   const id = this.elements.noteId.value;
   const title = this.elements.noteTitle.value;
   const content = this.elements.noteContent.value;
   const category = this.elements.noteCategory.value;

   if (!title || !content) return;

   if (id) {
     notesManager.updateNote(id, title, content, category);
   } else {
     notesManager.addNote(title, content, category);
   }

   this.resetForm();
   this.renderNotes();
   this.updateStats();
 },

 // Other UI rendering methods...
};

document.addEventListener('DOMContentLoaded', () => {
 UI.init();
 UI.renderNotes();
 UI.updateStats();
});
