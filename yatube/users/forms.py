from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model


User = get_user_model()


# собственный класс для форма регистрации
class CreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        # модель с которой будет связана создаваемая форма
        model = User
        # укажем какие полня должны быть видны в форме и в каком порядке
        fields = ('first_name', 'last_name', 'username', 'email')
