from django.core.files.uploadedfile import SimpleUploadedFile
from django.urls import reverse

from rest_framework.test import APITestCase

from assessment.settings import MEDIA_ROOT

from utils.utils import monster_b_data


class MonsterAPISetUp(APITestCase):
    def post_file(self, file_to_upload: SimpleUploadedFile):
        return self.client.post(
            self.url_import,
            {
                "file": file_to_upload,
            },
            format="multipart",
        )

    def setUp(self):
        def file_path(file_name: str) -> str:
            return f"{MEDIA_ROOT}/{file_name}"

        with open(file_path("monsters-correct.csv"), "rb") as correct_data:
            self.correct_csv = SimpleUploadedFile(
                name="monsters-correct.csv",
                content=correct_data.read(),
                content_type="multipart/form-data",
            )

        self.monster_data = monster_b_data
        self.monster_data["id"] = 6

        self.url_import = reverse("monster:monster_import")
        self.url_list_create = reverse("monster:monster_list_create")

        return super().setUp()
