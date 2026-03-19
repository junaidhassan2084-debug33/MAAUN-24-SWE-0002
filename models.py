from datetime import datetime

class Question:
    """Represents a single CBT question with options and correct answer."""
    
    def __init__(self, question_id, text, options, correct_answer):
        """Initialize a Question object.\n        \n        Args:\n            question_id (int): Unique identifier for the question\n            text (str): The question text\n            options (list): List of answer options (A, B, C, D)\n            correct_answer (str): The correct answer (A, B, C, or D)\n        """
        self.question_id = question_id
        self.text = text
        self.options = options
        self.correct_answer = correct_answer
    
    def is_correct(self, user_answer):
        """Check if user's answer is correct."""
        return user_answer.upper() == self.correct_answer.upper()
    
    def get_question_number(self):
        """Return the question number."""
        return self.question_id


class CBTTest:
    """Represents a complete CBT test session with multiple questions."""
    
    def __init__(self, test_name, questions):
        """Initialize a CBT Test.\n        \n        Args:\n            test_name (str): Name of the test\n            questions (list): List of Question objects\n        """
        self.test_name = test_name
        self.questions = questions
        self.total_questions = len(questions)
        self.user_answers = {}  
        self.score = 0
        self.start_time = None
        self.end_time = None
    
    def start_test(self):
        """Mark the test as started."""
        self.start_time = datetime.now()
    
    def submit_answer(self, question_id, user_answer):
        """Record a user's answer for a specific question."""
        self.user_answers[question_id] = user_answer
    
    def get_question(self, question_id):
        """Retrieve a specific question by ID."""
        for question in self.questions:
            if question.question_id == question_id:
                return question
        return None
    
    def calculate_score(self):
        """Calculate total score based on correct answers."""
        self.score = 0
        for question_id, user_answer in self.user_answers.items():
            question = self.get_question(question_id)
            if question and question.is_correct(user_answer):
                self.score += 1
        return self.score
    
    def end_test(self):
        """Mark the test as ended and calculate final score."""
        self.end_time = datetime.now()
        return self.calculate_score()
    
    def get_result_summary(self):
        """Generate a summary of test results.\n        \n        Returns:\n            dict: Dictionary containing test results\n        """
        if not self.end_time:
            self.end_test()
        
        duration = (self.end_time - self.start_time).total_seconds() if self.start_time else 0
        percentage = (self.score / self.total_questions * 100) if self.total_questions > 0 else 0
        
        return {
            'test_name': self.test_name,
            'score': self.score,
            'total_questions': self.total_questions,
            'percentage': round(percentage, 2),
            'submitted_at': self.end_time.strftime('%Y-%m-%d %H:%M:%S'),
            'duration_seconds': int(duration)
        }
    
    def get_detailed_results(self):
        """Return detailed breakdown of each question and answer."""
        results = []
        for question_id, user_answer in self.user_answers.items():
            question = self.get_question(question_id)
            is_correct = question.is_correct(user_answer) if question else False
            results.append({
                'question_num': question_id,
                'question_text': question.text,
                'user_answer': user_answer.upper(),
                'correct_answer': question.correct_answer,
                'is_correct': is_correct
            })
        return results


class TestBank:
    """Manages a collection of questions (Stack for Recently Viewed)."""
    
    def __init__(self):
        """Initialize the test bank with a stack for recently viewed questions."""
        self.questions = []
        self.recently_viewed = []
    
    def add_question(self, question):
        """Add a question to the test bank."""
        self.questions.append(question)
    
    def get_all_questions(self):
        """Retrieve all questions."""
        return self.questions
    
    def push_to_recently_viewed(self, question_id):
        """Add a question to recently viewed stack.\n        Uses Stack (LIFO) - most recent on top."""
        self.recently_viewed.append(question_id)
    
    def pop_recently_viewed(self):
        """Remove and return the most recently viewed question (Stack pop)."""
        if self.recently_viewed:
            return self.recently_viewed.pop()
        return None
    
    def get_recently_viewed(self):
        """Get the last 5 recently viewed questions (in reverse order)."""
        return self.recently_viewed[-5:] if self.recently_viewed else []
    
    def get_question(self, question_id):
        """Retrieve a specific question by ID."""
        for question in self.questions:
            if question.question_id == question_id:
                return question
        return None
