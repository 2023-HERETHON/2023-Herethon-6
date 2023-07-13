from django import forms

from review.models import Review


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('reviewTitle','reviewText')
        widgets = {
            'reviewTitle': forms.TextInput(attrs={'placeholder': '제목을 입력해주세요.'}),
            'reviewText': forms.Textarea(attrs={'placeholder': '부모님과의 시간은 어땠나요?'}),
        }