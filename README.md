# Scicode website

## Building it

```bash
pip install -r requirements.txt

# Check out submissions and turn them into table
git clone https://github.com/scicode-bench/submissions.git ../submissions
./leaderboard/create_leaderboard.py --input ../submissions --output docs/leaderboard_table.md

# Preview the website
mkdocs serve
```