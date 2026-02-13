import os
import requests
from typing import Optional, Dict, Any, List
from urllib.parse import quote_plus
from semantic_kernel.functions import kernel_function

class GitLabPlugin:
    """
    Minimal GitLab plugin for Product Owner workflows:
    - list_issues
    - create_issue
    - get_issue
    - search_merge_requests
    - add_labels_to_issue
    """

    def __init__(self, base_url: str, pat: str, default_project: Optional[str] = None):
        self.base_url = base_url.rstrip("/")
        self.pat = pat
        self.default_project = default_project
        self._session = requests.Session()
        self._session.headers.update({"PRIVATE-TOKEN": self.pat})

    def _project_url(self, project_path: str) -> str:
        return f"{self.base_url}/api/v4/projects/{quote_plus(project_path)}"

    @kernel_function(
        name="list_issues",
        description="List issues for a GitLab project, filter by state=opened/closed/all and search text.")
    def list_issues(
        self,
        project_path: Optional[str] = None,
        state: str = "opened",
        search: Optional[str] = None,
        per_page: int = 20
    ) -> str:
        project = project_path or self.default_project
        if not project:
            return "ERROR: project_path is required (no default project configured)."
        url = f"{self._project_url(project)}/issues"
        params = {"state": state, "per_page": per_page}
        if search:
            params["search"] = search
        r = self._session.get(url, params=params, timeout=30)
        if r.status_code != 200:
            return f"ERROR: {r.status_code} {r.text}"
        return r.text  # JSON string

    @kernel_function(name="create_issue", description="Create a GitLab issue in the given project.")
    def create_issue(
        self,
        title: str,
        description: Optional[str] = None,
        project_path: Optional[str] = None,
        labels_csv: Optional[str] = None
    ) -> str:
        project = project_path or self.default_project
        if not project:
            return "ERROR: project_path is required (no default project configured)."
        url = f"{self._project_url(project)}/issues"
        data: Dict[str, Any] = {"title": title}
        if description:
            data["description"] = description
        if labels_csv:
            data["labels"] = labels_csv
        r = self._session.post(url, data=data, timeout=30)
        if r.status_code not in (200, 201):
            return f"ERROR: {r.status_code} {r.text}"
        return r.text

    @kernel_function(name="get_issue", description="Get a single issue by IID (project-scoped number).")
    def get_issue(self, issue_iid: int, project_path: Optional[str] = None) -> str:
        project = project_path or self.default_project
        if not project:
            return "ERROR: project_path is required (no default project configured)."
        url = f"{self._project_url(project)}/issues/{issue_iid}"
        r = self._session.get(url, timeout=30)
        if r.status_code != 200:
            return f"ERROR: {r.status_code} {r.text}"
        return r.text

    @kernel_function(name="search_merge_requests", description="Search MRs by state and text query.")
    def search_merge_requests(
        self,
        project_path: Optional[str] = None,
        state: str = "opened",
        search: Optional[str] = None,
        per_page: int = 20
    ) -> str:
        project = project_path or self.default_project
        if not project:
            return "ERROR: project_path is required (no default project configured)."
        url = f"{self._project_url(project)}/merge_requests"
        params: Dict[str, Any] = {"state": state, "per_page": per_page}
        if search:
            params["search"] = search
        r = self._session.get(url, params=params, timeout=30)
        if r.status_code != 200:
            return f"ERROR: {r.status_code} {r.text}"
        return r.text

    @kernel_function(name="add_labels_to_issue", description="Append labels to an existing issue by IID.")
    def add_labels_to_issue(
        self,
        issue_iid: int,
        labels_to_add_csv: str,
        project_path: Optional[str] = None
    ) -> str:
        # Get current labels
        current_json = self.get_issue(issue_iid=issue_iid, project_path=project_path)
        if current_json.startswith("ERROR:"):
            return current_json
        import json
        try:
            issue = json.loads(current_json)
            current_labels: List[str] = issue.get("labels", [])
        except Exception:
            return f"ERROR: could not parse current issue JSON: {current_json}"
        new_labels = [x.strip() for x in labels_to_add_csv.split(",") if x.strip()]
        merged = sorted(set(current_labels + new_labels))

        project = project_path or self.default_project
        if not project:
            return "ERROR: project_path is required (no default project configured)."
        url = f"{self._project_url(project)}/issues/{issue_iid}"
        data = {"labels": ",".join(merged)}
        r = self._session.put(url, data=data, timeout=30)
        if r.status_code != 200:
            return f"ERROR: {r.status_code} {r.text}"
        return r.text
