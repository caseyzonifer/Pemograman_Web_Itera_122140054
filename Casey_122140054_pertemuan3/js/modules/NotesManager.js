// js/modules/NotesManager.js

class NotesManager {
    constructor() {
        this.notes = [];
        this.loadNotes();
    }

    // Simpan catatan di localStorage
    saveNotes() {
        localStorage.setItem('notes', JSON.stringify(this.notes));
    }

    // Muat catatan dari localStorage
    loadNotes() {
        const notesData = localStorage.getItem('notes');
        if (notesData) {
            this.notes = JSON.parse(notesData);
        }
    }

    // Tambah catatan
    addNote(note) {
        this.notes.push(note);
        this.saveNotes();
    }

    // Edit catatan
    editNote(noteId, updatedNote) {
        const index = this.notes.findIndex(note => note.id === noteId);
        if (index !== -1) {
            this.notes[index] = updatedNote;
            this.saveNotes();
        }
    }

    // Hapus catatan
    deleteNote(noteId) {
        this.notes = this.notes.filter(note => note.id !== noteId);
        this.saveNotes();
    }

    // Ambil semua catatan
    getAllNotes() {
        return this.notes;
    }
}

// Ekspor NotesManager untuk digunakan di file lain
export default NotesManager;
