from src.NotesStorage import NotesStorage
from src.NotesService import NotesService
from src.Note import Note
from unittest.mock import *
from unittest import TestCase, main

class test_NotesService(TestCase):
    def test_NotesService_add(self):
        with patch.object(NotesStorage, 'add', MagicMock(return_value=True)):
            service = NotesService(NotesStorage())
            self.assertEqual(service.add(Note("test", 4)), True)

    def test_NotesService_averageOf(self):
        with patch.object(NotesStorage, 'getAllNotesOf', MagicMock(return_value=[4.5, 4.5, 3, 3, 5])):
            service = NotesService(NotesStorage())
            self.assertEqual(service.averageOf("test"), 4)

    def test_NotesService_averageOf_empty(self):
        with patch.object(NotesStorage, 'getAllNotesOf', MagicMock(return_value=[])):
            service = NotesService(NotesStorage())
            self.assertFalse(service.averageOf("noname"))

    def test_NotesService_averageOf_float(self):
        with patch.object(NotesStorage, 'getAllNotesOf', MagicMock(return_value=[5, 4.5, 2])):
            service = NotesService(NotesStorage())
            self.assertAlmostEqual(service.averageOf("test"), 3.83, 2)

    def test_NotesService_clear(self):
        with patch.object(NotesStorage, 'getAllNotesOf', MagicMock(return_value=[])):
            service = NotesService(NotesStorage())
            self.assertFalse(service.clear())


if __name__ == '__main__':
    main()