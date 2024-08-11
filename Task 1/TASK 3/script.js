let workouts = [];
let totalDuration = 0;
let goal = 0;

function addWorkout() {
    const exerciseInput = document.getElementById('exercise');
    const durationInput = document.getElementById('duration');

    const exercise = exerciseInput.value.trim();
    const duration = parseInt(durationInput.value.trim());

    if (exercise && duration) {
        workouts.push({ exercise, duration });
        totalDuration += duration;
        updateWorkouts();
        updateProgress();
        exerciseInput.value = '';
        durationInput.value = '';
    } else {
        alert('Please enter both exercise and duration.');
    }
}

function setGoal() {
    const goalInput = document.getElementById('goal');
    goal = parseInt(goalInput.value.trim());

    if (goal) {
        updateProgress();
        goalInput.value = '';
    } else {
        alert('Please enter a valid goal.');
    }
}

function updateWorkouts() {
    const workoutsList = document.getElementById('workouts-list');
    workoutsList.innerHTML = '';

    workouts.forEach((workout, index) => {
        const li = document.createElement('li');
        li.textContent = `${workout.exercise}: ${workout.duration} minutes`;
        workoutsList.appendChild(li);
    });
}

function updateProgress() {
    const goalProgress = document.getElementById('goal-progress');
    const progress = document.getElementById('progress');

    goalProgress.textContent = goal ? `Goal: ${goal} minutes` : 'Goal: Not set';
    progress.textContent = `Total Duration: ${totalDuration} minutes`;
}

// Initialize with empty data
document.addEventListener('DOMContentLoaded', () => {
    updateWorkouts();
    updateProgress();
});
