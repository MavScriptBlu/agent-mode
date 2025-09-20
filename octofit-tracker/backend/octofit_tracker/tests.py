from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard
from datetime import date

class UserModelTest(TestCase):
    def test_create_user(self):
        user = User.objects.create(username='testuser', email='test@example.com')
        self.assertEqual(user.username, 'testuser')

class TeamModelTest(TestCase):
    def test_create_team(self):
        user = User.objects.create(username='member', email='member@example.com')
        team = Team.objects.create(name='Test Team')
        team.members.add(user)
        self.assertEqual(team.name, 'Test Team')

class ActivityModelTest(TestCase):
    def test_create_activity(self):
        user = User.objects.create(username='activityuser', email='activity@example.com')
        activity = Activity.objects.create(user=user, activity_type='run', duration_minutes=30, calories_burned=300, date=date.today())
        self.assertEqual(activity.activity_type, 'run')

class WorkoutModelTest(TestCase):
    def test_create_workout(self):
        user = User.objects.create(username='workoutuser', email='workout@example.com')
        workout = Workout.objects.create(user=user, name='Morning Routine', date=date.today())
        self.assertEqual(workout.name, 'Morning Routine')

class LeaderboardModelTest(TestCase):
    def test_create_leaderboard(self):
        team = Team.objects.create(name='Leaderboard Team')
        leaderboard = Leaderboard.objects.create(team=team, total_points=100, week=date.today())
        self.assertEqual(leaderboard.total_points, 100)
