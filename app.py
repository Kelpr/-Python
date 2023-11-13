from models import Note
from database import init_db, Session

def add_note():
    """ Добавление новой заметки в бд. """
    title = input("Enter note title: ")
    content = input("Enter note content: ")
    new_note = Note(title=title, content=content)

    session = Session()
    session.add(new_note)
    session.commit()
    session.close()
    print("Note added successfully.")

def view_notes():
    """ Просмотр всех заметок. """
    session = Session()
    notes = session.query(Note).all()
    for note in notes:
        print(f"{note.id}: {note.title} - {note.content}")
    session.close()

def search_notes():
    """ Поиск заметок по содержимому. """
    query = input("Enter search query: ")
    session = Session()
    notes = session.query(Note).filter(Note.content.contains(query)).all()
    for note in notes:
        print(f"{note.id}: {note.title} - {note.content}")
    session.close()

def delete_note():
    """ Удаление заметки по идентификатору. """
    note_id = int(input("Enter note ID to delete: "))
    session = Session()
    note = session.query(Note).filter_by(id=note_id).one()
    session.delete(note)
    session.commit()
    session.close()
    print("Note deleted successfully.")

def main():
    init_db()

    while True:
        print("\nNotes Manager")
        print("1. Add note")
        print("2. View notes")
        print("3. Search notes")
        print("4. Delete note")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_note()
        elif choice == '2':
            view_notes()
        elif choice == '3':
            search_notes()
        elif choice == '4':
            delete_note()
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()
