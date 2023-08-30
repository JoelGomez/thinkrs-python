from app.Database import db, BaseModelMixin

class Users(db.Model, BaseModelMixin):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50))
    email = db.Column(db.String(120), nullable=False, unique=True)
    rol_id = db.Column(db.Integer, db.ForeignKey('roles.id'), nullable=False)

    def __init__(self, first_name, last_name, email, rol_id):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.rol_id = rol_id

    def __repr__(self):
        return f'User({self.email})'
    
    @classmethod
    def find_first_by_email(cls, email):
        return cls.query.filter_by(email=email).first()
    
    @classmethod
    def find_all_by_rol_id(cls, rol_id):
        return cls.query.filter_by(rol_id=rol_id).all()
