from system.core.model import *
class Message(Model):
  def __init__(self):
    super(Message, self).__init__()

  def get_all_messages(self):
    query = "SELECT * FROM messages"
    return self.db.query_db(query)

  def get_3_messages(self):
    query = "SELECT * FROM message ORDER BY id DESC LIMIT 3"
    return self.db.query_db(query)

  def create_message(self, info):
    query = "INSERT INTO messages (content, name) VALUES (:content, :name)"
    data = { 'content': info['content'], 'name': info['name'] }
    return self.db.query_db(query, data)