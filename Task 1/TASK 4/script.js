let lessons = [
    { title: "Lesson 1: Basics", content: "Introduction to basic phrases and vocabulary." },
    { title: "Lesson 2: Numbers", content: "Learn numbers from 1 to 100." },
    { title: "Lesson 3: Greetings", content: "Learn how to greet people." }
];

let quizzes = [
    { question: "Translate 'Hello' to Spanish", answer: "Hola" },
    { question: "Translate 'One' to Spanish", answer: "Uno" }
];

let currentQuizIndex = 0;
let correctAnswers = 0;
let totalAnswers = 0;

function showSection(sectionId) {
    document.querySelectorAll('.section').forEach(section => {
        section.classList.remove('active');
    });
    document.getElementById(sectionId).classList.add('active');
}

function loadLessons() {
    const lessonList = document.getElementById('lesson-list');
    lessonList.innerHTML = '';
    lessons.forEach(lesson => {
        const div = document.createElement('div');
        div.textContent = `${lesson.title}: ${lesson.content}`;
        lessonList.appendChild(div);
    });
}

function loadQuiz() {
    if (currentQuizIndex < quizzes.length) {
        const quiz = quizzes[currentQuizIndex];
        document.getElementById('quiz-question').textContent = quiz.question;
        document.getElementById('quiz-answer').value = '';
        document.getElementById('quiz-feedback').textContent = '';
    } else {
        document.getElementById('quiz-question').textContent = 'No more quizzes available.';
        document.getElementById('quiz-answer').style.display = 'none';
        document.getElementById('quiz-feedback').textContent = `You answered ${correctAnswers} out of ${totalAnswers} correctly.`;
    }
}

function submitAnswer() {
    const answer = document.getElementById('quiz-answer').value.trim();
    const quiz = quizzes[currentQuizIndex];
    totalAnswers++;
    if (answer.toLowerCase() === quiz.answer.toLowerCase()) {
        correctAnswers++;
        document.getElementById('quiz-feedback').textContent = 'Correct!';
    } else {
        document.getElementById('quiz-feedback').textContent = `Incorrect. The correct answer is ${quiz.answer}.`;
    }
    currentQuizIndex++;
    loadQuiz();
}

function updateProgress() {
    const progressTracker = document.getElementById('progress-tracker');
    progressTracker.textContent = `You have completed ${correctAnswers} out of ${totalAnswers} questions correctly.`;
}

function loadAchievements() {
    const achievementList = document.getElementById('achievement-list');
    achievementList.innerHTML = '';
    if (correctAnswers >= 5) {
        const li = document.createElement('li');
