import os
import dotenv
from supabase import create_client, Client
from link_bio.model.Featured import Featured


class SupabaseAPI:

    dotenv.load_dotenv()

    SUPABASE_URL = os.environ.get("SUPABASE_URL")
    SUPABASE_KEY = os.environ.get("SUPABASE_KEY")

    def __init__(self) -> None:
        if self.SUPABASE_URL != None and self.SUPABASE_KEY != None:
            self.supabase: Client = create_client(
                self.SUPABASE_URL, self.SUPABASE_KEY
            )

    def featured(self) -> list[Featured]:

        response = self.supabase.table("Featured").select("*").order(
            "init_date", desc=True).limit(2).execute()

        featured_data = []

        if len(response.data) > 0:
            for featured_item in response.data:
                title = featured_item["title"]
                featured_data.append(
                    Featured(
                        title=title,
                        image=self._resolve_featured_image(title, featured_item["image"]),
                        url=featured_item["url"]
                    )
                )

        return featured_data

    def _resolve_featured_image(self, title: str, image_path: str) -> str:
        normalized_title = title.casefold()

        if "python" in normalized_title:
            return "/python_highlighted.png"

        if "sql" in normalized_title:
            return "/sql_highlighted.png"

        return self._normalize_image_path(image_path)

    def _normalize_image_path(self, image_path: str) -> str:
        image_path = image_path.strip()

        if image_path.startswith(("http://", "https://", "/")):
            return image_path

        if image_path.startswith("assets/"):
            image_path = image_path.removeprefix("assets/")

        return f"/{image_path}"