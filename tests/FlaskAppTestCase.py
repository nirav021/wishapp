import unittest
from flask import Flask
from pymongo import MongoClient
from app import app  # Import your Flask app


class FlaskAppTestCase(unittest.TestCase):
    def setUp(self):
        """ Set up a test client for the Flask app """
        self.app = app.test_client()
        self.app.testing = True  # Enable Flask's testing mode

    def test_invalid_method(self):
        """Test that an invalid request method returns a 405 status code"""
        response = self.app.post('/')  # Assuming / accepts GET; using POST here
        self.assertEqual(response.status_code, 405)


class MongoDBTestCase(unittest.TestCase):
    def setUp(self):
        """ Set up a MongoDB test client """
        self.client = MongoClient('mongodb://localhost:27017/')
        self.db = self.client['test_database']

    def test_mongodb_connection(self):
        """ Test the MongoDB connection using ping """
        try:
            self.client.admin.command('ping')
            connection = True
        except Exception as e:
            connection = False
        self.assertTrue(connection)


class MongoDBWriteTestCase(unittest.TestCase):
    def setUp(self):
        """ Set up a MongoDB test client """
        self.client = MongoClient('mongodb://localhost:27017/')
        self.db = self.client['test_database']

    def test_mongodb_write(self):
        """ Test writing a document to MongoDB """
        test_doc = {"name": "Test Document"}

        # Insert the document
        result = self.db.test_collection.insert_one(test_doc)

        # Check if document is successfully inserted
        self.assertIsNotNone(result.inserted_id)

        # Verify if the document exists in the database
        inserted_doc = self.db.test_collection.find_one({"_id": result.inserted_id})
        self.assertIsNotNone(inserted_doc)
        self.assertEqual(inserted_doc['name'], "Test Document")


if __name__ == '__main__':
    unittest.main()