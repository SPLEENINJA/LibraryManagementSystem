class Book:
    def __init__(self,title:str,author:str,is_available:bool=True):
        self.title=title
        self.author=author
        self.is_available=is_available

    def book_availability(self):
        available='available' if self.is_available else 'not available'
        return print(f'{self.title} by {self.author} is {self.is_available} today')
    
class Library:
    def __init__(self):
        self.books=[]

    def add_book(self,title:str,author:str, is_available: bool = True):
        book = Book(title,author,is_available)
        self.books.append(book)

    def list_books(self):
        return [str(book) for book in self.books]
    
    def load_books(self,file_path:str):
        try :
            with open(file_path,'r') as file :
                for line in file:
                    title,author,is_available=line.strip().split(',')
                    self.add_book(title,author,is_available)
        except FileNotFoundError:
            return ("Fichier n'existe pas")
        except ValueError:
            print('Erreur dans les lignes du fichier : mettre Titre, Auteur,  1 par ligne')
    
    def lend_book(self,book_title:str,student:'Student'):    
        for book in self.books:    
            if book.title== book_title and book.is_available:
                book.is_available=False
                student.borrowed_books.append(book)
                print(f"{book.title} a été emprunté par {student.name}")
                return True
        print(f"{book_title} n'est pas disponible")
        return False
    def accept_return(self,book_title:str,student:'Student'):
        for book in student.borrowed_books:
            if book.title==book_title and book.title in student.borrowed_books:
                student.borrowed_books.remove(book)
                book.is_available=True
                print(f"{student.name} a bien rendu {book.title}")
                return
        print(f"{student.name} n'a pas emprunté {book_title}")    

    def search_books(self,query:str):
        query=query.lower()
        matching_books = []
        for book in self.books:
            if query in book.title.lower() or query in book.author.lower():
                matching_books.append(str(book))
        return print(f"Il y a {len(matching_books)} correspondances : {matching_books}")
    
    def save_books(self, file_path: str):
        try:
            with open(file_path, 'w') as file:
                for book in self.books:
                    file.write(f'{book.title},{book.author},{book.is_available}\n')
            print(f"Les livres ont été sauvegardés dans {file_path}.")
        except Exception as e:
            print(f"Erreur lors de la sauvegarde des livres : {e}")

        
class Student:
    def __init__ (self, name:str):
        self.name=name
        self.borrowed_books=[]
    def borrow_books (self,book_title:str, library: 'Library'):
        for book in library.books:
            if book.title==book_title and book.is_available:
                book.is_available= False
                self.borrowed_books.append(book)
                print(f'{self.name} prend le livre {book_title}')
                return
        print(f"Le livre {book_title} n'est pas disponible")

    def return_book(self, book_title: str,library:Library):
        for book in self.borrowed_books:
            if book.title==book_title:
                book.is_available=True
                self.borrowed_books.remove(book)
                print(f'{self.name} rend {book_title}')
                return
        print(f"{self.name} ne peut pas rendre le livre, il ne l'a pas emprunté")

library = Library()

library.load_books("books.txt")

student = Student("Alice")

student.borrow_books("1984", library)

student.return_book("1984", library)

#je n'ai pas réussi à ajouter le menu dynamique, je vous rend le fichier comme ceci c'est ma dernière sauvegarde qui fonctionne bien. je passe directement au projet django