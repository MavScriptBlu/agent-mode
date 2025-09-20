from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard
from datetime import date, timedelta
import random

class Command(BaseCommand):
    help = 'Populate the database with test data for users, teams, activities, workouts, and leaderboard.'

    def handle(self, *args, **options):
        users = []
        for i in range(5):
            user, _ = User.objects.get_or_create(
                username=f'user{i}',
                email=f'user{i}@example.com',
                first_name=f'First{i}',
                last_name=f'Last{i}'
            )
            users.append(user)
        self.stdout.write(self.style.SUCCESS('Created users.'))

        teams = []
        for i in range(2):
            team, _ = Team.objects.get_or_create(name=f'Team{i}')
            for user in users[i*2:(i+1)*2]:
                team.members.add(user)
            teams.append(team)
        self.stdout.write(self.style.SUCCESS('Created teams.'))

        for user in users:
            for j in range(3):
                Activity.objects.get_or_create(
                    user=user,
                    activity_type=random.choice(['run', 'walk', 'cycle']),
                    duration_minutes=random.randint(20, 60),
                    calories_burned=random.randint(100, 500),
                    date=date.today() - timedelta(days=j)
                )
        self.stdout.write(self.style.SUCCESS('Created activities.'))

        for user in users:
            Workout.objects.get_or_create(
                user=user,
                name='Full Body Workout',
                description='A test workout',
                date=date.today()
            )
        self.stdout.write(self.style.SUCCESS('Created workouts.'))

        for team in teams:
            Leaderboard.objects.get_or_create(
                team=team,
                total_points=random.randint(100, 1000),
                week=date.today()
            )
        self.stdout.write(self.style.SUCCESS('Created leaderboard.'))
        self.stdout.write(self.style.SUCCESS('Test data created successfully.'))
