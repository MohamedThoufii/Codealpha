const quotes = [
    {
        quote: "The greatest glory in living lies not in never falling, but in rising every time we fall.",
        author: "Nelson Mandela"
    },
    {
        quote: "The way to get started is to quit talking and begin doing.",
        author: "Walt Disney"
    },
    {
        quote: "Your time is limited, don't waste it living someone else's life.",
        author: "Steve Jobs"
    },
    {
        quote: "If life were predictable it would cease to be life, and be without flavor.",
        author: "Eleanor Roosevelt"
    },
    {
        quote: "If you look at what you have in life, you'll always have more.",
        author: "Oprah Winfrey"
    },
    {
        quote: "If you set your goals ridiculously high and it's a failure, you will fail above everyone else's success.",
        author: "James Cameron"
    },
    {
        quote: "Life is what happens when you're busy making other plans.",
        author: "John Lennon"
    }
];

function generateQuote() {
    const randomIndex = Math.floor(Math.random() * quotes.length);
    const quote = quotes[randomIndex];
    document.getElementById('quote').textContent = `"${quote.quote}"`;
    document.getElementById('author').textContent = `- ${quote.author}`;
}

function shareOnTwitter() {
    const quoteText = document.getElementById('quote').textContent;
    const authorText = document.getElementById('author').textContent;
    const twitterUrl = `https://twitter.com/intent/tweet?text=${encodeURIComponent(quoteText + " " + authorText)}`;
    window.open(twitterUrl, '_blank');
}

// Initialize with a random quote when the page loads
document.addEventListener('DOMContentLoaded', generateQuote);
