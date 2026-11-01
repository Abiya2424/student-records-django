from django.test import TestCase
from django.urls import reverse
from .models import Student


def make_student():
    return Student.objects.create(
        name="Anu Thomas",
        email="anu@example.com",
        course="BVoc",
        year=1,
    )


class StudentModelTests(TestCase):
    def test_create_student(self):
        make_student()
        self.assertEqual(Student.objects.count(), 1)

    def test_student_name_saved(self):
        s = make_student()
        self.assertEqual(s.name, "Anu Thomas")


class StudentViewTests(TestCase):
    def test_list_page_loads(self):
        response = self.client.get(reverse("student_list"))
        self.assertEqual(response.status_code, 200)

    def test_list_shows_student(self):
        make_student()
        response = self.client.get(reverse("student_list"))
        self.assertContains(response, "Anu Thomas")

    def test_empty_list_message(self):
        response = self.client.get(reverse("student_list"))
        self.assertContains(response, "No students yet.")

    def test_add_page_loads(self):
        response = self.client.get(reverse("student_add"))
        self.assertEqual(response.status_code, 200)

    def test_edit_page_loads(self):
        s = make_student()
        response = self.client.get(reverse("student_edit", args=[s.pk]))
        self.assertEqual(response.status_code, 200)

    def test_delete_removes_student(self):
        s = make_student()
        self.client.post(reverse("student_delete", args=[s.pk]))
        self.assertEqual(Student.objects.count(), 0)

    def test_wrong_url_gives_404(self):
        response = self.client.get("/no-such-page/")
        self.assertEqual(response.status_code, 404)