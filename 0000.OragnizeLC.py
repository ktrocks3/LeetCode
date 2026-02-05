import os, shutil, requests
from tqdm import tqdm

URL = "https://leetcode.com/graphql/"

QUERY = """
query problemsetQuestionList($categorySlug: String, $limit: Int, $skip: Int, $filters: QuestionListFilterInput) {
  problemsetQuestionList: questionList(
    categorySlug: $categorySlug
    limit: $limit
    skip: $skip
    filters: $filters
  ) {
    questions: data {
      frontendQuestionId: questionFrontendId
      difficulty
      title
      titleSlug
    }
  }
}
"""

HEADERS = {
    "Content-Type": "application/json",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) PythonRequests",
    "Referer": "https://leetcode.com/",
    "Origin": "https://leetcode.com",
}


def get_difficulty(problem_number: int) -> str:
    # Using searchKeywords to narrow results. We'll still exact-match the ID.
    payload = {
        "query": QUERY,
        "variables": {
            "categorySlug": "",
            "skip": 0,
            "limit": 50,
            "filters": {"searchKeywords": str(problem_number)},
        },
    }

    r = requests.post(URL, json=payload, headers=HEADERS, timeout=15)
    if r.status_code != 200:
        raise RuntimeError(f"{r.status_code} {r.reason}\n{r.text}")

    questions = r.json()["data"]["problemsetQuestionList"]["questions"]
    for q in questions:
        if str(q["frontendQuestionId"]) == str(problem_number):
            return q["difficulty"]

    raise LookupError(f"Problem #{problem_number} not found in results.")


files = []
for file in tqdm(os.listdir('.'), desc="Scanning files", ascii=True):
    if file.endswith(".py") and not file.startswith("0000") and file.split('.')[0].isdecimal():
        files.append((file, get_difficulty(int(file.split('.')[0]))))

for filename, diff in tqdm(files, desc="Organizing", ascii=True):
    os.makedirs(diff, exist_ok=True)
    shutil.move(filename, os.path.join(diff, filename))
