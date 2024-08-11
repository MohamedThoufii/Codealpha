let flashcards = [];
let currentFlashcardIndex = -1;
let correctCount = 0;
let totalCount = 0;

function addFlashcard() {
    const questionInput = document.getElementById('question');
    const answerInput = document.getElementById('answer');

    const question = questionInput.value.trim();
    const answer = answerInput.value.trim();

    if (question && answer) {
        flashcards.push({ question, answer });
        questionInput.value = '';
        answerInput.value = '';
        alert('Flashcard added!');
    } else {
        alert('Please enter both a question and an answer.');
    }
}

function showFlashcard() {
    if (flashcards.length > 0) {
        currentFlashcardIndex = (currentFlashcardIndex + 1) % flashcards.length;
        const flashcard = flashcards[currentFlashcardIndex];
        document.getElementById('flashcard-question').textContent = flashcard.question;
        document.getElementById('flashcard-answer').style.display = 'none';
        document.getElementById('flashcard-answer').textContent = flashcard.answer;
        document.getElementById('show-answer-btn').style.display = 'inline';
        document.getElementById('correct-btn').style.display = 'none';
        document.getElementById('incorrect-btn').style.display = 'none';
    } else {
        alert('No flashcards available. Please add some flashcards first.');
    }
}

function showAnswer() {
    document.getElementById('flashcard-answer').style.display = 'block';
    document.getElementById('show-answer-btn').style.display = 'none';
    document.getElementById('correct-btn').style.display = 'inline';
    document.getElementById('incorrect-btn').style.display = 'inline';
}

function markCorrect() {
    correctCount++;
    totalCount++;
    updateScore();
    showFlashcard();
}

function markIncorrect() {
    totalCount++;
    updateScore();
    showFlashcard();
}

function updateScore() {
    document.getElementById('score').textContent = `Correct: ${correctCount} / ${totalCount}`;
}

// Initialize the first flashcard when the page loads
document.addEventListener('DOMContentLoaded', showFlashcard);
