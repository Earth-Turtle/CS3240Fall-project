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
        response = self.client.get(reverse('singleCategory', args=(test.slug,)))
        self.assertEqual(response.status_code, 200)

class PostCreationTests(TestCase):

    def testPostCreation(self):
        test_cat = createCategory("Education", "Education")
        test_post = createPost("Education Template 1", "asdf", test_cat, timezone.now(), "Education0")
        response = self.client.get(reverse('comment', args=(test_cat.slug, test_post.slug,)))
        self.assertEqual(response.status_code, 200)

class CommentPostTests(TestCase):

    def errorOnBlankComment(self):
        # TODO: implement this test
        self.assertTrue(True)
