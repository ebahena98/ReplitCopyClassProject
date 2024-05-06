from django import forms

from post.models import Post 


class CreatePostForm(forms.ModelForm):

	class Meta:
		model = Post
		fields = ['title', 'body', 'image']


class UpdatePostForm(forms.ModelForm):

	class Meta:
		model = Post
		fields = ['title', 'body', 'image']

	def save(self, commit=True):
		user_post = self.instance
		user_post.title = self.cleaned_data['title']
		user_post.body = self.cleaned_data['body']

		if self.cleaned_data['image']:
			user_post.image = self.cleaned_data['image']

		if commit:
			user_post.save()
		return user_post