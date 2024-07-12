#!/usr/bin/env python

import argparse
import dataclasses
from pathlib import Path
import pandas as pd
import json


@dataclasses.dataclass
class Submission:
    """Represents a single submission"""
    date: str
    author: str
    model: str
    scores: dict[str, float]
    
    @classmethod
    def from_file(cls, path: Path):
        data = json.loads(path.read_text())
        return cls(**data) 
    
    def to_single_score_dict(self, score="default") -> dict[str, float]:
        data = dataclasses.asdict(self)
        del data["scores"]
        data["score"] = self.scores[score]
        return data


class LeaderboardAggregator:
    def __init__(self):
        self.submissions = []
    
    def load_file(self, path: Path):
        submission = Submission.from_file(path)
        self.submissions.append(submission)
    
    def format_markdown(self, score="default") -> str:
        df = pd.DataFrame.from_records([s.to_single_score_dict(score) for s in self.submissions])
        print(df)
        df = df.sort_values(by="score", ascending=False)
        df = df.reset_index(drop=True)
        return df.to_markdown(index=False)
    
    def to_file(self, path: Path, score="default"):
        path.write_text(self.format_markdown(score))


def main(input: str, output: str) -> None:
    la = LeaderboardAggregator()
    for inpt in Path(input).rglob("score.json"):
        print("Loading", inpt)
        la.load_file(inpt)
    la.to_file(Path(output))


def cli():
    parser = argparse.ArgumentParser(description="Aggregate leaderboard data and format table")
    parser.add_argument("--input", help="Path to leaderboard data")
    parser.add_argument("--output", help="Path to save leaderboard table")
    return parser


if __name__ == "__main__":
    main(**vars(cli().parse_args()))