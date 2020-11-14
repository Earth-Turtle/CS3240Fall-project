from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from .models import Category
from .models import Post
from .models import Comment


def createCategory(category_title, slug_value):
    return Category.objects.create(title=category_title, slug=slug_value)

def createPost(post_title, post_text, post_category, post_publish, post_slug):
    return Post.objects.create(title=post_title, text=post_text, category=post_category, publish=post_publish, slug=post_slug)


class CategoryCreationTests(TestCase):

    def testCategoryCreation(self):
        test = createCategory("Education", "Education")
        response = self.client.get(reverse('singleCategory', args=(test.slug,)), secure=True)
        self.assertEqual(response.status_code, 200)

class PostCreationTests(TestCase):

    def testPostCreation(self):
        test_cat = createCategory("Education", "Education")
        test_post = createPost("Education Template 1", "asdf", test_cat, timezone.now(), "Education0")
        response = self.client.get(reverse('comment', args=(test_cat.slug, test_post.slug,)), secure=True)
        self.assertEqual(response.status_code, 200)

class CommentModelTests(TestCase):
    
    @classmethod
    def setUpTestData(cls):
        newCategory = createCategory("Education", "Education")
        newPost = createPost("Edu template 1", "test text", newCategory, timezone.now(), "Education0")
        testComment = Comment.objects.create(post=newPost, author="test author", text="test comment body", created_date=timezone.now())

    def test_name_label(self):
        comment = Comment.objects.get(id=1)
        field_label = comment._meta.get_field('author').verbose_name
        self.assertEqual(field_label, 'author')

    def test_text_label(self):
        comment = Comment.objects.get(id=1)
        field_label = comment._meta.get_field('text').verbose_name
        self.assertEqual(field_label, 'text')

    def test_post_label(self):
        comment = Comment.objects.get(id=1)
        field_label = comment._meta.get_field('post').verbose_name
        self.assertEqual(field_label, 'post')

    def test_created_date_label(self):
        comment = Comment.objects.get(id=1)
        field_label = comment._meta.get_field('created_date').verbose_name
        self.assertEqual(field_label, 'created date')


