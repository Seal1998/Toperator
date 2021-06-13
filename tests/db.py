from database.models import User

User.add('Testuser', 12312312)

q_user = User.get_by_tid(12312312)
print(q_user)