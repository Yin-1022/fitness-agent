from datetime import datetime
from app.features.health_log.domain.entities.user_profile import UserProfile
from app.features.health_log.domain.entities.workout_session import WorkoutSession
from app.features.health_log.domain.entities.exercise_record import ExerciseRecord
from app.features.health_log.domain.entities.body_measurement import BodyMeasurement
from app.features.health_log.domain.entities.body_status_log import BodyStatusLog

def test_user_profile_creation():
    user_profile = UserProfile(
        id=1,
        name="John Doe",
        height_cm=180.0,
        goal="Lose weight",
        weekly_training_days_goal=3,
        experience_level="Intermediate",
        created_at=datetime.now(),
        updated_at=datetime.now()
    )
    assert user_profile.name == "John Doe"
    assert user_profile.height_cm == 180.0
    assert user_profile.goal == "Lose weight"
    assert user_profile.weekly_training_days_goal == 3
    assert user_profile.experience_level == "Intermediate"

def test_workout_session_creation():
    workout_session = WorkoutSession(
        id=1,
        user_id="user123",
        date=datetime.now(),
        duration_minutes=60,
        workout_type="Strength Training",
        title="Upper Body Workout",
        muscle_groups=["Chest", "Back", "Arms"],
        intensity_level=7,
        notes="Felt strong today.",
        source="Manual Entry",
        created_at=datetime.now(),
        updated_at=datetime.now()
    )
    assert workout_session.user_id == "user123"
    assert workout_session.duration_minutes == 60

def test_exercise_record_creation():
    exercise_record = ExerciseRecord(
        id=1,
        workout_session_id=1,
        exercise_name="Bench Press",
        muscle_group="Chest",
        sets=3,
        reps=10,
        weight_kg=80.0,
    )
    assert exercise_record.exercise_name == "Bench Press"
    assert exercise_record.sets == 3
    assert exercise_record.reps == 10
    assert exercise_record.weight_kg == 80.0

def test_body_measurement_creation():
    body_measurement = BodyMeasurement(
        id=1,
        user_id="user123",
        date=datetime.now(),
        weight_kg=75.0,
        body_fat_percentage=15.0,
        created_at=datetime.now(),
    )
    assert body_measurement.user_id == "user123"
    assert body_measurement.weight_kg == 75.0
    assert body_measurement.body_fat_percentage == 15.0

def test_body_status_log_creation():
    body_status_log = BodyStatusLog(
        id=1,
        user_id="user123",
        date=datetime.now(),
        sleep_hours=7.5,
        sleep_quality=8,
        fatigue_level=5,
        stress_level=4,
        soreness_level=3,
        soreness_parts=["Back", "Legs"],
        mood_level=7,
        notes="Feeling good today.",
        source="Manual Entry",
        created_at=datetime.now(),
        updated_at=datetime.now()
    )
    assert body_status_log.user_id == "user123"
    assert body_status_log.sleep_hours == 7.5
    assert body_status_log.sleep_quality == 8