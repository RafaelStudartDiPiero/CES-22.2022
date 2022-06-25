from user import User
from document import *

user1 = User('Carlos', False)
user2 = User('Rafael', True)

document1 = Document(user1, 'Teste')
document2 = Document(user1, 'Teste1')

document1.publish(user1)

document1.publish(user2)
document1.publish(user2)
print()
document1.go_back(user1)
print()
document1.go_back(user2)
document1.render(user1)
