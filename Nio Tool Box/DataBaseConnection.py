from pymongo import MongoClient


def get_database():

    

    CONNECTION_STRING = "mongodb+srv://mkdjspython12:NumaniNumani@mkd.djbglnr.mongodb.net/?retryWrites=true&w=majority"

    client = MongoClient(CONNECTION_STRING)

    return client['Users']


if __name__ == "__main__":

    dbname = get_database()
