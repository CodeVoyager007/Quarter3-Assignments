from typing import Dict, Set, List
import json
import os

class UserProgress:
    def __init__(self, user_id: str):
        self.user_id = user_id
        self.completed_lessons: Dict[str, Set[str]] = {
            'python': set(),
            'javascript': set(),
            'typescript': set(),
            'nextjs': set()
        }
        self.completed_challenges: Dict[str, Set[str]] = {
            'python': set(),
            'javascript': set(),
            'typescript': set(),
            'nextjs': set()
        }
        self.quiz_scores: Dict[str, Dict[str, int]] = {
            'python': {},
            'javascript': {},
            'typescript': {},
            'nextjs': {}
        }
        self.achievements: Set[str] = set()

    def add_completed_lesson(self, language: str, lesson_id: str):
        self.completed_lessons[language].add(lesson_id)
        self._check_achievements()
        self._save_progress()

    def add_completed_challenge(self, language: str, challenge_id: str):
        self.completed_challenges[language].add(challenge_id)
        self._check_achievements()
        self._save_progress()

    def add_quiz_score(self, language: str, quiz_id: str, score: int):
        self.quiz_scores[language][quiz_id] = score
        self._check_achievements()
        self._save_progress()

    def _check_achievements(self):
        # Check for language mastery achievements
        for language in self.completed_lessons:
            if len(self.completed_lessons[language]) >= 10:
                self.achievements.add(f"{language}_master")
            
            if len(self.completed_challenges[language]) >= 5:
                self.achievements.add(f"{language}_challenge_master")

        # Check for overall progress achievements
        total_lessons = sum(len(lessons) for lessons in self.completed_lessons.values())
        if total_lessons >= 20:
            self.achievements.add("dedicated_learner")
        if total_lessons >= 50:
            self.achievements.add("knowledge_seeker")

    def _save_progress(self):
        progress_dir = "user_progress"
        if not os.path.exists(progress_dir):
            os.makedirs(progress_dir)
        
        progress_file = os.path.join(progress_dir, f"{self.user_id}.json")
        with open(progress_file, 'w') as f:
            json.dump({
                'completed_lessons': {lang: list(lessons) for lang, lessons in self.completed_lessons.items()},
                'completed_challenges': {lang: list(challenges) for lang, challenges in self.completed_challenges.items()},
                'quiz_scores': self.quiz_scores,
                'achievements': list(self.achievements)
            }, f)

    @classmethod
    def load_progress(cls, user_id: str) -> 'UserProgress':
        progress = cls(user_id)
        progress_file = os.path.join("user_progress", f"{user_id}.json")
        
        if os.path.exists(progress_file):
            with open(progress_file, 'r') as f:
                data = json.load(f)
                progress.completed_lessons = {lang: set(lessons) for lang, lessons in data['completed_lessons'].items()}
                progress.completed_challenges = {lang: set(challenges) for lang, challenges in data['completed_challenges'].items()}
                progress.quiz_scores = data['quiz_scores']
                progress.achievements = set(data['achievements'])
        
        return progress

    def get_progress_stats(self) -> Dict:
        return {
            'total_lessons_completed': sum(len(lessons) for lessons in self.completed_lessons.values()),
            'total_challenges_completed': sum(len(challenges) for challenges in self.completed_challenges.values()),
            'average_quiz_score': {
                lang: sum(scores.values()) / len(scores) if scores else 0
                for lang, scores in self.quiz_scores.items()
            },
            'achievements': list(self.achievements)
        } 