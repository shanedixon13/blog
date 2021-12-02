from django.http import response
from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from .models import Post


class BlogTests(TestCase):
    def setUp(self):
        self.user=get_user_model().objects.create_user(
            username="test",
            email="test@email.com",
            password="secret"
        )
        self.post=Post.objects.create(
            title="A Title",
            body="A Body",
            author=self.user
        )
    
    def test_string_representation(self):
        post=Post(title="A sample title")
        self.assertEqual(str(post), post.title)

    def test_get_absolute_url(self):
        self.assertEqual(str(self.post.get_absolute_url()), '/posts/1/')

    def test_post_content(self):
        self.assertEqual(f"{self.post.title}", "A Title")
        self.assertEqual(f"{self.post.body}", "A Body")
        self.assertEqual(f"{self.post.author}", "test")

    def test_post_list_view(self):
        response=self.client.get(reverse('post_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "A Body")
        self.assertTemplateUsed(response, 'post_list.html')

    def test_post_detail_view(self):
        response=self.client.get("/posts/1/")
        not_found_response=self.client.get("/posts/1000/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(not_found_response.status_code, 404)
        self.assertContains(response, "A Title")
        self.assertTemplateUsed(response, 'post_detail.html')

    def test_post_create_view(self):
        response=self.client.post(reverse('post_new'),{
            "title":"new title",
            "body":"new body",
            "author":self.user.id
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Post.objects.last().title,"new title")
        self.assertEqual(Post.objects.last().body,"new body")

    def test_post_edit_view(self):
        response=self.client.post(reverse('post_edit', args=[1]), {
            "title":"updated title",
            "body": "updated body"
        })
        self.assertEqual(response.status_code, 302)

    def test_post_delete_view(self):
        response=self.client.post(reverse('post_delete', args=[1]))
        self.assertEqual(response.status_code, 302)