from alayatodo import db

class users(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), nullable=False)
    password = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return '<user {}>'.format(self.username)  

class todos(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'),
        nullable=False)
    description = db.Column(db.String(255))
    completed = db.Column(db.Boolean)

    def __repr__(self):
        return '<todo {}>'.format(self.description) 